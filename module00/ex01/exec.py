import sys
# remove name of script from arguments
sys.argv.pop(0)
# create a string that will contain the arguments
str = ""
for args in sys.argv:
    for char in args:
        if (char.isupper()):
                str += char.lower()
        else:
                str += char.upper()
# str[::-1] reverse the string
print(str[::-1])

