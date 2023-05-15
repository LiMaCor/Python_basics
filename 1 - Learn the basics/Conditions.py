# Python uses boolean logic to evaluate conditions
x = 2
print(x == 2)
print(x == 3)
print(x < 3)

# The "and" and "or" boolean operators allow building complex boolean expressions
name = "Julian"
age = 27
if name == "Julian" and age == 27:
    print("Your name is %s, and you're also %d years old." % (name, age))

if name == "Julian" or name == "Lian":
    print("Your name is either Julian or Lian.")

# The "in" operator could be used to check if a specified object exists within an iterable object container
name = "Julian"
if name in ["Lian", "Julian"]:
    print("Your name is either Julian or Lian.")

# Python uses indentation to define code blocks, instead of brackets.
# The standard Python indetation is 4 spaces. Any number of tabs or spaces will work too either, as long as it is consistent

statement = False
another_statement = True
if statement is True:
    print("The statment isn't false.")
    pass
elif another_statement is True:
    print("The counter statement is true.")
    pass
else:
    print("Neither of the two statements is true.")
    pass

# Unlike other programming languages, Python has the "is" operator to match the instances of two variables, instead of their values
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)
print(x is y)

# Using the "not" operator before a boolean expression inverts it
print(not False)
print((not False) == (False))
