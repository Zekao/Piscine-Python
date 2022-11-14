import pandas as pd

def how_many_medals(df, name):
    assert (isinstance(df, pd.DataFrame)), 'Parameter must be a dataframe'
    assert (isinstance(name, str)), 'name must be a string
    
    new_df = df[df['Name'] == name]
    new_df.sort_values(by=['Year'])

    ret_dict = dict(enumerate(new_df.Year.unique()))
    ret_dict = {v: k for k, v in ret_dict.items()}

    for key, _  in ret_dict.items() :
        ret_dict[key] = {
        'G' : sum((new_df.Year == key) & (new_df.Medal == 'Gold')),
        'S':  sum((new_df.Year == key) & (new_df.Medal == 'Silver')),
        'B':  sum((new_df.Year == key) & (new_df.Medal == 'Bronze'))
        }

    return ret_dict
