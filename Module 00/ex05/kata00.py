kata = (19,42,21)

def display(var):
    string = ""
    for el in var:
        string += str(el) + ", "
    print("The " + str(len(var)) + " numbers are: " + string[:-2])

display(kata)