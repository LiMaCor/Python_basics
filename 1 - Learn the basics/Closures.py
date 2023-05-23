# A Closure is a function object that remembers values in enclosing scopes 
# even if they are not present in memory.
#
# Nested functions are functions defined inside another function.
# Nested functions can access the variables of the enclosing scope. 
# However, at least in Python, they are only readonly.
def transmit_to_space(message):
    def data_transmitter():
        print(message)
    
    data_transmitter()

print(transmit_to_space("Test message"))

# To access the variable of an enclosing scope, we need to use the "nonlocal" keyword
def print_msg(number):
    def printer():
        nonlocal number
        number = 3
        print(number)
    printer()
    print(number)

print_msg(9)

# Remember that functions are objects in Python. You can return directly the function 
# rather than calling the nested function
def transmit_to_space(message):
    def data_transmitter():
        print(message)
    return data_transmitter

fun2 = transmit_to_space("Look at the Void")
fun2()