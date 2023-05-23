# Partial functions allow one to derive a function with x parameters to a 
# function with fewer parameters and fixed values set fro the more limited function.
#
# You can create partial functions in Python by using the partial function from the functools library.
from functools import partial

def multiply(x, y):
    return x * y

dbl = partial(multiply, 2)
print(dbl(4))

# In order for the previos function to work correctly with the "partial" method invocation 
# it's mandatory that the function that calls the partially issued function, recieves
# at least, one or more parameters according to the paramteres required in the partially
# issued function