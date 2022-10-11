kata = (0, 4, 132.42222, 10000, 12345.67)


def display(var):
    print("module_{}{}, ex_{}{} : {:.2f}, {:.2e}, {:.2e}".format(
            "0" if kata[0] < 10 else "", kata[0],
            "0" if kata[1] < 10 else "", kata[1],
            kata[2],
            kata[3],
            kata[4]
        ))


display(kata)
