import pandas as pd


def extractmetadata(metadata, filepath):

    with pd.read_csv(filepath , nrows=1) as pd:
        metadata['table_shape'] = pd.shape
        metadata['table_collumns'] = pd.columns

    return metadata