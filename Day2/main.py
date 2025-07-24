'''Day 2 : topics loops & comprehensions (2 powerful core concepts)

Loops - how to repeat tasks during
 1. for loop - iterate over a list, tupple, dictionery, set, string
 2. while loop - repeat while a condition is true
 3. break and continue - control flow inside the loops'''

# 1. Print each fruit in a list using for loop
# fruits = ["Banana", "Orange", "Apple", "Guava", "Grapes"]
# for fruit in fruits:
#     print(fruit)

# 2. use while loop to print numbers from 1 to 6
# i = 1
# while i<=6:
#     print(i)
#     i+=1

# 3. use break to stop loop when a result is found
# nums = [1,2,3,4,4,5,9,8,10]
# for n in nums:
#     if n==4:
#         break
#     print(n)

# use continue to skip the number
# nums = [1,2,3,4,4,5,9,8,10]
# for n in nums:
#     if n==4:
#         continue
#     print(n)

'''list comprehensions - cleaner and faster way to build list in one line'''
# 1. create a list of squares using for loop and list comprehension
# squares_loop = []
# for i in range (1,6):
#     squares_loop.append(i*i)
# squares_comp = [i*i for i in range (1,6)]
# print(squares_loop)
# print(squares_comp)

# 2. create a list of even numbers from 1 to 10
# evens = [x for x in range(1,11) if x%2==0]
# print(evens)

# 3. convert list of strings into uppercase
# fruits = ["Banana", "Orange", "Apple", "Guava", "Grapes"]
# upper_words = [w.upper() for w in fruits]
# '''here i have missed to add (). so instead of calling the function, it actually collecting function references
# to the upper method of each string. so we will get error like this "<built-in method upper of str object>"'''
# print(upper_words)

# Get a list of numbers from 1 to 20
# i = 1
# nums = []
# while i <=20:
#     nums.append(i)
#     i+=1
# print(nums)
# '''Note: here indentation and iterate calling function is important'''

# Filter only the multiples of 3 using list comprehension
# multiples = [x for x in range(0,21) if x%3==0]
# print(multiples)

# Use a for loop to print “Even” or “Odd” for each number in that list
for i in range(1,21):
    if i%2==0:
        print(f"{i} is Even")
    else:
        print(f"{i} is Odd")