import math
import sys


def quadratic_equation():
    print("Hello :) Welcome in program to solve the quadratic equation ax^2 + bx + c = 0 ")

    try:
        AskUserA = int(input("Type 'a' coefficient: "))
        AskUserB = int(input("Type 'b' coefficient: "))
        AskUserC = int(input("Type 'c' coefficient: "))

        if AskUserA <= 0 or AskUserB <0 or AskUserC <0:
            print("Coefficient a must be greater than 0! Coefficients b and c must be at least equal to zero!")
            return
        print("Values are valid")

        delta = AskUserB**2 - 4*AskUserA*AskUserC
        print("Delta: ", delta)

        if delta > 0:
            x1 = (-AskUserB - math.sqrt(delta))/2*AskUserA
            x2 = (-AskUserB + math.sqrt(delta))/2*AskUserA
            print("Two solutions to the equation: %f and %f " % (x1, x2))

        elif delta == 0:
            x = -AskUserB/2*AskUserA
            print("One solution to the equation: %f " % x)

        elif delta < 0:
            print("There is no real solution to the equation!")

    except ValueError as e:
        print("Incorrect type of value. Value must be integer. See the error", e)
    except:
        print("Error occurs. See comment: ", sys.exc_info())

quadratic_equation()
