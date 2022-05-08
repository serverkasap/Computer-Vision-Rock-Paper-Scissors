import random


def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])


def get_user_choice():
    user_choice = input("Please enter your choice: ")
    return user_choice
