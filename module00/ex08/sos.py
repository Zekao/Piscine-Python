import sys

alphabet = dict(A='.-', B='-...', C='-.-.', D='-..', E='.', F='..-.', G='--.',
                H='....', I='..', J='.---', K='-.-', L='.-..', M='--', N='-.',
                O='---', P='.--.', Q='--.-', R='.-.', S='...', T='-', U='..-',
                V='...-', W='.--', X='-..-', Y='-.--', Z='--..')
alphabet.update({
    '0': '-----', '1': '.----',
    '2': '..---', '3': '...--',
    '4': '....-', '5': '.....',
    '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
})

def encode(str): 
    i = 0
    for letter in str:
        i += 1
        if (letter.isalnum() == False and letter != ' '):
            assert False, "ERROR"
        elif (letter != " "):
            print(alphabet[letter], end=" ")

def interpret(tab):
    encode (tab)

def checkParam():
    ret = ""
    i = 0
    for arg in sys.argv:
        if i == 0:
            i += 1
            continue
        arg = arg.strip(" ")
        ret += arg.upper() + " "
    ret = ret.split(" ")
    i = 0
    for str in ret:
        i += 1
        interpret(str)
        if (i < len(ret) - 1):
            print('/', end=" ")


def main():
    checkParam()

if __name__=="__main__":
    main()