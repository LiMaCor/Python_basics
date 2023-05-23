# Python provides built-in JSON libraries to encode and decode JSON
# In order to use json model, it must first be imported
# 
# There are two basics formats for JSON data: either in a string or the object datastructure.
# The object datastructure, in Python, consists of lists and dictionaries nested inside other.
# 
# The object datastructure allows one to use Python methods to add, list, search and remove 
# elements from datastructure.
# 
# To load JSON back to a data structure, use the "loads" method.
import json
print(json.loads("""
                 {
                     "testingNode": "testing response from node 1"
                 }
                 """))

# To encode a data structure to JSON, use the "dumps" method.
json_string = json.dumps([1, 2, 3, "a", "b", "c"])
print(json_string)

# Python supports a Python propietary data serialization method called pickle
import pickle
pickled_string = pickle.dumps([1, 2, 3, "a", "b", "c"])
print(pickle.loads(pickled_string))