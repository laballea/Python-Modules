import sys


def main(args):
    if (len(args) == 1):
        print("Usage: enter arguments.")
    else:
        print(' '.join(args[1:]).swapcase()[::-1])


main(sys.argv)
