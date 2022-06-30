from pickle import FALSE
import sys

def check():
    if (len(sys.argv) == 0):
        print('Usage: python operations.py <number1> <number2>')
        exit
    elif (len(sys.argv) < 3):
        assert False, "InputError: not enough arguments"
    elif (len(sys.argv) > 3):
        assert False, "InputError: too many arguments"
    if (((sys.argv[1].isdecimal())  == False) or (sys.argv[2].isdecimal()) == False):
        assert False, "InputError: only numbers"
    operations()
    # else:

def operations():
    print('Sum: ', float(sys.argv[1]) + float(sys.argv[2]))
    print('Difference: ', float(sys.argv[1]) - float(sys.argv[2]))
    print('Product: ', float(sys.argv[1]) * float(sys.argv[2]))
    print('Quotient: ', float(sys.argv[1]) / float(sys.argv[2]))
    print('Remainder: ', float(sys.argv[1]) % float(sys.argv[2]))

def main(): 
    check()

if __name__=="__main__":
    main()