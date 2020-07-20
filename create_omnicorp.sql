CREATE SCHEMA omnicorp;
CREATE TABLE omnicorp.CHEBI ( pubmedid int, curie varchar(255) );
\copy omnicorp.CHEBI FROM 'omnicorp_final/CHEBI' DELIMITER E'\t' CSV
CREATE INDEX ON omnicorp.CHEBI (pubmedid);
CREATE INDEX ON omnicorp.CHEBI (curie);
CREATE TABLE omnicorp.CL ( pubmedid int, curie varchar(255) );
\copy omnicorp.CL FROM 'omnicorp_final/CL' DELIMITER E'\t' CSV
CREATE INDEX ON omnicorp.CL (pubmedid);
CREATE INDEX ON omnicorp.CL (curie);
CREATE TABLE omnicorp.ECTO ( pubmedid int, curie varchar(255) );
\copy omnicorp.ECTO FROM 'omnicorp_final/ECTO' DELIMITER E'\t' CSV
CREATE INDEX ON omnicorp.ECTO (pubmedid);
CREATE INDEX ON omnicorp.ECTO (curie);
CREATE TABLE omnicorp.ENVO ( pubmedid int, curie varchar(255) );
\copy omnicorp.ENVO FROM 'omnicorp_final/ENVO' DELIMITER E'\t' CSV
CREATE INDEX ON omnicorp.ENVO (pubmedid);
CREATE INDEX ON omnicorp.ENVO (curie);
CREATE TABLE omnicorp.FAO ( pubmedid int, curie varchar(255) );
\copy omnicorp.FAO FROM 'omnicorp_final/FAO' DELIMITER E'\t' CSV
CREATE INDEX ON omnicorp.FAO (pubmedid);
CREATE INDEX ON omnicorp.FAO (curie);
CREATE TABLE omnicorp.FOODON ( pubmedid int, curie varchar(255) );
\copy omnicorp.FOODON FROM 'omnicorp_final/FOODON' DELIMITER E'\t' CSV
CREATE INDEX ON omnicorp.FOODON (pubmedid);
CREATE INDEX ON omnicorp.FOODON (curie);
CREATE TABLE omnicorp.GO ( pubmedid int, curie varchar(255) );
\copy omnicorp.GO FROM 'omnicorp_final/GO' DELIMITER E'\t' CSV
CREATE INDEX ON omnicorp.GO (pubmedid);
CREATE INDEX ON omnicorp.GO (curie);
CREATE TABLE omnicorp.HANCESTRO ( pubmedid int, curie varchar(255) );
\copy omnicorp.HANCESTRO FROM 'omnicorp_final/HANCESTRO' DELIMITER E'\t' CSV
CREATE INDEX ON omnicorp.HANCESTRO (pubmedid);
CREATE INDEX ON omnicorp.HANCESTRO (curie);
CREATE TABLE omnicorp.HP ( pubmedid int, curie varchar(255) );
\copy omnicorp.HP FROM 'omnicorp_final/HP' DELIMITER E'\t' CSV
CREATE INDEX ON omnicorp.HP (pubmedid);
CREATE INDEX ON omnicorp.HP (curie);
CREATE TABLE omnicorp.HsapDv ( pubmedid int, curie varchar(255) );
\copy omnicorp.HsapDv FROM 'omnicorp_final/HsapDv' DELIMITER E'\t' CSV
CREATE INDEX ON omnicorp.HsapDv (pubmedid);
CREATE INDEX ON omnicorp.HsapDv (curie);
CREATE TABLE omnicorp.MONDO ( pubmedid int, curie varchar(255) );
\copy omnicorp.MONDO FROM 'omnicorp_final/MONDO' DELIMITER E'\t' CSV
CREATE INDEX ON omnicorp.MONDO (pubmedid);
CREATE INDEX ON omnicorp.MONDO (curie);
CREATE TABLE omnicorp.NCBIGene ( pubmedid int, curie varchar(255) );
\copy omnicorp.NCBIGene FROM 'omnicorp_final/NCBIGene' DELIMITER E'\t' CSV
CREATE INDEX ON omnicorp.NCBIGene (pubmedid);
CREATE INDEX ON omnicorp.NCBIGene (curie);
CREATE TABLE omnicorp.NCBITaxon ( pubmedid int, curie varchar(255) );
\copy omnicorp.NCBITaxon FROM 'omnicorp_final/NCBITaxon' DELIMITER E'\t' CSV
CREATE INDEX ON omnicorp.NCBITaxon (pubmedid);
CREATE INDEX ON omnicorp.NCBITaxon (curie);
CREATE TABLE omnicorp.PO ( pubmedid int, curie varchar(255) );
\copy omnicorp.PO FROM 'omnicorp_final/PO' DELIMITER E'\t' CSV
CREATE INDEX ON omnicorp.PO (pubmedid);
CREATE INDEX ON omnicorp.PO (curie);
CREATE TABLE omnicorp.UBERON ( pubmedid int, curie varchar(255) );
\copy omnicorp.UBERON FROM 'omnicorp_final/UBERON' DELIMITER E'\t' CSV
CREATE INDEX ON omnicorp.UBERON (pubmedid);
CREATE INDEX ON omnicorp.UBERON (curie);
