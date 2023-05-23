# Generators are used to create iterators but with a diferent approach.
# Generators return iterable set of items, one at a time, in a special way.
# When an iteration over a set of item starts using the for statement, the generator is run.
# Once the generator's funtion code reaches a "yield" statement, the generator yields its execution back to the for loop.
# Then, the generator function can generate as many values (possibly infinite) as it wants, yielding each one in its turn.

import random
def lottery():
    for i in range(6):
        yield random.randint(1, 40)
    
    yield random.randint(1, 15)

for random_number in lottery():
    print("And the next number is ... %d!" % random_number)
