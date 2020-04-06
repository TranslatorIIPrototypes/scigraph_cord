import os
import requests
import sys

class Normalizer():
    def __init__(self):
        self.url = 'https://nodenormalization-sri.renci.org/get_normalized_nodes'
        self.iri_to_curie = {}
        self.iri_to_label = {}
        self.curie_to_normalized = {}
        self.curie_to_type = {}
        self.curie_to_label = {}
    def add(self,iri,label):
        if iri in self.iri_to_curie:
            return
        newcurie = self.curify(iri)
        self.iri_to_curie[iri] = newcurie
        self.iri_to_label[iri] = label
    def curify(self,iri):
        #print(iri)
        ns = iri.split('/')
        n = ns[-1]
        if n.startswith('gene_symbol_report'):
            return f"HGNC:{n.split('=')[-1]}"
        if ':' in n:
            return n
        x = n.split('_')
        if len(x) == 2:
            x[0] = x[0].upper()
            return ':'.join(x)
        if len(x) == 1:
            return f'{ns[-2].upper()}:{ns[-1]}'
        print(iri)
        return(iri)
    def normalize_all(self):
        batchsize=20
        unnormalized_curies = self.iri_to_curie.values()
        print(len(unnormalized_curies))
        print(len(unnormalized_curies)/batchsize)
        batch = []
        for x in unnormalized_curies:
            batch.append(x)
            if len(batch) >= batchsize:
                batchmap,typemap,labelmap = self.normalize_batch(batch)
                self.curie_to_normalized.update(batchmap)
                self.curie_to_type.update(typemap)
                self.curie_to_label.update(labelmap)
                batch= []
        if len(batch) > 0:
            batchmap,typemap,labelmap = self.normalize_batch(batch)
            self.curie_to_normalized.update(batchmap)
            self.curie_to_type.update(typemap)
            self.curie_to_label.update(labelmap)
    def normalize_batch(self,batch):
        result = requests.get('https://nodenormalization-sri.renci.org/get_normalized_nodes', params={'curie': batch})
        r = result.json()
        nb = {}
        types = {}
        labels = {}
        for b in batch:
            back = r[b]
            if r[b] is None:
                nb[b] = b
                types[b] = '[named_thing]'
            else:
                bid = r[b]['id']['identifier']
                try:
                    labels[b] = r[b]['id']['label']
                except KeyError:
                    pass
                nb[b] = bid
                types[b] = r[b]['type']
        return nb,types,labels
    def write(self,ofile):
        with open(ofile, 'w') as outf:
            outf.write('input_term\tcurie\tnormalized_curie\tsemantic_type\tlabel\n')
            for iri,curie in self.iri_to_curie.items():
                normcurie = self.curie_to_normalized[curie]
                normtype = self.curie_to_type[curie]
                if curie in self.curie_to_label:
                    label = self.curie_to_label[curie]
                else:
                    label = self.iri_to_label[iri]
                outf.write(f'{iri}\t{curie}\t{normcurie}\t{normtype}\t{label}\n')


def work_on_rfiles(indir,outdir):
    normy = Normalizer()
    rfiles = os.listdir(indir)
    #for rf in rfiles[:1]:
    for rf in rfiles:
        with open(f'{indir}/{rf}','r') as inf:
            for line in inf:
                x = line.strip().split('\t')
                pmid = x[0]
                term = x[6]
                label = x[7].split(']')[0][1:]
                normy.add(term,label)
    normy.normalize_all()
    normy.write(f'{outdir}/normalized.txt')

if __name__ == '__main__':
    work_on_rfiles(sys.argv[1],sys.argv[2])
