t = ( 0, 4, 132.42222, 10000, 12345.67)


def main():
    mod = '{:02d}'.format(t[0])
    ex = '{:02d}'.format(t[1])
    val1 = '{:.2f}'.format(t[2])
    val2 = '{:.2e}'.format(t[3])
    val3 = '{:.2e}'.format(t[4])
    res = 'module_{}, ex_{} : {}, {}, {}'.format(mod, ex, val1, val2, val3)
    print(res)

if __name__=="__main__":
    main()