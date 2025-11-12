# Day 1: 30 Days of python programming

# Do the following operations. The operands are 3 and 4:
print(3+4) 
print(3-4)
print(3*4)
print(3%4)
print(3/4)
print(3**4)
print(3//4)

# Write strings in python:
print("Emrik")
print("Rellmar")
print("Sweden")

# Check the data types of the following data:
print(type(10))      
print(type(9.8))
print(type(3.14))
print(type(4-4j))   
print(type(['Asabeneh', 'Python', 'Finland']))
print(type('Emrik'))
print(type("Rellmar"))
print(type("Sweden"))

# 1. Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.
print(1) # Integer
print(1.0) # Float
print(2 + 5j) # Complex
print("Hello, World!") # String
print(True) #Boolean

numbers_list = [1, 2, 3, 4, 5] # List
print(numbers_list)

numbers_tuples = (6, 7, 8, 9, 10) # Tuples
print(numbers_tuples)

numbers_set = {11, 12, 13, 14, 15} # Set
print(numbers_set) 

dictionary = { # Dictionary
    'first_name': 'Emrik',
    'last_name': 'Rellmar',
    'country': 'Sweden',
    'age': 19,
    'is_married': False,
    'skills': ['Skill 1', 'Skill 2', 'Skill 3']

}
print("Person Dictionary:", dictionary) 
print("First name:", dictionary['first_name']) 
print("Number of skills:", len(dictionary['skills']))

# 2. Find an Euclidian distance between (2, 3) and (10, 8)
x1, y1 = 2, 3 # En punkt med kordinaterna (2,3)
x2, y2 = 10, 8 # En punkt med kordinaterna (10, 8)

euclidean_distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5 
print(euclidean_distance)

