kata = (19, 25)


def display(var):
    string = ""
    for el in var:
        string += str(el) + ", "
    print("The " + str(len(var)) + " numbers are: " + string[:-2])


display(kata)
