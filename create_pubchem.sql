CREATE TABLE omnicorp.PUBCHEM_COMPOUND ( pubmedid varchar(255), curie varchar(255) );
\copy omnicorp.PUBCHEM_COMPOUND FROM 'omnicorp_final/PUBCHEM.COMPOUND' DELIMITER E'\t' CSV
CREATE INDEX ON omnicorp.PUBCHEM_COMPOUND (pubmedid);
CREATE INDEX ON omnicorp.PUBCHEM_COMPOUND (curie);

