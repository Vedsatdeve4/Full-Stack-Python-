# Accessing Items

#To access a specific element

dict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print("dict1['model']=" ,dict1["model"])

#To access a specific element using a variable

dict2 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = dict2["model"]
print("dict2['model']=" ,x)

# To access a specific element using 'get' method

dict3 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = dict3.get("model")
print("dict3['model'] =" ,x)
print()

#To access items in dictionary

dict4 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = dict4.items()
print("items =" ,x)

#To access values in dictionary
print("values =" , dict4.values())

#To access keys in dictionary
print("keys =" ,dict4.keys())
print()



#Build-in Function on Dictionary

dict5 = { "brand": "Ford",
         "model": "Mustang",
         "year": 1964,
         "anual": 2000}
print("len =" ,len(dict5))
print("max =" ,max(dict5))
print("min =" ,min(dict5))
print("sorted =" ,sorted(dict5))
print("sorted_rev =" ,sorted(dict5, reverse = True))
print()


dict6 = { "aa": "Ford",
         "ab": "Mustang",
         "ac": 1964,
         "ad": {1,2,3}}
print("len =" ,len(dict6))
print("max =" ,max(dict6))
print("min =" ,min(dict6))
print("sorted =" ,sorted(dict6))
print("sorted_rev =" ,sorted(dict6, reverse = True))
print("dict6 =" ,type(dict6["ad"]))
print()


dict7 = {"1": 1964,
        "10": "Ford",
         "3": "Mustang",         
         "1": 20}
print("len =" ,len(dict7))
print("max =" ,max(dict7))
print("min =" ,min(dict7))
print("sorted =" ,sorted(dict7))
print("sorted_rev =" ,sorted(dict7, reverse = True))
print("dict7 =" ,dict7["1"])
print()


#hetrogeneous list

dict8 = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "list": ["red", 1, 3.14, True],
  "Tuple": (1,2,3),
  "Set": {1,2,3}
}
print("dict8 =" ,dict8)
print()


#Changing values

dict9 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dict9["year"] = 2000
print("dict9 =" ,dict9)

# Using update method
dict9.update({"model": 30})
print("dict9 =" ,dict9)
print()

#Adding Items

dict11 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dict11["color"] = 2000
print("dic11 =" ,dict11)

# Using update method
dict11.update({"type": "car"})
print("dict11 =" ,dict11)
print()


#Removing items

dict12 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "color": "red",
  "type": "car"
}

#To remove the item with specified key
dict12.pop("model")
print("dict12 =" ,dict12)

#To remove  the last inserted item.
dict12.popitem()
print("dict12 =" ,dict12)

# To remove the item with the specified key name using del keyword
del dict12["color"]
print(dict12)

#TO remove all the elements from the dictionaries
dict12.clear()
print("dict12 =", dict12)

# The del keyword can also delete the dictionary completely
del dict12
print(dict12)

