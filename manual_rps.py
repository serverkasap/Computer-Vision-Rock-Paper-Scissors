import random


def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])


def get_user_choice():
    user_choice = input("Please enter your choice: ")
    return user_choice.lower()


def get_winner(computer_choice, user_choice):
    if computer_choice == "rock":
        if user_choice == "rock":
            return "tie"
        elif user_choice == "paper":
            return "user"
        else:
            return "computer"

    if computer_choice == "paper":
        if user_choice == "rock":
            return "computer"
        elif user_choice == "paper":
            return "tie"
        else:
            return "user"

    if computer_choice == "scissors":
        if user_choice == "rock":
            return "user"
        elif user_choice == "paper":
            return "computer"
        else:
            return "tie"


def play():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()

    winner = get_winner(computer_choice, user_choice)

    print(f"The computer has chosen {computer_choice}.")

    if winner == "tie":
        print("There is no winner.")
    else:
        print(f"The winner is {winner}.")


if __name__ == '__main__':
    play()
