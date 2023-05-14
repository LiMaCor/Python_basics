# Lists are very similar to arrays but not the same.
# They can contain any type of variable and many of them as you wish
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0])
print(mylist[1])
print(mylist[2])

# You can also iterate over a lsit very easily
for x in mylist:
    print(x)

# Accesing an index that doesn't exists, raises an exception

mylist = [1, 2, 3]
# Try this uncommented, then comment it again
#print(mylist[10])