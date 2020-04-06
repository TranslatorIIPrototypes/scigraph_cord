all_pubs = 42446
relevance = 1./30.

with open('output/scoredpairs_sorted.txt') as inf, open('output/loadpairs.txt','w') as outf:
    n=0
    h = inf.readline()
    outf.write('Term1\tTerm2\tTerm1Counts\tTerm2Counts\tSharedCounts\tEnrichment_p\tEffective_Pubs\n')
    for line in inf:
        x = line.strip().split('\t')
        t1 = x[0]
        t2 = x[1]
        source_pubs = int(x[4])
        target_pubs = int(x[5])
        edge_pubs = int(x[6])
        p = float(x[7])
        if p > 1e-7:
            break
        cov = (edge_pubs / all_pubs) - (source_pubs / all_pubs) * (target_pubs / all_pubs)
        cov = max((cov, 0.0))
        effective_pubs = cov * all_pubs * relevance
        outf.write(f'{t1}\t{t2}\t{source_pubs}\t{target_pubs}\t{edge_pubs}\t{p}\t{effective_pubs}\n')
        n += 1
        #if n > 1000:
        #    break
