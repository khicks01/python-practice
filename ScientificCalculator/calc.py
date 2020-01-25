looper = True
operationList = ["Addition", "Subtraction", "Multiplication",
"Division", "Modulo", "Raising to a power", "Square root", "Logarithm", "Sine",
"Cosine", "Tangent"]

def twoNumberChooser():
    x = input("Choose the first number: ")
    print()
    y = input("Choose the second number: ")
    returnTuple = (int(x),int(y))
    return returnTuple
 
def sum_x_y(numberTuple, reverseFlag = False):
    if reverseFlag:
        return (numberTuple[0]+numberTuple[1]*-1)
    else:
        return (numberTuple[0]+numberTuple[1])

while looper:
    print("Choose the math operation or type EXIT:")
    print()
    for element in operationList:
        print(str(operationList.index(element)) +" - "+str(element))
    print()
    userChoice = input()
    print()
    if userChoice.upper() =="EXIT":
        looper = False
    elif (userChoice)=="0":
        numbers = twoNumberChooser()
        print()
        print("The result is: "+str(sum_x_y(numbers)))
        print()
    elif (userChoice)=="1":
        numbers = twoNumberChooser()
        print()
        print("The result is: "+str(sum_x_y(numbers, reverseFlag = True)))
        print()