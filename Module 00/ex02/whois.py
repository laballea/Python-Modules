import sys


def main(args):
    if (len(args) != 2):
        print("Usage: enter one arguments.")
    elif (args[1].isdigit() == False):
        print("Usage: arguments must be integer.")
    elif (int(args[1]) == 0):
        print("I'm Zero.")
    elif (int(args[1]) % 2 == 1):
        print("I'm Odd.")
    else:
        print("I'm Even.")


main(sys.argv)
