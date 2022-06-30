import datetime
t = (3,30,2019,9,25)

def main():
    
    year = '{:02d}'.format(t[2])
    month = '{:02d}'.format(t[3])
    day = '{:02d}'.format(t[4])
    hour = '{:02d}'.format(t[1])
    minute = '{:02d}'.format(t[0])
    time = '{}/{}/{} {}:{}'.format(month, day, year, minute, hour)
    print(time)

if __name__=="__main__":
    main()