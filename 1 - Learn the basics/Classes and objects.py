# Objects are an encapsulation of variables and functions into a single entity
# Classes are essentially a template to create your objects
class MyClass:
    variable = "blah"
    
    def function(self):
        print("This is a message inside the class.")

# To assign the above class to an object you would do the following
myobjectx = MyClass()

# Now the variable "myobjectx" holds an object of the class "MyClass" that contains
# the variable and function defined within the class called "MyClass".
# To access the variable inside of the newly created object "myobjectx", you would do the following
print(myobjectx.variable)

# We can have different independent instances of the same class.
# Each instance shares the same properties and functions of the class, but changes made to one of these instances
# are only available in that instance that changed
myobjecty = MyClass()
myobjecty.variable = "nah"
print(myobjectx.variable)
print(myobjecty.variable)

# The "__init__()" function is a special function that is called when the class is being initiated.
# It's used for assigning values in a class
class NumberHolder:
    
    def __init__(self, number):
        self.number = number
    
    def function(self):
        print("This is the number that has initialised this instance of the class 'NumberHolder': %d" % self.number)

myobjectz = NumberHolder(4)
myobjectz.function()