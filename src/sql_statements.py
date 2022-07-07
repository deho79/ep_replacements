select_libelle_query = """
SELECT LIB_LIBELLE, c.CPT_ID
FROM bce.libelle l
join bce.concept c
on l.CPT_ID  = c.CPT_ID and LAN_ID = 5;
"""