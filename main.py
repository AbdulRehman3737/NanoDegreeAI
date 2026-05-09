# Init
from random import random

import module_math as mm

x=15
# function initialize
def addition(x_assign, y = 10):
    x=x_assign
    # conditional
    if x > y:
    # string literals with 'f string'
        print(f"Adding {x} to {y} is: ", x+y, " With Type: ", type(x+y))
    else:
        print("Else condition achieved")

# inputs
input_assign = input('Enter the second number to add: ')
# typecasting with eval
addition(eval(input_assign), 5)

# args(start, stop, step)
custom_range = range(10, 0, -2)
for item in custom_range:
    print("Looped: ", item)

# List(array)
array = ['first', 'second', 'third']
for item in range(len(array)):
    print('Array mappedL: ', item, array[item])

# String splicing
# 0->len | -1->-len
string = 'Hey There '
# str + str => .concat()
print('Spliced: ', string[0:6], string + string)

# Unicode assinged to everything
print("Unicode reps: ", ord('A'), chr(65))

# String are immutable and do not support reassignment
immutable = 'I do not dream of labour'
# Error is expected here
# immutable[0] = "I W"
print("Assigned place in memory: ", id(immutable))

# Split, assumes '' if nothing passed, works same as .split() in js
print("Split: ", immutable.split('not'))

# Escape characters
print("Escape characters: ", "This is a new line \n and this is a tab \t and this is a backslash \\ and this is a single quote \' and this is a double quote \" ")

# Sets, can also be init by class(prototype) x= set((val, val))
uniqSet = {"red", "green", "blue", True, 3}
# 1==True, 0==False, so if 1 and True in the set, will only keep either
uniqSet.add('yellow')
uniqSet.update(['blue', 'violet'])
uniqSet.update(('Leomord', 'Hecarim'))
print("Set: ", len(uniqSet), uniqSet)

# Set operations
print("Union: ", uniqSet.union({'lavendar', 'indigo'}))

# Dictonaries, key-value pairs, can also be init by class(prototype) x= dict((key, value))
dict = {'name': 'John', 'age': 30, 'city': 'New York'}
dict.update({'country': 'USA'})
print("Dictionary: ", dict, " Keys: ", dict.keys(), " Values: ", dict.values(), " Items: ", dict.items())

fileName = 'readFile.txt'

# Read from file, 'r' for read, 'w' for write, 'a' for append, 'x' for create
fileObj = open(fileName, 'r')
print(fileObj.read())
fileObj.close()

# Alternative to above, with statement ensures that the file is closed after the block is executed, even if an error occurs
with open(fileName, 'r') as f:
    print("With statement: ", f.read())
    
# Write to file, 'w' will overwrite the file, 'a' will append to the file, 'x' will create a new file and write to it, if the file already exists, it will raise an error
with open(fileName, 'w') as w:
    w.write("This is a new line added to the file.\n")
with open(fileName, 'r') as f:
    print("With statement: ", f.read())
    
# Exception handling
try:
    print(an_undefined_var) # type: ignore
    # Exception specifically for NameError, which occurs when a variable is not defined
except NameError as e:
    print("NameError: ", e)
    # Catch all other exceptions
except Exception as e:
    print(e)
    
try:
  print(x)
except:
  print('Something went wrong')
# Can raise exceptions manually with the raise keyword, which can be used to trigger an exception when a certain condition is met, or to re-raise an exception that was caught in an except block
  raise
# Finally block is executed regardless of whether an exception is raised or not, and is typically used for cleanup actions, such as closing files or releasing resources
finally:
  print('The try except is finished')
  
# Importing from module
print(mm.add_num(5, 25))
print(mm.access_var)

# Get all the attributes of a module, which includes functions, variables, and classes defined in the module, as well as built-in attributes like __name__ and __file__
print(dir(random))

# Classes init (OOP)
class Student:
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department
        
student1 = Student('Arthas Menethil', 30, 'CEO of Icecrown Citadel')
print("Student: ", student1.name, student1.age, student1.department)