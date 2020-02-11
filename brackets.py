text = input("Enter the bracket : ")
#text = text.replace(" ", "")
theLenght = len(text)
openbracket = 0
closedbracket = 0

if (text[0] == ")") or (text[theLenght - 1] == "("):
    print(False)
else:
    #for char in text
    for i in range(0, theLenght):
        if (text[i] == "("):
            openbracket += 1
        elif (text[i] == ")"):
            closedbracket += 1
    if openbracket == closedbracket:
            print(True)
    else:
            print(False)