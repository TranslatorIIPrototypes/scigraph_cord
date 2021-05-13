from collections import defaultdict
import numpy as np
from scipy.stats import chi2_contingency

def generate_covid_papers():
    covids = set(['MONDO:0100096','NCBITaxon:2697049'])
    covidpapers = set()
    with open('output/annotation_0.txt','r') as inf:
        header = inf.readline()
        for line in inf:
            x = line.strip().split('\t')
            curie = x[0]
            if curie in covids:
                covidpapers.add(x[1]) 
    return covidpapers

def generate_covid_counts():
    covidpapers = generate_covid_papers()
    papers = defaultdict(set)
    with open('output/annotation_0.txt','r') as inf:
        header = inf.readline()
        for line in inf:
            x = line.strip().split('\t')
            curie = x[0]
            paper = x[1]
            if paper in covidpapers:
                papers[curie].add(paper)
    with open('output/covid_counts.txt','w') as outf:
        ntotal = len(covidpapers)
        outf.write('Term\tNumWithCovid\tNumWithoutCovid\n')
        for term in papers:
            n = len(papers[term])
            outf.write(f'{term}\t{n}\t{ntotal-n}\n')

def generate_omnicorp_counts():
    papers = defaultdict(set)
    all_papers = set()
    with open('omnicorp_output/annotation_0.txt','r') as inf:
        header = inf.readline()
        for line in inf:
            x = line.strip().split('\t')
            curie = x[0]
            paper = x[1]
            papers[curie].add(paper)
            all_papers.add(paper)
    with open('omnicorp_output/counts.txt','w') as outf:
        ntotal = len(all_papers)
        for curie in papers:
            n = len(papers[curie])
            outf.write(f'{curie}\t{n}\t{ntotal-n}\n')
   

def read_covid_counts():
    counts = {}
    with open('output/covid_counts.txt','r') as inf:
        heder = inf.readline()
        for line in inf:
            x = line.strip().split('\t')
            counts[x[0]] = ( int(x[1]), int(x[2]) )
    return counts

def generate_statistics():
    covid_counts = read_covid_counts()
    with open('output/covid_scores.txt','w') as outf, open('omnicorp_output/counts.txt','r') as inf:
        for line in inf:
            x = line.strip().split('\t')
            curie = x[0]
            if curie not in covid_counts:
                continue
            non_covid_counts = (int(x[1]), int(x[2]))
            # I only care about the cases where the covid freq is greater than the non-covid
            covid_total = covid_counts[curie][0] + covid_counts[curie][1]
            covid_f = covid_counts[curie][0] / covid_total
            non_covid_total = non_covid_counts[0] + non_covid_counts[1]
            non_covid_f = non_covid_counts[0] / non_covid_total
            if non_covid_f > covid_f:
                continue
            obs = np.array( [ [covid_counts[curie][0], covid_counts[curie][1]], [non_covid_counts[0], non_covid_counts[1]]])
            c2, p, dof, ex = chi2_contingency(obs)
            outf.write(f'{curie}\t{covid_f}\t{non_covid_f}\t{c2}\t{p}\n')

def add_labels():
    labels = {}
    with open('output/normalized.txt','r') as inf:
        for line in inf:
            x = line.strip().split('\t')
            curie = x[0]
            label = x[2]
            labels[curie] = label
    with open('output/covid_scores.txt','r') as inf, open('output/labeled_covid_scores.txt','w') as outf:
        for line in inf:
            x = line.strip().split('\t')
            outf.write(f'{labels[x[0]]}\t{line}')
 
def finalize():
    good = set(['MONDO:0100096'])
    bad = set()
    with open('output/removes.txt','r') as inf:
        for line in inf:
            x = line.strip().split('\t')[1]
            bad.add(x)
    with open('final_output/pairs.txt','w') as outf, open('output/labeled_covid_scores.txt','r') as inf:
        outf.write('Term1\tTerm2\tEnrichment_p\tEffective_Pubs\n')
        for line in inf:
            x = line.strip().split('\t')
            p = float(x[-1])
            if p == 0:
                if x[1] not in bad:
                    c2 = float(x[4])
                    outf.write(f'MONDO:0100096\t{x[1]}\t{p}\t{c2/10000}\n')
                    good.add(x[1])
    with open('final_output/normalized.txt','w') as outf, open('output/normalized.txt','r') as inf:
        outf.write(inf.readline())
        for line in inf:
            x = line.strip().split('\t')[0]
            if x in good:
                outf.write(line)

if __name__ == '__main__':
    generate_covid_counts()
    generate_omnicorp_counts()
    generate_statistics()
    add_labels()
    finalize()
   
