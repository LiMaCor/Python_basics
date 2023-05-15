# Functions in Python are defined using the block keyword "def", followed with the function's name as the block's name
def my_function():
    print("Hello from my function!")
my_function()

# Functions may also recieve arguments
def my_function_with_args(username, greeting):
    print("Hello, %s, from my function! I wish you %s" % (username, greeting))
my_function_with_args("Lian", "luck")

# Functions may return a value to the caller using the keyword "return"
def sum_two_numbers(a, b):
    return a + b
x = sum_two_numbers(4, 9)
print(x)