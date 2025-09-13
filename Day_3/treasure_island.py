import random
import time

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
*******************************************************************************
''')

print("Welcome to Treasure Island 2.0")
print("Your mission is to find the treasure before your rivals do!")

# Game state
health = 3
inventory = []

def pause():
    time.sleep(1)

# First choice
first = input("You are at a crossroad. Go Left or Right? ").lower()
if first == "right":
    print("Oh no! Rival pirates ambushed you.")
    health -= 1
    print(f"You lost 1 health. Health: {health}")
    if health <= 0:
        print("You died. Game over.")
        exit()
    print("You manage to escape back to the crossroad.")
    first = "left"

if first == "left":
    print("You find a small hut. Inside, you see a map and a sword.")
    choice = input("Do you take the sword, the map, or both? ").lower()
    if "sword" in choice:
        inventory.append("sword")
    if "map" in choice:
        inventory.append("map")
    print(f"Inventory: {inventory}")

# Second choice
second = input("You reach the shore. Swim across or Wait for a boat? ").lower()
if second == "swim":
    if "sword" in inventory and random.choice([True, False]):
        print("A shark attacked! But you fought it off with your sword.")
    else:
        print("A shark attacked and you couldn't escape.")
        health -= 2
        print(f"Health: {health}")
        if health <= 0:
            print("You died. Game over.")
            exit()
elif second == "wait":
    print("You waited and found a friendly fisherman who ferried you across.")

# Third choice
print("You arrive at Treasure Island. There are two paths: Jungle or Cave.")
third = input("Which path do you take? ").lower()

if third == "jungle":
    print("You encounter a venomous snake!")
    if "sword" in inventory:
        print("You kill it with your sword.")
    else:
        print("You get bitten!")
        health -= 1
        print(f"Health: {health}")
        if health <= 0:
            print("You died. Game over.")
            exit()
elif third == "cave":
    print("It's dark. Without a torch, you stumble and hurt yourself.")
    health -= 1
    print(f"Health: {health}")
    if health <= 0:
        print("You died. Game over.")
        exit()

# Final puzzle
print("You find a locked chest. It has a 3-digit code.")
code = str(random.randint(100, 999))
attempts = 3
while attempts > 0:
    guess = input(f"Enter the code ({attempts} attempts left): ")
    if guess == code:
        print("The chest opens! You found the treasure! 🎉")
        break
    else:
        print("Wrong code.")
        attempts -= 1
else:
    print("The chest locks forever. Game over.")