'''
author:Lakshmy Byju
date:03-12-2024
python program to show a game
'''
import random

print("Welcome to the show")
doors=[1,2,3]
host=random.choice(doors)
participate=int(input("please choose a door"))
if participate==host:
    print("You won")
else:
    print("You have choosen wrong option")
    replay=input("Do you want to change the option")
    if replay=='yes':
        received =int(input("choose another option"))
        if received==host:
            print("you won")
        else:
            print("You have got a goat  again,you lost")
        if replay=="no":
            print("you have got a goat ,so you loose")