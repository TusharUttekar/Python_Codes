#Exercise we will see inheritance concept with multiple and multilevel inheritance

#Normal class definition
class Student:
    Position = "Student"

    def __init__(self):
        print("Constructor from student class.")

    def show_student(self):
        print("This represents student class.")

    @classmethod    #Decorates a method to receive the class as the first argument.
    def class_method(cls):
        print(f"The class method from {cls.Position} class")

#Class inheritance from the student class
class Teacher(Student):
    Position = "Teacher"

    def __init__(self):
        super().__init__()  #Call's the contructor of the parent class/inherited class
        print("Constructor from teacher class.")

    def show_teacher(self):
        print("This represents teacher class.")

    @property   #Decorates a method to read only attribute means you can access method as a attribute
    def teacher_name(self):
        return f"Teacher name is {self.name}"
    
    @teacher_name.setter    #Decorates creates a setter method to set the value of an attribute(name)
    def teacher_name(self,value):
        self.name = value

#Multilevel inheritance from student->teacher->principal
class Principal(Teacher):
    Position = "Principal"

    def __init__(self):
        super().__init__()  #Call's the contructor of the parent class/inherited class
        print("Constructor from Principal class.")

    def show_principal(self):
        print("This represents principal class")


A = Principal()
A.show_student()
A.show_teacher()
A.show_principal()

B = Teacher()
B.show_student()
B.show_teacher()

#Call to the setter method
B.name = "Suresh"   

#Call to the property decorator method
print(B.teacher_name)


C = Student()
C.show_student()

#Call to the class method
C.class_method()


