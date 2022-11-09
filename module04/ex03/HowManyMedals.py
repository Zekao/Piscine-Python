import pandas as pd

def how_many_medals(df, name):
    assert (isinstance(df, pd.DataFrame)), 'Parameter must be a dataframe'
    assert (isinstance(name, str)), 'name must be a string'

    df = df[df.Medal.notnull()]
    new_df = df.loc[df['Name'] == name]
    new_df = new_df.groupby(['Year', 'Medal']).size()
    new_df = new_df.rename(index={'Bronze': 'B', 'Silver': 'S', 'Gold': 'G'})
    new_df = new_df.unstack(level=-1).fillna(0).astype(int)
    new_df = new_df.to_dict(orient='index')


    for year in new_df:
        new_df[year] = {k: new_df[year][k] for k in ['G', 'S', 'B']}
    return new_df