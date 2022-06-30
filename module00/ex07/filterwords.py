import sys
import string

def checkArgs():
    if len(sys.argv) != 3:
        assert False, "ERROR, wrong number of arguments"
    if sys.argv[2].isdecimal() == False:
        assert False, "ERROR, second argument must be a decimal value"
def filterwords():
    checkArgs()
    str = sys.argv[1]
    str = str.translate(str.maketrans('', '', string.punctuation))
    words = str.split()
    words_tmp = str.split()
    size = int(sys.argv[2]) 

    size_debug = 0
    for word in words:
        size_debug += 1
        if len(word) <= size:
            words_tmp.remove(word)
    print(words_tmp)

def main(): 
    filterwords()

if __name__=="__main__":
    main()