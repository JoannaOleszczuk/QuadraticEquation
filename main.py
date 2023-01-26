import sys

def QuadraticEquation():
    print("Hello :) Welcome in program to solve the quadratic equation ax^2 + bx + c = 0 "
          "The n")

    try:
        AskUserA = int(input("Type 'a' coefficient: "))
        AskUserB = int(input("Type 'b' coefficient: "))
        AskUserC = int(input("Type 'c' coefficient: "))

        if AskUserA <0 or AskUserB <0 or AskUserC<0:
            print("Coefficients a,b and c must be at least equal 0!")
            return
        print("Values are valid")

    except ValueError as e:
        print("Incorrect type of value. Value must be integer. See the error", e)
    except:
        print("Error occurs. See comment: ", sys.exc_info())

QuadraticEquation()