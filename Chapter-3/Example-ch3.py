#We will do string exercise with indexing, negative slicing and builtin functions as well

'''
hello indexing can be done in two ways
1) 0 -> 5           normal method
2) -5 -> -1         negative indexing method
'''
var_str = "Hello"
print(var_str[0:5])     #Indexing where the string starts from 0th index and ends at length - 1 index
print(var_str[:3])      #Indexing where :3 is equals to 0:3
print(var_str[2:])      #Indexing where 2: is equals to 2:5
print(var_str[-5:])     #Indexing where -5: is equals to 0:5


'''
String manipulation with different inbuilt functions or methods
'''

var_method = "Hello World from python"
print(var_method.find("World"))
print(var_method.replace("World","world"))
print(var_method.index("python"))