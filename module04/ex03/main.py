from FileLoader import FileLoader
from HowManyMedals import how_many_medals


def main():
    loader = FileLoader()
    data = loader.load('../data/athlete_events.csv')
    dict_ = how_many_medals(data, 'Kjetil Andr Aamodt')

    for row in dict_:
        print(row)

if __name__ == "__main__":
    main()