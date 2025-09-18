import sys
import random


def guess_number(name):
    game_count = 0
    player_wins = 0

    def playing_guess_number():
        player = input(f"{name}, guess which number I'm thinking of... 1, 2 or 3.\n")
        AI = int(random.choice("123"))
        player = int(player)
        print("")
        nonlocal game_count
        nonlocal player_wins

        print(f"{name}, you chose {player}.")
        print(f"I was thinking about the number {AI}.\n")
        if player == AI:
            print(f"{name}, you win!")
            player_wins += 1
        else:
            print(f"Sorry, {name}. Better luck next time.")
        game_count += 1

        print(f"\nGame count: {game_count}")
        print(f"\n{name}'s wins: {player_wins}")
        print(f"\nYour winning percentage: {player_wins / game_count:.2%}")

        while True:
            playagain = input(f"Play again, {name}?\nY for Yes or\nQ to Quit\n")
            if playagain.lower() not in ["y", "q"]:
                print("Invalid input")
                continue
            else:
                break
        if playagain.lower() == "y":
            return playing_guess_number()
        else:
            print("Thank you for playing!")
            return

    return playing_guess_number


if __name__ == "__main__":
    import argparse  # For command-line argument parsing

    parser = argparse.ArgumentParser(description="Guess the Number Game")
    parser.add_argument(
        "-n", "--name", type=str, required=True, help="Player's name"
    )  # Add the name argument
    args = parser.parse_args()
    guess_my_number = guess_number(args.name)
    guess_my_number()
