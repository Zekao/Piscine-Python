import pandas as pd

class FileLoader():
    def __init__(self):
        return

    def load(self, path):
        try:
            open(path, 'r')
        except Exception as e:
            print(e)
            return
        df = pd.read_csv(path)
        print('Loading dataset of dimensions {} x {}' .format(df.shape[0], df.shape[1]))
        return (df) 


    def display(self, df, n):
        assert isinstance(df, pd.DataFrame), 'df is not a dataframe'
        assert n >= 0, 'n must be a positive value'
        print(df.head(n))
        return