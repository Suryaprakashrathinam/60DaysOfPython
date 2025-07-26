'''functions - reusable block of code that perform a specific task
define it once - use it anywhere
Uses:
1. avoid code repitition
2. improve readability
3. make code modular and organised
4. easy to debug and maintain'''
from numpy.random import chisquare
from reportlab.lib.utils import isNonPrimitiveInstance


# # Define a basic function and call it
# def greet():
#     print("Hello world, Welcome to day 3!")
# greet()
#
# # function with one parameter
# def greet_user(name):
#     print(f"Hi {name}, good to see you")
# greet_user("Surya")
#
# # Function with multiple parameters and return value
# def add(a,b):
#     return a+b
# result = add(5,5)
# print(result)
#
# # Use default and keyword arguments
# def welcome(name="Guest"):
#     print(f"Welcome, {name}")
# welcome() #uses default
# welcome("Abinaya") #positional
# welcome(name="Surya")
#
# # function calling another function
# def multiply(x,y):
#     return x*y
# print(multiply(5,6))
# def square(n):
#     return multiply(n,n)
# print(square(6))
#
# # Task
# # Create a function Accept a list of numbers and returns the list of even numbers only
# def filter_even(numbers):
#     return [n for n in numbers if n%2==0]
# nums = [1,2,3,4,5,6,7,8,9,10]
# print(filter_even(nums)

# Build mini calculator using functions
# Step 1 : Define basic arithmetic functions
# def add(a,b):
#     return a+b
# def subtract(a,b):
#     return a-b
# def multiply (a,b):
#     return a*b
# def divide(a,b):
#     if b!=0 :
#         return a/b
#     else:
#         return "Error: Division by zero not allowed"
#
# # Step 2 : Add simple menu to call these functions
# def calculator():
#     print("Mini calculator")
#     print("1. Add")
#     print("2. Subtract")
#     print("3. Multiply")
#     print("4. Divide")
#
#     choice = input("Please enter your choice (1-4): ")
#
#     a = float(input("Enter first number: "))
#     b = float(input("Enter second number: "))
#
#     if choice == '1':
#         print("Add Result:", add(a,b))
#     elif choice == '2':
#         print("Subtract Result:", subtract(a,b))
#     elif choice == '3':
#         print("multiply Result:", multiply(a,b))
#     elif choice == '4':
#         print("Divide Result:", divide(a,b))
#     else:
#         print("Invalid choice")
#
# calculator()

'''Small anonymous function defined using lambda keyword. generally used for short operations where
full length function is not necessory.'''
add = lambda a,b: a+b
subtract = lambda a,b: a-b
multiply = lambda a,b: a*b
divide = lambda a,b: a/b if b!=0 else "Error"

print(add(5,84))
print(subtract(84,75))
print(multiply(54,654))
print(divide(564, 541))
print(divide(54, 0))
