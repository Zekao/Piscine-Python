import pandas as pd

def how_many_medals(df, name):
    assert (isinstance(df, pd.DataFrame)), 'Parameter must be a dataframe'
    assert (isinstance(name, str)), 'name must be a string'

    df = df[df.Medal.notnull()]
    new_df = df.loc[df['Name'] == name]
    new_df = new_df.groupby(['Year', 'Medal']).size()
    new_df = new_df.to_frame()

    # sort new_df by year descending
    new_df = new_df.sort_values(by=['Year'], ascending=True)
    dict_medals = [ ]
    for year in new_df.index.levels[0]:
        dict_medals.append({'Year': year, 'Gold': 0, 'Silver': 0, 'Bronze': 0})
        for medal in new_df.index.levels[1]:
            if (year, medal) in new_df.index:
                dict_medals[-1][medal] = new_df.loc[(year, medal)][0]

    return dict_medals