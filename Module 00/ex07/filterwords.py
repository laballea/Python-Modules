import sys
import string


def main(args):
    if (len(args) != 3):
        print("ERROR")
        return
    if (not args[2].isdigit()):
        print("ERROR")
        return
    print([
        x.translate(str.maketrans('', '', string.punctuation))
        for x in sys.argv[1].split(' ') if len(x.translate(str.maketrans('', '', string.punctuation))) > int(args[2])
    ])


main(sys.argv)
