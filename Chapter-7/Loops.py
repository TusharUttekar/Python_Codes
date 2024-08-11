#Simple for and while loop with some conditions such as break/continue/pass used inside loops based on requirement
'''
Break -> Exits the loop when a certain condition gets true
Continue -> Skips the next set of statements in the loop and start next iteration of the loop
Pass -> It is a null operater/statement in python.
'''

let_list = ["Alpha", "Beta", "Lamda", "Gamma"]

for i in let_list:
    if(i.endswith("a")):
        print(f"List value {i}")

#The range operator has three arguments start, stop and step size

for i in range(0,10,5):
    print(i)

#While loop

j = 0

while(j<5):
    print(j)
    j = j + 1

#Star Pattern

'''

***
* *       for n = 3
***


'''
n = int(input("Enter the number: "))
for i in range(1, n+1): 
    if(i==1 or i==n):
        print("*"* n, end="")
    else:
        print("*", end="")
        print(" "* (n-2), end="")
        print("*", end="")
    print("")