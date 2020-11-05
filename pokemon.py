# program is written by Prasanna Sahera

import random
from time import sleep

choices = ["Charmander", "Squirtle", "Bulbasaur"]
computer = random.choice(choices)

name = input("Hello, Please enter your name: ")
print(f"Hello {name}, Welcome to Pockemon Battles Game!!")

player = False
while player == False :
    player = input("\nWhich pokemon do you want to choose?\n'Charmander': 'Charmander'\n'Squirtle': 'Squirtle'\n'Bulbasaur': 'Bulbasaur'\n'Stop the game': 'Stop': "
)
    if player == computer:
        print("Tie!!")
    elif player == "Charmander":
        if computer == "Squirtle":
            print("\n Please, wait we are loading your results...")
            sleep(2)
            print(" You Lose!!")
        else:
            print("\n Please, wait we are loading your results...")
            sleep(2)
            print(" You Win!!")

    elif player == "Squirtle":
        if computer == "Bulbasaur":
            print("\n Please, wait we are loading your results...")
            sleep(2)
            print(" You Lose!!")
        else:
            print("\n Please, wait we are loading your results...")
            sleep(2)
            print(" You Win!!")

    elif player == "Bulbasaur":
        if computer == "Charmander":
            print("\n Please, wait we are loading your results...")
            sleep(2)
            print(" You Lose!!")
        else:
            print("\n Please, wait we are loading your results...")
            sleep(2)
            print(" You Win!!")
    elif player == "Stop":
        print(" Thanks for playing")
        break
    else:
        print(" That's not a valid play!")
    player = False
