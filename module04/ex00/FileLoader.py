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
        if (n > 0):
            print(df.head(n))
        else:
            print(df.tail(abs(n)))
        return

if __name__ == "__main__":
    fl = FileLoader()
    df = fl.load('athlete_events.csv')
    fl.display(df, -12)
