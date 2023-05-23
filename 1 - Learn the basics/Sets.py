# Sets are lists with no duplicate entries.
print(set("My name is Julian and Julian is my name".split()))

# Sets are a powrful tool in Python since they have the ability to 
# calculate differences and intersections between other sets.
# You can find out which elements in both sets are the same with the "intersection" method.
a = set(["Julian", "Sky", "Derek"])
print(a)
b = set(["Sky", "Julian", "Koti"])
print(b)
print(a.intersection(b))
print(b.intersection(a))

# You can find out which elements are in one of the two sets defined with the "symmetric_difference" method.
a = set(["Julian", "Sky", "Derek"])
b = set(["Sky", "Julian", "Koti"])
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))

# You can find out which elements are in one of the two sets and not the other with the "difference" method.
a = set(["Julian", "Sky", "Derek"])
b = set(["Sky", "Julian", "Koti"])
print(a.difference(b))
print(b.difference(a))

# You can also join the unique items from two defined sets with the "union" method.
a = set(["Julian", "Sky", "Derek"])
b = set(["Sky", "Julian", "Koti"])
print(a.union(b))