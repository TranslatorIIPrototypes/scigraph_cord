garbage_curies = set(['MONDO:0019395', #Hinman syndrome with synonym "HAS",
                      'MONDO:0012833', #"CAN"
                      'MONDO:0000001', #disease
                      'MONDO:0004967', #"ALL"
                      'UBERON:0014899', #"ALL",
                      'HP:0000001',
                      'UBERON:0006611', #Has synonym test
                      'ENVO:00000026', #well
                      'CHEBI:33232', #application
                      'CHEBI:75958', #solution
                      'ENVO:01000584', #table
                      'ENVO:2000036', #generates
                      'HP:0012824', #severity
                      'HP:0012830', #Position
                      'HP:0012834', #Right
                      'HP:0012835', #Left
                      'HP:0032320', #Affected
                      'HP:0040279', #Frequency
                      'HP:0040285', #Excluded
                      'CHEBI:24433', #Group
                      'CHEBI:52217', #Pharmaceutical
                      'CHEBI:23888', #Drug
                      'CHEBI:50906', #Role
                      'HP:0011009', #Acute
                      'HP:0012828', #Severe
                      'HP:0025254', #Ameliorated by
                      'HP:0032322', #Healthy
                      'MONDO:0021137', #not rare
                      'NCBITaxon:order',
                      'NCBITaxon:family',
                      'CHEBI:35225', #buffer
                      'CHEBI:60004', #mixture
                      'CHEBI:25367', #molecule
                      'GO:0005623', #cell
                      'FOODON:03420236', #foodon
                      'ENVO:01000605', #car
                      'FOODON:00003004', #animal
                      'GO:0005488', #binding
                      'HP:0012825', #Mild
                      'NCBIGene:4233', #MET
                      'NCBIGene:55364', #IMPACT
                      'NCBIGene:6418', #SET
                      'HP:0030646', #Peripheral
                      'HP:0040282', #Frequent
                      'NCBIGene:94005', #PIGS
                      'HP:0003674', #Onset
                      'NCBIGene:3815', #KIT
                      'NCBIGene:4280', #MICE
                      'UBERON:0004529', #anatomical projection
                      'HP:0011010', #Chronic
                      'CHEBI:33893', #reagent
                      'MONDO:0045042', #localized
                      'FOODON:03430131', #whole
                      'HP:0025303', #episodic
                      'HP:0003745', #Sporadic
                      'HP:0003676', #Progressive
                      'HP:0025275', #Lateral
                      'HP:0020034', #Diffuse
                      'HP:0031797', #Clinical course
                      'HP:0012833', #Unilateral
                      'CHEBI:75830', #HOME
                      'CHEBI:33731', #cluster
                      'NCBITaxon:class',
                      'NCBITaxon:species',
                      'MONDO:0021141', #acquired
                      'ENVO:00000444', #clearing
                      'ENVO:00000427', #meander
                      'CHEBI:33250', #atom
                      'ENVO:01000604', #vehicle
                      'HP:0025297', #Prolongued
                      'HP:0012840', #Proximal
                      'ENVO:01000588', #sofa
                      'CHEBI:3608', #protein
                      'ENVO:00000480', #peak
                      'HP:0012829', #Profound
                      ])

