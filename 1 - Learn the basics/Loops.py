# "for" loops can iterate over a sequence of numbers using the "range" and "xrange" functions.
# The difference between "range" and "xrange" is that "range" returns a list with numbers of that specified range
# whereas "xrange" returns an iterator, which is more efficient
for x in range(5):
    print(x)

for x in range(3, 6):
    print(x)

for x in range(3, 8, 2):
    print(x)

# "while" loops repeat as long as a certain boolean condition is met
count = 0
while count < 5:
    print(count)
    count += 1

# The "break" statement is used to exit a for loop or a while loop
# On the other hand, the "continue" statement is used to skip the current block and return to the "for" or "while" loop
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

for x in range(10):
    if x % 2 == 0:
        continue
    print(x)

# Unlike other languages, Python supports the use of "else" for loops.
# When the loop condition of "for" or "while" statement fails, then code part in an "else" statement is executed
# If a "break" statement is executed inside the "for" or "while" loop, then the "else" part is skipped,
# but if there is a "continue" statement, the "else" part is executed.
count = 0
while(count < 5):
    print(count)
    count += 1
else:
    print("count variable reached %d" % count)

for i in range(1, 10):
    if (i % 5 == 0):
        break
    print(i)
else:
    print("This part is not printed because 'for' loop is terminated because of 'break' statement but not due to fail in condition.")
