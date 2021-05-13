import os

def write_block(dname,prefix,outf):
    use_pref = '_'.join(prefix.split('.'))
    tablename = 'omnicorp.{}'.format(use_pref)
    outf.write('CREATE TABLE {} ( pubmedid varchar(255), curie varchar(255) );\n'.format(tablename))
    outf.write(f"\copy {tablename} FROM '{dname}/{prefix}' DELIMITER E'\\t' CSV\n")
    outf.write("CREATE INDEX ON {} (pubmedid);\n".format(tablename))
    outf.write("CREATE INDEX ON {} (curie);\n".format(tablename))

def generate_psql_script(dname,ignoreset):
    with open('create_omnicorp.sql','w') as sqlfile:
        sqlfile.write('CREATE SCHEMA omnicorp;\n')
        files = os.listdir(dname)
        for prefix in files:
            if prefix not in ignoreset:
                write_block(dname,prefix,sqlfile)

#psql -U murphy robokop -f create_omnicorp.sql
#psql -h stars-k1.edc.renci.org -p 30333 -f create_omnicorp.sql robokop murphy
