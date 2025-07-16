# create a list of 5 items (fruits)
# fruits = ["Banana", "Orange", "Apple", "Guava", "Grapes"]
# print(fruits)
# fruits.append("Mango") #Add an item
# print(fruits)
# fruits.remove("Orange") #remove an item
# print(fruits)
# print(fruits[1:4]) #Access elements by index
# print(fruits[-1]) #last element
# print(fruits[0:3]) #slice a sublist
'''upto this list exercise'''

# fruits = ("Banana", "Orange", "Apple", "Guava", "Grapes", "Mango")
# print(fruits)
# fruits.append("Mango") #here we will get error because tuples are immutable. so we cant append or remove.
'''upto this tupple exercise'''

# nums = {1,2,3,3,4,5,5,5,6} #created a set with duplicates
# print(nums) #auto deduplication
# nums.add(10) #in list we are using append, but in sets we are using add
# print(nums)
# nums.remove(5) #remove an element
# print(nums)
'''upto this set exercise'''

# dict1 = {
#     "Surya":30,
#     "Abinaya":33,
#     "Ishu":31
# } #created a dictionary with 3 key value pairs
# print(dict1)
# print(dict1["Ishu"]) #access value by key
# dict1["Ishu"]=28 #update the value
# print(dict1) #print the updated value
#
# for key in dict1.keys():
#     print(key) #loop through keys only
#
# for value in dict1.values():
#     print(value) #loop through values only.
#
# for key,value in dict1.items():
#     print(f"{key}:{value}")
'''upto this dictionary exercise'''

#mini project
nums = [1,2,3,4,4,5,9,8,10]
print(nums)
print(type(nums))
sets = set(nums)
print(sets)
print(type(sets))
nums_new = list(sets)
print(nums_new)
print(type(nums_new))