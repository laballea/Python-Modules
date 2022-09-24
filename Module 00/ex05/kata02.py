kata = (2019, 9, 25, 3, 30)

def display():
    print(("0" if kata[1] < 10 else "") + str(kata[1]) + "/" + ("0" if kata[2] < 10 else "") + str(kata[2]) + "/" + str(kata[0]) + " " + ("0" if kata[3] < 10 else "") + str(kata[3]) + ":" + ("0" if kata[4] < 10 else "") + str(kata[4]))

display()