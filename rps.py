import sys
import random
from enum import Enum


def rps(name="Player1"):
    game_count = 0
    player_wins = 0
    computer_wins = 0

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal computer_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        player = input(f"{name}, enter your choice (1: Rock, 2: Paper, 3: Scissors): ")
        if player not in ["1", "2", "3"]:
            print(f"{name}, invalid choice. Please enter 1, 2, or 3.")
            return play_rps()
        player = int(player)

        computer = int(random.choice("123"))
        print("")
        print(f"\n {name} choice: {RPS(player).name}")
        print(f"computer choice: {RPS(computer).name}")

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins  # Track player wins, nested function inside another function
            nonlocal computer_wins  # Track computer wins, nested function inside another function
            if player == computer:
                return "It's a tie!"
            elif (
                (player == 1 and computer == 3)
                or (player == 2 and computer == 1)
                or (player == 3 and computer == 2)
            ):
                player_wins += 1
                return f"{name} wins!"

            else:
                computer_wins += 1
                return f"Computer wins!\n Sorry, {name}..."

        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame count: {game_count}")
        print(f"\n{name}'s wins: {player_wins}")
        print(f"\nComputer wins: {computer_wins}")

        while True:
            playagain = input("Play again?\n y for yes\n q for quit: ")
            if playagain.lower() not in ["y", "q"]:
                print("Invalid input.")
                continue
            else:
                break
        if playagain.lower() == "y":
            return play_rps()
        else:
            print("Thanks for playing!")
            return

    return play_rps


if __name__ == "__main__":
    import argparse  # For command-line argument parsing

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )  # Create the parser

    parser.add_argument(
        "-n",
        "--name",
        metavar="name",
        required=True,
        help="The name of the person playing the game.",
    )

    args = parser.parse_args()  # Parse the arguments

    rock_paper_scissors = rps(args.name)  # Create a closure

    rock_paper_scissors()  # Start the game
