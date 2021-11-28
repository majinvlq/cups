"""Cup game. Players bet in which cup there is a ball."""
import random as rd
import os


def cls():
    """Clears the prompt screen."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def cups_printer(table: list):
    """
    Prints out the cups scheme.
    :param table: list - takes the current game board representation
    """
    patterns = ["   _    ", "  / \   ", " /   \  "]
    for i in patterns:
        print(i * 3)
    print(f"/  {table[0]}  \ " + f"/  {table[1]}  \ " + f"/  {table[2]}  \ ")


def game_starter(table: list):
    """
    Function to initiate the game.
    :param table: list - takes in the game board representation - positions
    :return bool
    """
    answers = ('Y', 'N')
    cups_printer(table)
    ans1 = ''
    status = True
    print("\nWelcome to the Cup Game!"
          "\nYou have to chose in which cup the ball is hidden.")
    while status:
        ans1 = str(input("\nDo you want to start? [Y/N]: "))
        if ans1.capitalize() not in answers:
            print("\nYou have to pick Y or N. Try again!")
        else:
            break
    if ans1.capitalize() == 'N':
        print("\nThanks, goodbye!")
        status = False
    else:
        status = True
    return status


def player_guess():
    """Asks for players choice from given range. Returns int as the choice."""
    while True:
        try:
            number = int(input("\nIn which cup there is a ball? [1/2/3]: "))
            if number not in range(1, 4):
                print("\nWrong choice. Pick 1, 2 or 3.")
            else:
                return number
        except ValueError:
            print("\nYour choice is incorrect. Pick 1, 2 or 3")


def result_check(choice: int, table: list):
    """Conditional statement which checks if game has been won or lost."""
    if table[choice-1] == 'O':
        cls()
        cups_printer(table)
        print("\nThis is correct! YOU HAVE WON!")
    else:
        cls()
        cups_printer(table)
        print("\nYOU WERE WRONG!")


def replay():
    """
    Asks for the decision if player continues or not.
    :return bool
    """
    answers = ('Y', 'N')
    end_game = True
    while True:
        answer = input("\nDo you want to play again? [Y/N]? ").capitalize()
        # check if answer is proper
        if answer not in answers:
            print("\nYou have to pick Y or N.")
        else:
            break

    # check if answer is Y, else concludes the game
    if answer != answers[0]:
        print("\nThanks, goodbye!")
        end_game = False

    return end_game


def main():
    """Main game script."""
    instruction_positions = ['1', '2', '3']
    positions = ['O', ' ', ' ']
    cls()
    game_on = game_starter(instruction_positions)
    while game_on:
        cls()
        game_board = positions
        rd.shuffle(game_board)
        cups_printer(instruction_positions)
        guess = player_guess()
        result_check(guess, game_board)
        game_on = replay()


if __name__ == "__main__":
    main()
