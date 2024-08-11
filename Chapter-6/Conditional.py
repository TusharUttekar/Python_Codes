#Simple if else ladder state same as any other programming language just a change in indendation

let_list = ["Alpha", "Beta", "Gama", "Zeta"]

inputs = input("Enter the user input : ")

#We can use builtin function in the conditional checking based on the required condition
if(inputs in let_list):
    print("The user input is present in the list")
else:
    print("The user input is not present in the list")

#We can also use logical conditions such as and, or and not within the conditional checking statement

ip = int(input("Enter a number : "))

if(ip > 10 and ip < 100):
    print("Entered number is greater than 10")
    if(ip > 50):
        print("Entered number is greater than 50")
elif(not(ip)):
    print("Entered number is 0")
else:
    print("Entered number is less than 10")