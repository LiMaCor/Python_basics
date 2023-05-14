# To print the length of a string, we use the "len()" function
helloworld_string = "Hello world!"
print(len(helloworld_string))

# We can get the index of a character in string using the "index()" function
# The "index()" function only retrieves the index position for the first occurrence for a given string
helloworld_string = "Hello world!"
print(helloworld_string.index("o"))

# If we want to know how many times a substring is repeated insed a string, we could use the "count()" function
helloworld_string = "Hello world!"
print("How many l's are in the string 'Hello world!'?: %d" % helloworld_string.count("l"))
print("How many 'Hello' words are in the string 'Hello world!'?: %d" % helloworld_string.count("Hello"))

# Also, we can have a slice of a string using ranges
helloworld_string = "Hello world!"
print(helloworld_string[3:7])

# There is no reverse function to get a string reversed, but we could use of the slice syntax to get an string reversed
helloworld_string = "Hello world!"
print(helloworld_string[::-1])

# To get a string with all letters formatted as upper or lowercase, we can use the "upper()" and "lower()" functions
helloworld_string = "Hello world!"
print(helloworld_string.upper())
print(helloworld_string.lower())

# To find out if a given strings starts or ends with something, we can use the "startswith()" and "endswith()" functions respectively
# These functions returns "True" if the strings starts or ends with a given string and returns "False" if the string doesn't finds 
# an occurrence at the beginning or ending of the original string
helloworld_string = "Hello world!"
print(helloworld_string.startswith("Hello"))
print(helloworld_string.endswith("asdfasdf"))

# With the "split()" function, we can split a string with a separator passed as a parameter to the "split()" function, grouped together in a list
helloworld_string = "Hello world!"
separated_words = helloworld_string.split(" ")
print(separated_words)