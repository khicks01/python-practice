input_1 = input("Enter the first number: ")
input_2 = input("Enter the second number: ")
try:
    result = float(input_1) + float(input_2)
    if type(result) == float:
        print(result)
except:
    print("You entered non-numbers, try again")