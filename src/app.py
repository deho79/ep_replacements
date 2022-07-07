import pandas as pd

from bce_connect import connect_to_bce
from constants import CHUNKSIZE
from sql_statements import select_libelle_query


def main():
    engine = connect_to_bce()

    # since chunksize is specified a concat is necessary
    chunks = []
    for chunk in pd.read_sql_query(select_libelle_query, engine, coerce_float=True, chunksize=CHUNKSIZE):
        chunks.append(chunk)
    df = pd.concat(list(chunks))


if __name__ == "__main__":
    main()