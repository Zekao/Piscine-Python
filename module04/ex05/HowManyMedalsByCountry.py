import pandas as pd

def how_many_medals_by_country(df, name):
    assert isinstance(df, pd.DataFrame), 'df is not a dataframe'
    assert isinstance(name, str), 'name must be a string'

    df_tmp = df.loc[df['Team'] == name]
    df_tmp = df_tmp[df_tmp['Medal'].notna()]
    # df_tmp = df_tmp.drop_duplicates(subset = ['Year', 'Sport'])

    new_df = df_tmp.groupby(['Year', 'Medal']).size()

    # return a list of dictionaries
    dict_medals = [ ]
    for year in new_df.index.levels[0]:
        dict_medals.append({'Year': year, 'Gold': 0, 'Silver': 0, 'Bronze': 0})
        for medal in new_df.index.levels[1]:
            print(medal, year)