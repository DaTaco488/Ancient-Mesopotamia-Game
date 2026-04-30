#Ancient Mesopotamia python program | Created by: DaTaco | Under the CC BY-NC-SA 4.0 license

import time
import random
import math

#starting variables

food = 150
water = 100
population = 50
year = 1

#opening message

print(f"Created by DaTaco | CC BY-NC-SA 4.0")

print(f"\nWelcome to the Ancient Mesopotamia resource game!")
print(f"You are the ruler of a growing civilization")
print(f"The job you must complete is to manage your resources the best you can for 20 years")

print(f"\n\nHOW TO PLAY: \nYou pick from options each turn. After each turn a year passes, your population increases or decrases, and your population uses resources. There also is a chance to have random events happen.")
print(f"\nOptions: Farm (gives you a random amount food based on population), Irrigate (gives you a random amount of water based on population), Do nothing (Quite literally does nothing)")

time.sleep(2)

#main while loop

while population > 0 and year < 21:
    print(f"\n--- Year {year} ---")
    print(f"Population: {population}")
    print(f"Food: {food}")
    print(f"Water: {water}")

    print("\nChoose an action:")
    print("1. Farm (gain food)")
    print("2. Build irrigation (gain water)")
    print("3. Do nothing")

    choice = input("> ")

    if choice == "1":
        gained = random.randint(population//4, math.floor(population*0.7))
        food += gained
        print(f"You harvested {gained} food.")
    elif choice == "2":
        gained = random.randint(population//4, math.floor(population*0.6))
        water += gained
        print(f"You improved irrigation and gained {gained} water.")
    elif choice == "3":
        print("You chose to rest.")
    else:
        print("Invalid input try again with a valid input")
        continue

    event = random.choice(["flood", "drought", "attack", "none", "none2", "none3"])

    #random event

    if event == "flood":
        loss = random.randint(10, 25)
        food -= loss
        print(f"Flood! You lost {loss} food.")
    elif event == "drought":
        loss = random.randint(10, 25)
        water -= loss
        print(f"Drought! You lost {loss} water.")
    elif event == "attack" and choice != 3:
        loss = random.randint(5, 10)
        population -= loss
        print(f"Attack! You lost {loss} people")

    # Population consumes resources
    food -= population // 3
    water -= population // 4
    print(f"\n{population//2} food was eaten, and {population//3} water was drank, leaving you with {food} food, and {water} water.")

    # Check survival
    if food <= 0:
        food = 0
        loss = random.randint(10, 15)
        population -= loss
        print(f"\nWarning! There is not enough food, people are starving. Population decreased by {loss}")
    if water <= 0:
        water = 0
        loss = random.randint(10, 15)
        population -= loss
        print(f"\nWarning! There is not enough water, people are dehydrated. Population decreased by {loss}")
    if population <= 0:
        population = 0
        break

    #population grow

    if population > 2 and population < 55:
        grow = math.floor(population * 0.05)
        if grow < 1:
            grow = random.randint(0,1)
        population += grow
        print(f"\nYour populaiton grew by {grow} people")

    year += 1

print(f"\nYour ending stats: Food {food}, Water {water}, Population {population}")

if population <= 0:
    print("\nEveryone is dead. Your civilization has collapsed. U gotta do it again")
    print("\nGame Over. You Lose :(")
else:
    print("\nGGz you win! :)")