"""Snake, Water, Gun: a small command-line game against the computer.

Rules: snake drinks water, water douses gun, gun kills snake.
"""
import random

CHOICES = {"s": "snake", "w": "water", "g": "gun"}
# Each key beats its value.
BEATS = {"snake": "water", "water": "gun", "gun": "snake"}
VERBS = {"snake": "drinks", "water": "douses", "gun": "kills"}


def decide(player, computer):
    """Return 'tie', 'player' or 'computer'."""
    if player == computer:
        return "tie"
    return "player" if BEATS[player] == computer else "computer"


def play_round():
    answer = input("Enter your choice (s = snake, w = water, g = gun): ").strip().lower()
    if answer not in CHOICES:
        print("Invalid input. Please enter s, w or g.")
        return
    player = CHOICES[answer]
    computer = random.choice(list(CHOICES.values()))
    print(f"You chose {player}, the computer chose {computer}.")
    result = decide(player, computer)
    if result == "tie":
        print("Game tie.")
    elif result == "player":
        print(f"{player.capitalize()} {VERBS[player]} {computer}. You win!")
    else:
        print(f"{computer.capitalize()} {VERBS[computer]} {player}. Computer wins.")


def main():
    while True:
        play_round()
        if input("Play again? (y/n): ").strip().lower() != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
