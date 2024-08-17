#We are going to learn basics of functions in this exercise

#Simple hello world function
def Hello():
    print("Hello World")

#Function with arguments
def argument(value):
    for i in range(0,value):
        print(i, end="")

#Function with default arguments
def default_argument(input = "....."):
    print("My name is" , input)

#Recurssive functions
def recursive(count):
    if not(count):
        return 1
    else:
        return count * recursive(count-1)
    
#All functions call from above

Hello()
argument(5)
default_argument()
default_argument("tushar")
print(recursive(5))
print(recursive(15))
print(recursive(25))
print(recursive(35))
        
        