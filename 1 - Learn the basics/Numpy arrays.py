# Numpy arrays are faster alternatives to Python lists.
# They're also easy to work and gives users the opportunity 
# to perform calculations across entire arrays
height = [1.87, 1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 92.25, 92.98, 86.18, 88.45]

import numpy as np

np_height = np.array(height)
np_weight = np.array(weight)
print(type(np_height))

# Element-wise calculations are fast and computationally efficient calculations.
# They're particularly helpful when you have 1000s of observations in your data.
bmi = np_weight / np_height ** 2
print(bmi)

# Another great feature of Numpy arrays is the ability to subset.
print(bmi > 24)
print(bmi[bmi > 24])