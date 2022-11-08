import pandas as pd

class SpatioTemporelData():
    def __init__(self, df):
        assert isinstance(df, pd.DataFrame), 'df is not a dataframe'
        self.df = df


    def when(self, location):
        df_location = self.df.loc[self.df['City'] == location]
        df_years = df_location.drop_duplicates(subset = ["Year"])
        years = df_years['Year'].tolist()
        return years

    def where(self, date):
        df_date = self.df.loc[self.df['Year'] == date]
        df_location = df_date.drop_duplicates(subset = ["City"])
        city = df_location['City'].tolist()
        return city
