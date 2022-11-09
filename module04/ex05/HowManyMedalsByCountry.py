import pandas as pd

def how_many_medals_by_country(df, name):
    assert isinstance(df, pd.DataFrame), 'df is not a dataframe'
    assert isinstance(name, str), 'name must be a string'

    team_sports = [
            "Basketball",
            "Football",
            "Tug-Of-War",
            "Badminton",
            "Sailing",
            "Handball",
            "Water Polo",
            "Hockey",
            "Rowing",
            "Bobsleigh",
            "Softball",
            "Volleyball",
            "Synchronized Swimming",
            "Baseball",
            "Rugby Sevens",
            "Rugby",
            "Lacrosse",
            "Polo",
    ]

    team_df = df[df["Sport"].isin(team_sports)]
    team_df = team_df[team_df["Team"] == name]
    team_df = team_df.dropna(subset=["Medal"])
    team_df = team_df.drop_duplicates(subset=['Year', 'Medal', 'Event'])

    solo_df = df[~df["Sport"].isin(team_sports)]
    solo_df = solo_df[solo_df["Team"] == name]
    solo_df = solo_df.dropna(subset=["Medal"])

    new_df = pd.concat([team_df, solo_df]).groupby(['Year', 'Medal']).size()
    new_df = new_df.rename(index = {'Gold': 'G', 'Silver': 'S', 'Bronze': 'B'})
    new_df = new_df.unstack(level=-1).to_dict(orient='index')


    for year in new_df:
        new_df[year] = {k: new_df[year][k] for k in ['G', 'S', 'B']}

    return new_df