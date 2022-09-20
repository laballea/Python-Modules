import sys


def main(args):
    if (len(args) == 1):
        print("Usage: enter arguments.")
    else:
        string = concatenateArgs(args)
        print(' '.join(args[1:]).swapcase()[::-1])


main(sys.argv)
