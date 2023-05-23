# We can use Python's lambda functions which are inline fucntions defined at the same place we use it.
# They don't have a name, so they also called anonymous functions.
# We define a lambda function using the keyword "lambda".
a = 1
b = 2
sum = lambda x,y : x + y
c = sum(a, b)
print(c)