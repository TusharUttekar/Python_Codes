#file io example to update the file based on the user input

import random

def function():
    print("Choosing the number...")
    score = random.randint(1,20)

    #get the value from the file
    with open("score.txt") as F:
        Filescore = F.read()

        if(Filescore != ""):
            Filescore = int(Filescore)
        else:
            Filescore = 0
    
    print(f"User input is {score}")

    if(score > Filescore):
        with open("score.txt", "w") as F:
            F.write(str(score))

    return score

function()