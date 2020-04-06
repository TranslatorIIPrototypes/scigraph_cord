import os
from collections import defaultdict

def load_norms():
    norms = {}
    names = {}
    with open('output/renormalized.txt','r') as inf:
        header = inf.readline()
        for line in inf:
            x = line.strip().split('\t')
            iri = x[0]
            norm = x[2]
            name = x[-1]
            norms[iri] = norm
            names[norm] = name
    return norms,names

def work_on_rfiles(indir,outdir):
    norms,names = load_norms()
    terms_to_papers = defaultdict(set)
    rfiles = os.listdir(indir)
    for rf in rfiles:
        with open(f'{indir}/{rf}','r') as inf:
            for line in inf:
                x = line.strip().split('\t')
                pmid = x[0]
                term = x[6]
                try:
                    nterm = norms[term]
                    terms_to_papers[nterm].add(pmid)
                except KeyError:
                    #this is a crappy identifier, let's just keep going
                    pass
    terms = list(terms_to_papers.keys())
    with open(f'{outdir}/pairs.txt','w') as outf:
        outf.write('Term1\tTerm2\tLabel1\tLabel2\tCountTerm1\tCountTerm2\tSharedCount\n')
        for i,t_1 in enumerate(terms):
            for t_2 in terms[i+1:]:
                s1 = terms_to_papers[t_1]
                s2 = terms_to_papers[t_2]
                pair = s1.intersection(s2)
                if len(pair) > 0:
                    label1 = names[t_1]
                    label2 = names[t_2]
                    outf.write(f'{t_1}\t{t_2}\t{label1}\t{label2}\t{len(s1)}\t{len(s2)}\t{len(pair)}\n')

if __name__ == '__main__':
    work_on_rfiles('input', 'output')

