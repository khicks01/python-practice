looper = True
operationList = ["Addition", "Subtraction", "Multiplication",
"Division", "Modulo", "Raising to a power", "Square root", "Logarithm", "Sine",
"Cosine", "Tangent"]

def twoNumberChooser():
    x = input("Choose the first number: ")
    print()
    y = input("Choose the second number: ")
    returnTuple = (float(x),float(y))
    return returnTuple
 
def sum_x_y(numberTuple, reverseFlag = False):
    if reverseFlag:
        return (numberTuple[0]+numberTuple[1]*-1)
    else:
        return (numberTuple[0]+numberTuple[1])
def mult_x_y(numberTuple, inverseFlag = False):
    if inverseFlag:
        if(numberTuple[1]==0):
            print("You cannot divide by zero")
        else:
            return (numberTuple[0]/numberTuple[1])
    else:
        return (numberTuple[0]*numberTuple[1])

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
    elif (userChoice) =="2":
        numbers = twoNumberChooser()
        print()
        print("The result is: "+str(mult_x_y(numbers)))
        print()
    elif (userChoice) =="3":
        numbers = twoNumberChooser()
        print()
        print("The result is: "+str(mult_x_y(numbers, inverseFlag= True)))
        print()