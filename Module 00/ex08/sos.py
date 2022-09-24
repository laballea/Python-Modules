import sys

morse = {
            "A":".-",
            "B":"-...",
            "C":"-.-.",
            "D":"-..",
            "E":".",
            "F":"..-.",
            "G":"--.",
            "H":"....",
            "I":"..",
            "J":".---",
            "K":"-.-",
            "L":".-..",
            "M":"--",
            "N":"-.",
            "O":"---",
            "P":".--.",
            "Q":"--.-",
            "R":".-.",
            "S":"...",
            "T":"-",
            "U":"..-",
            "V":"...-",
            "W":".--",
            "X":"-..-",
            "Y":"-.--",
            "Z":"--..",
            "0":"-----",
            "1":".----",
            "2":"..---",
            "3":"...--",
            "4":"....-",
            "5":".....",
            "6":"-....",
            "7":"--...",
            "8":"---..",
            "9":"----.",
            " ": "/"
        }


def main(args):
    if (len(args) == 1):
        print("Usage: enter arguments.")
        return
    
    string = ' '.join(args[1:]).upper()
    if (all(chr.isalpha() or chr.isspace() or chr.isdigit() for chr in string) == False):
        print("Error.")
        return
    print(' '.join([morse[c] for c in string]))

main(sys.argv)