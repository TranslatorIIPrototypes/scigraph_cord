from Normalize import normalize
from subprocess import call
from generate_omnicorp_table_script import generate_psql_script

def go():
    normalize('omnicorp_input','omnicorp_output',pmidcol=0,termcol=1,labelcol=None)
    call('sort -T . omnicorp_output/annotation_0.txt | uniq > omnicorp_output/annotation_1.txt', shell=True)
    call('sort output/annotation_0.txt | uniq > omnicorp_output/annotation_1.txt', shell=True)
    ##
    # annotation_1 looks like
    # CHEBI:100       https://www.ncbi.nlm.nih.gov/pubmed/30176279
    # CHEBI:100       https://www.ncbi.nlm.nih.gov/pubmed/31121832
    # CHEBI:100       https://www.ncbi.nlm.nih.gov/pubmed/3877941
    # 
    # Now need to combine with the cord data which looks like:
    # MONDO:0100096	PMID:32122113
    # MONDO:0100096	PMID:32061198
    # MONDO:0100096	DOI:10.1016/0168-1702(86)90086-9
    # ENVO:01000965	DOI:10.1016/0378-1097(85)90057-6d
    # now clean up
    curify('omnicorp_output/annotation_1.txt', 'omnicorp_output/annotation_2.txt')
    #combine omnicorp and cord
    call('cat omnicorp_output/annotation_2.txt output/annotation_0.txt | sort | uniq > omnicorp_output/annotation_3.txt', shell=True)
    make_final('omnicorp_output','omnicorp_final')
    generate_psql_script('omnicorp_final',set(['CGNC','Curie','ENSEMBL','FBDV']))

def curify(infname,outfname):
    with open(infname,'r') as inf, open(outfname,'w') as outf:
        for line in inf:
            x = line.strip().split('\t')
            pmid = x[1].split('/')[-1]
            outf.write(f'{x[0]}\tPMID:{pmid}\n')

def make_final(indir,outdir):
    prefix=''
    ofile = None
    with open(f'{indir}/annotation_3.txt','r') as inf:
        for line in inf:
            x = line.strip().split('\t')
            cpref = x[0].split(':')[0]
            if cpref != prefix:
                if ofile is not None:
                    ofile.close()
                prefix = cpref
                ofile = open(f'{outdir}/{prefix}','w')
            pmid = x[1].split(':')[-1]
            ofile.write(f'{pmid}\t{x[0]}\n')
    ofile.close()

if __name__ == '__main__':
    go()
