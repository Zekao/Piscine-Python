from FileLoader import FileLoader
from HowManyMedalsByCountry import how_many_medals_by_country

def main():
    loader = FileLoader()
    data = loader.load('../data/athlete_events.csv')
    print (how_many_medals_by_country(data, 'United States'))

if __name__ == "__main__":
    main()