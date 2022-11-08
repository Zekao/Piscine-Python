from YoungestFellah import youngest_fellah
from ex03.FileLoader import FileLoader


def main():
    loader = FileLoader()
    data = loader.load('../data/athlete_events.csv')
    youngest_fellah(data, 2004)


if __name__ == "__main__":
    main()