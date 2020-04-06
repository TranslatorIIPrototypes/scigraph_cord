from scipy.stats import hypergeom

total_paper_count=42446

with open('output/pairs.txt', 'r') as inf, open('output/scoredpairs.txt', 'w') as outf:
    header = inf.readline().strip()
    outf.write(header)
    outf.write(f'\tscore\n')
    for line in inf:
        parts = line.strip().split('\t')
        Term1 = parts[0]
        Term2 = parts[1]
        Label1 = parts[2]
        Label2 = parts[3]
        CountTerm1 = int(parts[4])
        CountTerm2 = int(parts[5])
        SharedCount = int(parts[6])
        # The hypergeometric distribution models drawing objects from a bin.
        # For co-occurence, suppose that the number papers with the first term is the number of draws (ndraws)
        # And the total number of papers is total_paper_count, representing how many things could be drawn from (M)
        # Then number of papers with term 2 (n) is total number of Type I objects.
        # The random variate(x) represents the number of Type I objects in N drawn (the number of papers with both)
        #  without replacement from the total population (len curies).
        enrichp = hypergeom.sf(SharedCount - 1, total_paper_count, CountTerm2, CountTerm1)
        parts.append(str(enrichp))
        outf.write('\t'.join(parts))
        outf.write('\n')
