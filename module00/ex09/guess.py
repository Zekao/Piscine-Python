from random import random
import sys
import random
def randGame():
    res = random.randint(1, 99)
    val = 0
    count = 0
    print('This is an interactive guessing game!\nYou have to enter a number between 1 and 99 to find out the secret number.\nGood luck!\n')
    while (val != res):
        count += 1
        val = input("What's your guess between 1 and 99?\n>>")
        if (val == "exit"):
            print("Goodbye!")
            return
        if (val.isdigit() == False):
            print("That's not a number.")
            continue
        val = int(val)
        if (val < res):
            print('Too low!')
        elif (val > res):
            print('Too high!')    
    if (count == 1 and val == 42):
        print('The answer to the ultimate question of life, the universe and everything is 42.\nCongratulations! You got it on your first try!')
    else:
        print('You won in', count, 'attemps!')
def main():
    randGame()

if __name__=="__main__":
    main()