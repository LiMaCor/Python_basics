# Like in other programming languages, the addition, substraction, multiplication and division operators are available in Python
number = 1 + 2 * 3 / 4.0
print(number)

# Another operator available is the modulo, wich returns the integer remainder of a division
remainder = 11 % 3
print(remainder)

# Using two multiplication symbols makes a power operator
squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)

# As seen on the "Variables and types.py", Python supports concatenating strings using the addition operator
helloworld = "hello" + " " + "world"
print(helloworld)

# Python also supports multiplying strings to form a string with a repeating sequence
lotsofhellos = "hello" * 10
print(lotsofhellos)

# Lists can be even joined with addition operators
even_numbers = [2, 4, 6, 8]
odd_numbers = [1, 3, 5, 7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

# Like with strings, Python supports forming new lists with a repeating sequence using the multiplication operator
print([1, 2, 3] * 3)