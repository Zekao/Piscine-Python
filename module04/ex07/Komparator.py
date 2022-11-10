import pandas as pd
import matplotlib.pyplot as plt

class Komparator:
    def __init__(self, data):
        assert (isinstance(data, pd.DataFrame)), 'data must be a dataframe'
        self.data = data.dropna()

    def compare_box_plots(self, categorical_var, numerical_var):
        self.data.boxplot(column=[numerical_var], by=categorical_var)
        plt.show()

    def compare_histograms(self, categorical_var, numerical_var):
        self.data.hist(column=numerical_var, by=categorical_var)
        plt.show()

    def density_plot(self, categorical_var, numerical_var):
        self.data.groupby(categorical_var)[numerical_var].plot(kind='density')
        plt.show()