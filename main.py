# Init
from random import random
from abc import ABC, abstractmethod

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

class Person(ABC):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.__gender = gender # private variable, can only be accessed within the class, and not by instances of the class or subclasses, it is denoted by double underscore __ before the variable name
    # Abstract method, which is a method that is declared but not implemented in the parent class, and must be implemented in the child class, if the child class does not implement the abstract method, it will raise an error
    @abstractmethod
    def is_faculty(self):
        pass
    def gender_print(self):
        return self.__gender
class Student(Person):
    def __init__(self, name, age, gender, department):
        # Inheritance, super() is used to call the __init__ method of the parent class, which allows us to initialize the name and age attributes of the Student class using the __init__ method of the Person class
        super().__init__(name, age, gender)
        self.department = department
        
    def is_faculty(self):
        return False
class Teacher(Person):
    def __init__(self, name, age, gender, department):
        # Inheritance, super() is used to call the __init__ method of the parent class, which allows us to initialize the name and age attributes of the Student class using the __init__ method of the Person class
        super().__init__(name, age, gender)
        self.department = department
        
    def is_faculty(self):
        return True

# Cannot instantiate an abstract class, which is a class that contains one or more abstract methods, and cannot be instantiated directly, but can be subclassed by other classes that implement the abstract methods,
# if we try to instantiate an abstract class, it will raise an error
try:
    person_instance = Person("asd", 10)
except Exception as e:
    print(e)
student1 = Student('Arthas Menethil', 30, "Doom", "CEO of Icecrown Citadel")
teacher1 = Teacher('Uther Lightbringer', 45, "Light", "Paladin of Silver Hand")
print("Student: ", student1.name, student1.age, student1.department, student1.is_faculty(), student1.gender_print())
print("Teacher: ", teacher1.name, teacher1.age, teacher1.department, teacher1.is_faculty(), teacher1.gender_print())

# =========================
# Additional Important Concepts
# =========================

# Tuples (immutable collections)
tuple_example = ('apple', 'banana', 'orange')
print("Tuple:", tuple_example, tuple_example[1])

# List methods
numbers = [1, 2, 3]
numbers.append(4)
numbers.remove(2)
numbers.insert(1, 99)
print("List methods:", numbers)

# List comprehension
squares = [x*x for x in range(5)]
print("List comprehension:", squares)

# break, continue, pass
for i in range(5):
    if i == 2:
        continue
    if i == 4:
        break
    print("Loop control:", i)

def empty_func():
    pass

# While loop
counter = 0
while counter < 3:
    print("While loop:", counter)
    counter += 1

# enumerate() gives index + value
langs = ['Python', 'Java', 'C++']
for index, value in enumerate(langs):
    print("Enumerate:", index, value)

# zip() combines iterables
names = ['John', 'Jane']
scores = [90, 85]

for n, s in zip(names, scores):
    print("Zip:", n, s)

# Lambda functions
multiply = lambda a, b: a * b
print("Lambda:", multiply(3, 4))

# map() applies function to iterable
mapped = list(map(lambda x: x * 2, [1, 2, 3]))
print("Map:", mapped)

# filter() filters iterable
filtered = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))
print("Filter:", filtered)

# Recursion
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print("Recursion factorial:", factorial(5))

# *args and **kwargs
def demo_args(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

demo_args(1, 2, 3, name="Python", type="Language")

# Scope
global_var = "I am global"

def scope_test():
    local_var = "I am local"
    print(global_var)
    print(local_var)

scope_test()

# Type checking
print("Type checking:", isinstance(5, int))

# Copy vs reference
list_a = [1, 2, 3]
list_b = list_a
list_c = list_a.copy()

list_b.append(4)

print("Reference copy:", list_a)
print("Actual copy:", list_c)

# Generator using yield
def simple_generator():
    yield 1
    yield 2
    yield 3

for val in simple_generator():
    print("Generator:", val)

# =========================
# More OOP Concepts
# =========================

class Animal:
    species = "Unknown"  # Class variable

    def __init__(self, name):
        self.name = name

    # String representation
    def __str__(self):
        return f"Animal: {self.name}"

    # Static method
    @staticmethod
    def static_example():
        return "Static methods do not access instance data"

    # Class method
    @classmethod
    def class_example(cls):
        return cls.species

dog = Animal("Husky")

print(dog)
print(Animal.static_example())
print(Animal.class_example())

# Getter and Setter (Encapsulation)

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount

account = BankAccount(1000)

print("Getter:", account.get_balance())

account.set_balance(500)

print("Setter:", account.get_balance())

# =========================
# Regular Expressions (Regex)
# =========================

import re

text = "My phone number is 12345"

match = re.search(r'\d+', text)

if match:
    print("Regex found:", match.group())

# =========================
# Main Entry Point
# =========================

def main():
    print("Program started from main")

if __name__ == "__main__":
    main()