# Init

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
uniqSet = {"red", "red", "green", "blue", 1, True, 3,3}
# 1==True, 0=False, so if 1 and True in the set, will only keep either
uniqSet.add('yellow')
uniqSet.update(['blue', 'violet'])
uniqSet.update(('Leomord', 'Hecarim'))
print("Set: ", len(uniqSet), uniqSet)