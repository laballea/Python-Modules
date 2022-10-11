kata = "The right format"


def display():
    res = kata.rjust(41, "-")
    print(res[0:41])


display()
