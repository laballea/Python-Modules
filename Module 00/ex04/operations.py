import sys


def main(args):
    """
        A program that takes two integers A and B as arguments and prints the result
        of the following operations: Sum, Difference, Product, Quotient, Remainder.
    """
    if (len(args) == 1):
        print("Usage: enter two integer as arguments.")
        return
    if (len(args) != 3):
        print("Usage: enter only two arguments.")
        return
    elif (args[1].isdigit() == False or args[2].isdigit() == False):
        print("Usage: arguments must be integer.")
        return
    st = int(args[1])
    nd = int(args[2])

    sum = str(st + nd)
    diff = str(st - nd)
    prod = str(st * nd)
    quot = str(("ERROR (division by zero)" if nd == 0 else st / nd ))
    mod = str(("ERROR (modulo by zero)" if nd == 0 else st % nd ))

    print("Sum:         " + sum)
    print("Difference:  " + diff)
    print("Product:     " + prod)
    print("Quotient:    " + quot)
    print("Remainder:   " + mod)

main(sys.argv)