def go(original_file,final_file):
    with open(original_file,'r') as inf, open(final_file,'w') as outf:
        h = inf.readline()
        outf.write(h)
        for line in inf:
            x = line.strip().split('\t')
            if x[0].startswith('http://dbpedia.org/resource/'):
                continue
            if x[0].startswith('http://purl.org/dc/elements/'):
                continue
            if x[0].startswith('http://xmlns.com/foaf/'):
                continue
            if x[0].startswith('http://flybase.org/'):
                continue
            if x[0].startswith('https://www.wikidata.org/'):
                continue
            if x[-1].startswith('obsolete'):
                continue
            if x[-3] in garbage_curies:
                continue
            if x[-2] != "[named_thing]":
                outf.write(line)
            else:
                prefix = x[-3].split(':')[0]
                if prefix in ['DDANAT','UO','SO','RO','EFO','PR','MF','OBI','VO','BFO','PATO','IAO','BSPO','IDO',
                              'BTO','http','TERMS','OGMS','FMA','MP','MPATH','NBO','MA','UBPROP','UBREL','CARO',
                              'PCO','OBA','CLO','EO','FBBT','CHMO','SIO','OMIT','CP','GAZ','ORPHANET','TO','OPL',
                              'ZFA','NCIT','ZEA','MOD','MGI','REO','OMIABIS','GENE','WBLS']:
                    #hopefully we're picking PR up with hgnc
                    #hopefully we're picking BTO,CLO up with CL
                    #hopefully we're picking MP up with HP
                    #hopefully we're picking NBO up with HP/MONDO
                    #hopefully we're picking FBBT up with UBERON
                    #hopefully we're picking ORPHANET up with MONDO
                    #OBA seems like we don't have a good place for it
                    continue
                if prefix == 'MONDO':
                    x[3] = "['disease', 'named_thing', 'biological_entity', 'disease_or_phenotypic_feature']"
                    outf.write('\t'.join(x))
                    outf.write('\n')
                    continue
                if prefix in 'CHEBI':
                    #hardcoding some conversions to get around issues with current nn
                    chebis = {'CHEBI:26158':'CHEBI:37848',
                              'CHEBI:22584':'CHEBI:2762',
                              'CHEBI:185922':'CHEBI:40154',
                              'CHEBI:2360':'CHEBI:421707',
                              'CHEBI:153671':'CHEBI:80240',
                              'CHEBI:64208':'CHEBI:90693',
                              'CHEBI:4836':'CHEBI:28792',
                              'CHEBI:33097':'CHEBI:35227'}
                    x[-3] = chebis[x[-3]]
                    x[3] = "['chemical_substance', 'molecular_entity', 'biological_entity', 'named_thing']"
                    outf.write('\t'.join(x))
                    outf.write('\n')
                    continue
                if prefix in ['UBERON','HP','GO','CL']:
                    # If a mondo or other good one gets here, it is old/not normalizing correctly
                    continue
                if prefix in ['DEPICTED']:
                    #These are things that aren't real prefixes, but our iri munging makes them and we want to ignore
                    continue
                if '#' in x[-3]:
                    print(x)
                    continue
                if x[-3].startswith('EFO:'):
                    #For the most part, EFO will either be unique, or they should be folded into a MONDO/HP
                    # if the latter, then hopefully those will be picked up independently
                    x[3] = "['phenotypic_feature', 'named_thing', 'biological_entity', 'disease_or_phenotypic_feature']"
                    outf.write('\t'.join(x))
                    outf.write('\n')
                    continue
                if x[-3].startswith('NCBITAXON:'):
                    p = x[-3].split(':')
                    x[-3] = f'NCBITaxon:{p[1]}'
                    x[-2] = "['organism_taxon','named_thing']"
                    outf.write('\t'.join(x))
                    outf.write('\n')
                    continue
                if x[-3].startswith('HSAPDV:'):
                    p = x[-3].split(':')
                    x[-3] = f'HsapDv:{p[1]}'
                    x[-2] = "['life_stage','organismal_entity','named_thing']"
                    outf.write('\t'.join(x))
                    outf.write('\n')
                    continue
                if x[-3].startswith('ECTO:'):
                    x[3] = "['chemical_exposure', 'exposure_event', 'named_thing']"
                    outf.write('\t'.join(x))
                    outf.write('\n')
                    continue
                if x[-3].startswith('ENVO:'):
                    x[3] = "['environmental_feature', 'planetary_entity', 'named_thing']"
                    outf.write('\t'.join(x))
                    outf.write('\n')
                    continue
                if x[-3].startswith('HANCESTRO:'):
                    x[3] = "['population_of_individual_organisms', 'named_thing']"
                    outf.write('\t'.join(x))
                    outf.write('\n')
                    continue
                if x[-3].startswith('FAO:') or x[-3].startswith('PO:'):
                    x[3] = "['anatomical_entity', 'organismal_entity', 'biological_entity', 'named_thing']"
                    outf.write('\t'.join(x))
                    outf.write('\n')
                    continue
                if x[-3].startswith('FOODON:'):
                    x[3] = "['food', 'named_thing']"
                    outf.write('\t'.join(x))
                    outf.write('\n')
                    continue
                print('?')
                print(line)
                exit()


if __name__ == '__main__':
    go('output/normalized.txt','output/renormalized.txt')