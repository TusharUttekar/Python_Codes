#List(Array's) and Tupple with exercise and example

'''
List are mutable means we can modify them unlike string's which are immutable
Tupple as well is immutable like string type
'''

my_list = ["abcd", "john", "cj", "ble", 4, 5.0, True]

print(my_list)
print(my_list[2])

#operations on the list

my_list.append(45)
my_list.insert(6,"hello")
print(my_list)

#Tupple

my_tupple = (1,2,3,4,5)

print(my_tupple)
print(my_tupple.count(4))
print(my_tupple.index(3))
print(len(my_tupple))