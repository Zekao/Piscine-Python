from FileLoader import FileLoader
from  Komparator import Komparator

def main():
    df = FileLoader()
    df = df.load("../data/athlete_events.csv")

    komp = Komparator(df)
    category = 'Medal'
    category1 = 'Sex'
    numerical = 'Age'
    numerical1 = 'Height'
    numerical2= 'Weight'

    komp.compare_box_plots(category, numerical)
    komp.compare_histograms(category1, numerical1)
    komp.density_plot(category1, numerical2)

if __name__ == "__main__": 
    main()
