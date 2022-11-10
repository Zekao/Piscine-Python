from FileLoader import FileLoader
from MyPlotLib import MyPlotLib


def main():
    loader = FileLoader()
    mpl = MyPlotLib()

    data = loader.load("../data/athlete_events.csv")
    x = ["Height", "Weight"]
    y = ["Weight", "Height"]
    mpl.histogram(data, x)
    mpl.density(data, y)
    mpl.pair_plot(data, y)
    mpl.box_plot(data, y)

if __name__ == "__main__":
    main()