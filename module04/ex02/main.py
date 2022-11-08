from ProportionBySport import proportion_by_sport
from ex03.FileLoader import FileLoader


def main():
    loader = FileLoader()
    data = loader.load('../data/athlete_events.csv')
    proportion_by_sport(data, 1964, 'Biathlon', 'M')


if __name__ == "__main__":
    main()