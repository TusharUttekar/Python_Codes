#Exercise for making a snake, water and gun game
'''
Here we consider value as below for the given choice by the player
snake   1
water   2
gun     3

win condition

snake drinks water  1 < 2
water drowns gun    2 < 3
gun kills snake     3 > 1

'''
import random

SnakeDic = {"s" : 1, "w" : 2, "g" : 3}
RevsnakeDic = {1 : "Snake", 2 : "Water", 3 : "Gun"}


computer = random.choice([1,2,3])
userinput = input("Enter your choice : ")

print(f"Your choice is {RevsnakeDic[SnakeDic[userinput]]}")
print(f"Computer choice is {RevsnakeDic[computer]}")

if(computer == SnakeDic[userinput]):
    print("It's a draw")

else:

    if((computer - SnakeDic[userinput] == -1) or (computer - SnakeDic[userinput] == 2)):
        print("You lose!")
    else:
        print("You Win!")
