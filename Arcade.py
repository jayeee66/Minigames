import sys
from enum import Enum
import guess_number
import rps


def arcade(name):
    def choose_game():
        nonlocal name
        print(f"{name}, welcome to the Arcade!\n")
        choice = input(
            "Choose a game:\n1 = Rock, Paper, Scissors\n2 = Guess My Number\nOr press 'x' to exit the Arcade\n"
        )
        if choice.lower() not in ["1", "2", "x"]:
            print("Invalid input.")
            return choose_game()
        if choice == "1":
            game = rps.rps(name)
            game()
        elif choice == "2":
            game = guess_number.guess_number(name)
            game()
        else:
            print("Exiting the Arcade. Goodbye!")
            sys.exit()

    return choose_game


if __name__ == "__main__":
    import argparse  # For command-line argument parsing

    parser = argparse.ArgumentParser(description="Arcade Game")
    parser.add_argument(
        "-n", "--name", type=str, required=True, help="Player's name"
    )  # Add the name argument
    args = parser.parse_args()
    play = arcade(args.name)
    play()
