import os
from scipy.stats import hypergeom
from collections import defaultdict

def make_pairs_by_type(wdir,p_cutoff=1e-7):
    relevance = 1. / 30.
    terms_to_papers = defaultdict(set)
    rfiles = os.listdir(wdir)
    types = {}
    with open(f'{wdir}/normalized.txt','r') as inf:
        h = inf.readline()
        for line in inf:
            x = line.strip().split('\t')
            types[x[0]] = x[1].split("'")[1]
    papers_to_types = defaultdict(set)
    for rf in rfiles:
        if rf.startswith('annotation'):
            with open(f'{wdir}/{rf}','r') as inf:
                h = inf.readline()
                for line in inf:
                    x = line.strip().split('\t')
                    term = x[0]
                    pmid = x[1]
                    terms_to_papers[term].add(pmid)
                    papers_to_types[pmid].add(types[term])
    type_pairs = defaultdict( lambda: defaultdict( int) )
    for pmid,ptypes in papers_to_types.items():
        typesl = list(ptypes)
        for i,typei in enumerate(typesl):
            for typej in typesl[i:]:
                type_pairs[typei][typej] += 1
                if typei != typej:
                    type_pairs[typej][typei] += 1
    terms = list(terms_to_papers.keys())
    with open(f'{wdir}/pairsbt.txt','w') as outf:
        outf.write('Term1\tTerm2\tCountTerm1\tCountTerm2\tSharedCount\tTotal_papers\tEnrichment_p\tEffective_Pubs\n')
        for i,Term1 in enumerate(terms):
            for Term2 in terms[i+1:]:
                type1 = types[Term1]
                type2 = types[Term2]
                total_paper_count = type_pairs[type1][type2]
                terms1 = terms_to_papers[Term1]
                terms2 = terms_to_papers[Term2]
                SharedCount = len(terms1.intersection(terms2))
                CountTerm1 = len(terms1)
                CountTerm2 = len(terms2)
                if SharedCount > 0:
                    enrichp = hypergeom.sf(SharedCount - 1, total_paper_count, CountTerm2, CountTerm1)
                    if enrichp < p_cutoff:
                        cov = (SharedCount / total_paper_count) - (CountTerm1 / total_paper_count) * (CountTerm2 / total_paper_count)
                        cov = max((cov, 0.0))
                        effective_pubs = cov * total_paper_count * relevance
                        outf.write(f'{Term1}\t{Term2}\t{CountTerm1}\t{CountTerm2}\t{SharedCount}\t{total_paper_count}\t{enrichp}\t{effective_pubs}\n')


def make_pairs(wdir,total_paper_count,p_cutoff=1e-7):
    relevance = 1. / 30.
    terms_to_papers = defaultdict(set)
    rfiles = os.listdir(wdir)
    for rf in rfiles:
        if rf.startswith('annotation'):
            with open(f'{wdir}/{rf}','r') as inf:
                h = inf.readline()
                for line in inf:
                    x = line.strip().split('\t')
                    term = x[0]
                    pmid = x[1]
                    terms_to_papers[term].add(pmid)
    terms = list(terms_to_papers.keys())
    with open(f'{wdir}/pairs.txt','w') as outf:
        outf.write('Term1\tTerm2\tCountTerm1\tCountTerm2\tSharedCount\tEnrichment_p\tEffective_Pubs\n')
        for i,Term1 in enumerate(terms):
            for Term2 in terms[i+1:]:
                terms1 = terms_to_papers[Term1]
                terms2 = terms_to_papers[Term2]
                SharedCount = len(terms1.intersection(terms2))
                CountTerm1 = len(terms1)
                CountTerm2 = len(terms2)
                if SharedCount > 0:
                    enrichp = hypergeom.sf(SharedCount - 1, total_paper_count, CountTerm2, CountTerm1)
                    if enrichp < p_cutoff:
                        cov = (SharedCount / total_paper_count) - (CountTerm1 / total_paper_count) * (CountTerm2 / total_paper_count)
                        cov = max((cov, 0.0))
                        effective_pubs = cov * total_paper_count * relevance
                        outf.write(f'{Term1}\t{Term2}\t{CountTerm1}\t{CountTerm2}\t{SharedCount}\t{enrichp}\t{effective_pubs}\n')

