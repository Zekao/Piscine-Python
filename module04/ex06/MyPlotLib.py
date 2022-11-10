import matplotlib.pyplot as plt  
import pandas as pd

class MyPlotLib():
    '''
        a
    '''
    def histogram(self, data, features):
        assert (isinstance(data, pd.DataFrame)), 'data must be a dataframe'
        assert (isinstance(features, list)), 'features must be a list'
        data[features].hist()
        plt.show()

    def density(self, data, features):
        assert (isinstance(data, pd.DataFrame)), 'data must be a dataframe'
        assert (isinstance(features, list)), 'features must be a list'
        data[features].plot.density()
        plt.show()

    def pair_plot(self, data, features):
        assert (isinstance(data, pd.DataFrame)), 'data must be a dataframe'
        assert (isinstance(features, list)), 'features must be a list'
        pd.plotting.scatter_matrix(data[features])
        plt.show()

    def box_plot(self, data, features):
        assert (isinstance(data, pd.DataFrame)), 'data must be a dataframe'
        assert (isinstance(features, list)), 'features must be a list'
        data.boxplot(features)
        plt.show()
