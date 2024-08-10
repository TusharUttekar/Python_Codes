#Dictionary data type in python is key value pair

#To create a empty dictionary use the following syntex
# d = {}
#Dictionary are unordered, muttable and not indexed

dictionary = {
    "Tomato"    : 20,
    "Potato"    : 30,
    "Coliflower": 40
}

#To print the dictionary and access particular element
print(dictionary["Tomato"])
print(dictionary.get("Brinjal"))    #Does not raise an error if the element is not present.
print(dictionary["Brinjal"])        #Raises a KeyError if the element is not present.

local_key = input("Get the user key input : ")
local_value = input("Get the user value input : ")

#Update the dictionary based on the user input
dictionary.update({local_key : local_value})

#Print the updated dictionary content
print(dictionary)

#Methods
print(dictionary.items())
print(dictionary.keys())
print(dictionary.values())