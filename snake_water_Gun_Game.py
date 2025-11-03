"""1 is for snake
-1 is for water
0 is for gun
"""
import random

computer = random.choice([1, -1, 0])
your_choice = input("Enter your choice (s for snake, w for water, g for gun): ")
yourdict = {"s": 1, "w": -1, "g": 0}

you = yourdict.get(your_choice)

if you is None:
    print("Invalid input")
elif computer == 1 and you == -1:
    print("Snake drinks water,you_lose.")
elif computer == 1 and you == 0:
    print("Gun kills the snake,you_win.")
elif computer == 1 and you == 1:
    print("Game tie.")
elif computer == -1 and you == -1:
    print("Game tie.")
elif computer == -1 and you == 0:
    print("Water douses gun, computer wins.")
elif computer == -1 and you == 1:
    print("Snake drinks water, you win.")
elif computer == 0 and you == -1:
    print("Water douses gun, you win.")
elif computer == 0 and you == 0:
    print("Game tie.")
elif computer == 0 and you == 1:
    print("Gun kills snake, you win.")
else:
    print("Something went wrong.")
