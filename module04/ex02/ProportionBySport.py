import pandas as pd

def proportion_by_sport(df, year, sport, gender):
    assert (isinstance(df, pd.DataFrame)), 'Parameter must be a dataframe'
    assert (isinstance(year, int)), 'Year must be an integer'
    assert (isinstance(sport, str)), 'sport must be a string'
    assert (isinstance(gender, str)), 'gender must be a string'

    for_sport = df.loc[df['Year'] == year]
    current_gender = for_sport.loc[df['Sex'] == gender]
    for_sport = current_gender[df['Sport'] == sport]
    print(for_sport)
    print(current_gender)
    print ((for_sport.shape[0] / current_gender.shape[0]) * 100)
