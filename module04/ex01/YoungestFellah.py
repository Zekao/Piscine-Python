import pandas as pd

def youngest_fellah(df, year):
    assert (isinstance(df, pd.DataFrame)), 'Parameter must be a dataframe'
    assert (isinstance(year, int)), 'Year must be an integer'
    new_df = df.loc[df['Year'] == year]
    youngest_girl = new_df.loc[df['Sex'] == 'F']
    youngest_boy = new_df.loc[df['Sex'] == 'M']

    print("'f': {}, 'm': {}".format(youngest_girl['Age'].min(), youngest_boy['Age'].min()))