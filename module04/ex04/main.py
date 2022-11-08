from FileLoader import FileLoader
from SpatioTemporalData import SpatioTemporelData


def main():
    loader = FileLoader()
    data = loader.load('../data/athlete_events.csv')
    sp = SpatioTemporelData(data)
    print(sp.when('Athina'))
    print(sp.where(2004))

if __name__ == "__main__":
    main()