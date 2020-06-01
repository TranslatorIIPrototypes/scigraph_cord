files={}
with open('output/annotation_0.txt','r') as inf:
    for line in inf:
        prefix = line.strip().split(':')[0]
        if prefix not in files:
            outf = open(f'output/omnicorp.{prefix}','w')
            files[prefix] = outf
        files[prefix].write(line)
for f in files.values():
    f.close()