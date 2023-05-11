def getKeys():
    dico={}
    with open("data/keys.txt", "r") as file:
        for k in file.readlines():
            a=k.rstrip().split(";")
            dico[int(a[1])] = a[0]
    return dico