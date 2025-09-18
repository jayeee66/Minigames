import sys
from enum import Enum
from guess_number import guess_number
from rps import rps


def arcade(name):
    while True:
        print(f"{name}, welcome to the Arcade!\n")
        choice = input(
            "Choose a game:\n1 = Rock, Paper, Scissors\n2 = Guess My Number\nOr press 'x' to exit the Arcade\n"
        )
        if choice == "1":
            game = rps(name)
            game()
        elif choice == "2":
            game = guess_number(name)
            game()
        elif choice.lower() == "x":
            print("Exiting the Arcade. Goodbye!")
            sys.exit()
        else:
            print("Invalid input.")
            continue


if __name__ == "__main__":
    import argparse  # For command-line argument parsing

    parser = argparse.ArgumentParser(description="Arcade Game")
    parser.add_argument(
        "-n", "--name", type=str, required=True, help="Player's name"
    )  # Add the name argument
    args = parser.parse_args()
    play = arcade(args.name)
    play()
