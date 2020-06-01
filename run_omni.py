from Normalize import normalize
from subprocess import call
from generate_omnicorp_table_script import generate_psql_script

def go():
    #normalize('omnicorp_input','omnicorp_output',pmidcol=0,termcol=1,labelcol=None)
    #call('sort omnicorp_output/annotation_0.txt | uniq > omnicorp_output/annotation_1.txt', shell=True)
    #make_final('omnicorp_output','omnicorp_final')
    generate_psql_script('omnicorp_final',set(['CGNC','Curie','ENSEMBL','FBDV']))

def make_final(indir,outdir):
    prefix=''
    ofile = None
    with open(f'{indir}/annotation_1.txt','r') as inf:
        for line in inf:
            x = line.strip().split('\t')
            cpref = x[0].split(':')[0]
            if cpref != prefix:
                if ofile is not None:
                    ofile.close()
                prefix = cpref
                ofile = open(f'{outdir}/{prefix}','w')
            pmid = x[1].split('/')[-1]
            ofile.write(f'{pmid}\t{x[0]}\n')
    ofile.close()

if __name__ == '__main__':
    go()