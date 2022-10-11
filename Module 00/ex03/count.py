import sys


def text_analyzer(*args):
    """
        This function counts the number of upper characters, lower characters,
        punctuation and spaces in a given text.
    """

    if (len(args) > 1):
        print("Usage: enter only one arguments.")
        return
    if (len(args) < 1):
        print("What is the text to analyze ?")
        arg = input(">>")
    else:
        arg = args[0]
        if (not isinstance(arg, str) or arg.isdigit()):
            print("Usage: arguments is not a string.")
            return
        if (arg is None):
            print("What is the text to analyze ?")
            arg = input(">>")

    while (len(arg) == 0):
        print("What is the text to analyze ?")
        arg = input(">>")
        if (not isinstance(arg, str) or arg.isdigit()):
            print("Usage: arguments is not a string.")
            return

    countLower = 0
    countUpper = 0
    countSpace = 0
    countMark = 0
    for char in arg:
        if (char.islower()):
            countLower += 1
        elif (char.isupper()):
            countUpper += 1
        elif (char == " "):
            countSpace += 1
        elif char in ('!', ",", "\'", ";", "\"", ".", "-", "?"):
            countMark += 1
    print("The text contains {} character{}".format(
        str(len(arg)),
        ("s." if len(arg) > 1 else ".")
    ))
    print("- {} upper letter{}".format(
        str(countUpper),
        ("s." if countUpper > 1 else ".")
    ))
    print("- {} lower letter{}".format(
        str(countLower),
        ("s." if countLower > 1 else ".")
    ))
    print("- {} punctuation mark{}".format(
        str(countMark),
        ("s." if countMark > 1 else ".")
    ))
    print("- {} space{}".format(
        str(countSpace),
        ("s." if countSpace > 1 else ".")
    ))


if __name__ == '__main__':
    if (len(sys.argv) > 2):
        print("Usage: enter only one arguments.")
    elif (len(sys.argv) < 2):
        text_analyzer()
    else:
        text_analyzer(sys.argv[1])
