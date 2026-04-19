# Init

x=15
def addition(y, x_assign):
    x=x_assign
    # string literals
    print(f"Adding {x} to {y} is: ", x+y, " With Type: ", type(x+y))

# inputs
input_assign = input('Enter the second number to add: ')
# typecasting with eval
addition(5, eval(input_assign))
