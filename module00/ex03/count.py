from string import punctuation

def text_analyzer (*str) -> str:
    """ 
        text_analyzer if a function that will take a string in parameter
        and return how many lowercases, uppercases, spaces and punctuations 
        characters are present on it.
        there is 2 differents ways to use it:
            - text_analyzer() -> it will wait an input 
            - text_analyzer("your input")
    """
    if (len(str) > 1):
        assert False, "ERROR: wrong number of arguments."
    elif (len(str) == 0):
        main()
    upper = 0
    lower = 0
    punctuation = 0
    spaces = 0
    numbers = 0
    if (len(str) != 0):
        str = str[0]
        for char in str:
            if (char.isupper()):
                upper += 1
            elif (char.islower()):
                lower += 1
            elif (char.isspace()):
                spaces += 1
            elif (char.isdigit()):
                numbers += 1
        punctuation = len(str) - (upper + lower + spaces) - numbers
        aff_content(punctuation, upper, lower, spaces, str)

def aff_content(punctuation, upper, lower, spaces, str):
    print("The text contains ", len(str), " characters:")
    print("- ", upper, " upper letters")
    print("- ", lower, " lower letters")
    print("- ", punctuation, " punctuation marks")
    print("- ", spaces, " spaces")

def main(): 
    text = input("What is the test to analyse?\n")
    text_analyzer(text)

if __name__=="__main__":
    main()