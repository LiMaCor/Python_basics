# Python uses a C-style string formatting to create new formatted strings.
# The "%" operator us used to format a set of variables enclosed in a "tuple", together with a format string.
# These strings also contains a text together with "argument specifiers", special symbols like "%s" or "%d"
name = "Julian"
print("Hello, %s!" % name)

# You can use a tuple to specify two or more arguments specifiers
# A tuple is a fixed size list
name = "Julian"
age = 27
print("%s is %d years old." % (name, age))

# Any object which is not a string can be formatted using the "%s" operator as well.
# The string returned of that object is formatted as the string.
mylist = [1, 2, 3]
print("A list: %s" % mylist)

# These are some basic arguments specifiers in Python
# String argument specifier "%s"
name = "Julian"
job = "Salesforce Technical Architect"
print("%s works as %s in Calibre 360" % (name, job))
# Integer argument specifier "%d"
price = 40
print("The shipping tax costs around %d dollars!" % price)
# Floating point numbers "%f"
currency_devaluation = 0.437
print("Last time I checked it out, the SHIB crypto currency had a %f of devaluation" % currency_devaluation)
# Floating point numbers with fixed amount of digits to the right dot "%.<number of digits to format>f"
power_price = 0.63482931728394783
gas_price = 0.5673
print("The current prices on the power energy market are %.6f and %.2f for the gas energy market" % (power_price, gas_price))
# Integers in hex representation "%x", "%X" (lower and uppercase)
fifty_hex = 50
twelve_hex = 12
print("%X and %X are the hex representation for the 50 and 12 numbers respectively" % (fifty_hex, twelve_hex))