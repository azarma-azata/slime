def getKeys():
    dico={}
    with open("data/storedData/keys.txt", "r") as file:
        for k in file.readlines():
            a=k.rstrip().split(";")
            dico[int(a[1])] = a[0]
    return dico

def getTexts():
    dico={}
    with open("data/storedData/texts.csv", "r", encoding="utf-8") as file:
        for k in file.readlines():
            a=k.rstrip().split(";")
            dico[a[0]] = a[1:]
    return dico