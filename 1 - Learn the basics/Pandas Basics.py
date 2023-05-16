# Pandas is a high-level data manipulation tool.
# It's built on the Numpy package and its key data structure is called the DataFrame.
# DataFrames allows to store and manipulate tabular data in rows of observations and columns of variables
# There are several ways to create a DataFrame, one of them is using a dictionary
dict = {
    "country": [
        "Brazil",
        "Russia",
        "India",
        "China",
        "South Africa"
    ],
    "capital": [
        "Brasilia",
        "Moscow",
        "New Dehli",
        "Beijing",
        "Pretoria"
    ],
    "area": [
        8.516,
        17.10,
        3.286,
        9.597,
        1.221
    ],
    "population": [
        200.4,
        143.5,
        1252,
        1357,
        52.98
    ]
}

import pandas as pd
brics = pd.DataFrame(dict)
print(brics)

# If you would like to have different index values instead default numbers defined in the Pandas module
# you can do that easily as well.
brics.index = ["BR", "RU", "IN", "CH", "SA"]
print(brics)

# Another way to create a DataFrame is by importing a csv file using Pandas.
cars = pd.read_csv("1 - Learn the basics\pandas_resources\cars.csv")
print(cars)

# There are several ways to index a Pandas DataFrame
# one of the esiest ways to do this is by using square bracket notation.
# You can either use a single bracket or a double bracket.
# The single bracket will output a Pandas Series, while a double bracket will output a Pandas DataFrame
cars = pd.read_csv("1 - Learn the basics\pandas_resources\cars.csv", index_col=0)
print(cars["cars_per_cap"])
print(cars[["cars_per_cap"]])
print(cars[["cars_per_cap", "country"]])

# Square brackets can also be used to access observations from a DataFrame
print(cars[0:4])
print(cars[4:6])

# You can also use the "loc" and "iloc" functions to perform just about any data selection operation.
# "loc" function is label based, which means that you have to specify rows and columns based on their rwo and column labels.
# "iloc" is integer index based, so you have to specify rows and columns by their index.
print(cars.iloc[2])
print(cars.loc[["AUS", "EG"]])