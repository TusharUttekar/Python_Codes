#Exercise for understanding basics of class

class Example:
    #Attributes
    value = 1000
    string = "ABCDEFG"

    #Constructor
    def __init__(self, value = 1000, str= "xyz"):   #We can use slf instead of self here
        self.value = value
        self.string = str

    #Methods/Functions
    def get_value(self):
        print(f"The value for the object is {self.value}")

    def get_str(self):
        print(f"The string for the object is {self.string}")

    @staticmethod
    def default():
        print("Static method inside a class")


B = Example(456,"XYZ")
B.default()
B.get_value()
B.get_str()

A = Example()
A.default()
A.get_value()
A.get_str()


'''
Instance Attributes
-Belong to individual objects.
-Defined within the __init__ method.
-Unique for each object.
-Accessed using the object's name and dot notation.

Example code :

class Car:
    def __init__(self, color, make, model):
        self.color = color  # Instance attribute
        self.make = make  # Instance attribute
        self.model = model  # Instance attribute

car1 = Car("red", "Toyota", "Camry")
car2 = Car("blue", "Honda", "Civic")

print(car1.color)  # Output: red
print(car2.color)  # Output: blue



Class Attributes
-Belong to the class itself.
-Defined outside any method.
-Shared by all objects of the class.
-Accessed using the class name or an object's name.

class Car:
    wheels = 4  # Class attribute

    def __init__(self, color, make, model):
        self.color = color
        self.make = make
        self.model = model

car1 = Car("red", "Toyota", "Camry")
car2 = Car("blue", "Honda", "Civic")

print(car1.wheels)  # Output: 4
print(Car.wheels)  # Output: 4

Important Points
-Modifying a class attribute affects all objects.
-Modifying an instance attribute affects only that specific object.
-Use class attributes for values that are constant across all objects.
-Use instance attributes for values that vary between objects.
-You can access class attributes through an instance, but modifying them this way might lead to unexpected behavior.

When to Use Which:

Class attributes: For shared properties or constants.
Instance attributes: For object-specific data.

'''