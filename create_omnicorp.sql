CREATE TABLE omnicorp.MESH ( pubmedid varchar(255), curie varchar(255) );
\copy omnicorp.MESH FROM 'omnicorp_final/xaa' DELIMITER E'\t' CSV
\copy omnicorp.MESH FROM 'omnicorp_final/xab' DELIMITER E'\t' CSV
\copy omnicorp.MESH FROM 'omnicorp_final/xac' DELIMITER E'\t' CSV
CREATE INDEX ON omnicorp.MESH (pubmedid);
CREATE INDEX ON omnicorp.MESH (curie);

