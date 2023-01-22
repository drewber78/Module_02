"""
Name: Drew Cochran
Date: 22JAN2023
Description: Basic Math Script. Program asks for user's input of two numbers, then outputs the sum, difference, product,
and quotient of the two inputted numbers. Input can be whole numbers, integers, and floats, positive and negative. Output is a
float with one decimal point.
Changelog:

"""

# defining the function
def BasicMathScript():

    # defining the variables
    userinputnumber_1 = 0.0
    userinputnumber_2 = 0.0
    outputvariable = 0.0

    # defining the inputs from user
    userinputnumber_1 = float(input("Enter a first number: "))
    userinputnumber_2 = float(input("Enter a second number: "))

    # Calculating the sum
    outputvariable = userinputnumber_1 + userinputnumber_2
    print("The sum of", userinputnumber_1, "and", userinputnumber_2, "is: ", outputvariable)

    # Calculating the difference
    outputvariable = userinputnumber_1 - userinputnumber_2
    print("The difference of", userinputnumber_1, "and", userinputnumber_2, "is: ", outputvariable)

    # Calculating the product
    outputvariable = userinputnumber_1 * userinputnumber_2
    print("The product of", userinputnumber_1, "and", userinputnumber_2, "is: ", outputvariable)

    # Calculating the quotient
    if userinputnumber_2 == 0:
        print("Quotient cannot be found as you cannot divide by zero.")
    else:
        outputvariable = userinputnumber_1 / userinputnumber_2
        print("The quotient of", userinputnumber_1, "and", userinputnumber_2, "is: ", outputvariable)

BasicMathScript()