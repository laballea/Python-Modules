import sys
import random


def main(args):
    print("This is an interactive guessing game!\n\
            You have to enter a number between 1 and 99 to find out the secret number.\n\
            Type 'exit' to end the game. \nGood luck!")
    answer = random.randrange(0, 100)
    attempt = 0
    while True:
        value = input("What's your guess between 1 and 99 ?\n>>")
        if (value == "exit"):
            break
        if (not value.isdigit()):
            print("Not a digit.")
            continue
        if (int(value) > 99 or int(value) < 0):
            print("Value not in range.")
            continue
        attempt += 1
        if (int(value) == 42):
            print("The answer to the ultimate question of life, the universe and everything is 42.")
        if (int(value) > answer):
            print("Too hight !")
        elif (int(value) < answer):
            print("Too low !")
        else:
            if (attempt == 1):
                print("Congratulations! You got it on your first try !")
            else:
                print("Congratulations, you've got it!\nYou won in {} attempt{} !".format(
                    attempt,
                    "s" if attempt > 0 else ""
                ))
            break
    print("Goodbye !")


main(sys.argv)
