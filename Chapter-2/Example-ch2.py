# We will test arithmatic and logical operators

'''
Naming of the varibles allows alphabets, numbers and underscore
it does not allow whitespace and special symbol like e.g.'@'
the varible name cannot start with a number
'''
var_int = 5             #This is a integer data type
var_float = 5.6         #This is a float data type
var_string = "Example"  #This is a string data type

# Test the varible by printing
print(var_int)
print(var_float)
print(var_string)


'''
Arithmatic operators include basic mathematical operations like
+-/*
+=,-=,*=,/=
'''
a = 5
b = 6
print(a + b)

d = 4
d *=2
print(d)

'''
logical and comparison operators like
>,<,>=,<=,==,!=
and, or, not
'''

print(a == b)
print(True and False)
print(True or False)
print(not(True))