looper = True
operationList = ["Addition", "Subtraction", "Multiplication",
"Division", "Modulo", "Raising to a power", "Square root", "Logarithm", "Sine",
"Cosine", "Tangent"]

while looper:
    print("Choose the math operation or type EXIT:")
    print()
    for element in operationList:
        print(str(operationList.index(element)) +" - "+str(element))
    print()
    userChoice = input()
    if userChoice.upper() =="EXIT":
        looper = False

