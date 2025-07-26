# day4 : exception handling
'''an exception is an error that happens during program execution, which stops the normal flow of the
program unless handled.'''
from webbrowser import Elinks

from numpy.random import choice


# Basic try/except
'''try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Invalid input! Please enter a number.")'''

# catching multiple exceptions
'''try:
    a = int(input("Enter a numerator: "))
    b = int(input("Enter a denominator: "))
    result = a/b
    print("The result is: ", result)
except ZeroDivisionError:
    print("Error found! Can't divide by zero")
except ValueError:
    print("Invalid input! Please enter a valid number.")'''
#
# # Else and finally
'''try:
    n = int(input("Enter a number: "))
except ValueError:
    print("This is not a number!")
else:
    print("Good! Your entered number is:", n)
finally:
    print(f"Execution finished with entered number {n}")'''

# Custom Exceptions
'''class NegativeNumberError(Exception):
    pass

try:
    x = int(input("Enter a number: "))
    if x<0:
        raise NegativeNumberError("Negative numbers are not allowed!")
    print("You entered:", x)
except NegativeNumberError as e:
    print(e)'''

# Mini Project - Safe calculator
def add(a,b):
    return a + b
def subtract(a,b):
    return a-b
def multiply (a,b):
    return a*b
def divide(a,b):
    return a/b
def calculator():
    print("Mini calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

class NegativeNumberError(Exception):
    pass

while True:
    calculator()

    try:
        choice = input("Please enter your choice (1-4): ")

        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if a<0 or b<0:
            raise NegativeNumberError("Negative Numbers are not allowed!")
        print(f"Your entered numbers are {a} and {b}")

        if choice == '1':
            print("Add Result:", add(a,b))
        elif choice == '2':
            print("Subtract Result:", subtract(a,b))
        elif choice == '3':
            print("Multiply Result:", multiply(a,b))
        elif choice == '4':
            if b == 0:
                raise ZeroDivisionError("Error: Can't divide by zero")
            else:
                print("Divide Result:", divide(a,b))
        else:
            print("Invalid choice")

        choice_for_repeat = input("Do you want to try again? (y/n): ")
        if choice_for_repeat.lower() != 'y':
            break

    except ValueError:
        print("Your entered values are not numbers")
    except NegativeNumberError as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)