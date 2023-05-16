# A dictionary is a data type similar to arrays, but works with keys and values instead of indexes.
phonebook = {}
phonebook["Julian"] = 678332901
phonebook["Lian"] = 6338920123
phonebook["Engel"] = 654889005
print(phonebook)

# You can initialise a dictionary with the same values in the following pattern
phonebook = {
    "Aldia" : 783456921,
    "Gryphus" : 619022839,
    "Griever" : 664839013
}
print(phonebook)

# You can iterate over a dictionary just like a list. However, a dictionary, unlike a list
# does not keep the order of the values storid in it
phonebook = {
    "Sky" : 638900354,
    "Lya" : 622979364,
    "Koti" : 735402819,
    "Derek" : 613325873,
    "Paula" : 677832004
}
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

# To remove a specified index, use either one of the following notations
phonebook = {
    "Nerea" : 647889037,
    "Esther (pelo blanco)" : 635554892,
    "Fer" : 689980337
}
del phonebook["Fer"]
print(phonebook)
phonebook.pop("Esther (pelo blanco)")
print(phonebook)