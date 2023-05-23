# Every functionin Python receives a predefined number of arguments, if declared normally.
# It is possible to declare functions which receive a variable number of arguments, using the following syntax:
def foo(first, second, third, *therest):
    print("First parameter: %s" % first)
    print("Second parameter: %s" % second)
    print("Third parameter: %s" % third)
    print("And all the rest... %s" % list(therest))

foo(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# It is also possible to send function arguments by keyword, so that the order of the
# argument does not matter, usign the following syntax:
def bar(first, second, third, **options):
    if options.get("action") == "sum":
        print("The sum is: %d" % (first + second + third))
    
    if options.get("number") == "first":
        return first

result = bar(1, 2, 3, action = "sum", number = "first")
print("Result: %d" % result)