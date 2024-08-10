'''
A set in Python is an unordered collection of unique elements.
It's defined by curly braces {} or the set() function.
Sets are used for mathematical set operations like union, intersection, difference, and symmetric difference.

Key characteristics:

Unordered: Elements have no specific order.
Unindexed: You cannot access elements by their position.
Mutable: You can add or remove elements.
No duplicates: Each element appears only once.

it's important to note that the elements within a set must be immutable.
This means you cannot have mutable objects like lists or dictionaries as elements of a set
'''

# Empty set
my_set = set()

# Set with elements
my_set = {1, 2, 3, 4}

# Methods
my_set.add(5)
my_set.update([6,7,8,9])
print(my_set)

my_set.remove(5)    #Raises a KeyError if the element is not present.
print(my_set)

my_set.discard(8)   #Does not raise an error if the element is not present.
print(my_set)
