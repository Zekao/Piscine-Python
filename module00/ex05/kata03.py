phrase = "The right format"

size=0
def main():
    size = len(phrase)
    while True:
        print('-', end="")
        if (size >= 40):
            print(phrase)
            break
        size += 1

if __name__=="__main__":
    main()