# Simple terminal game in Python

import random
import sys

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        import time
        time.sleep(0.1)

def start_game():
    print_slow("Welcome to the Simple Terminal Game!\n")
    print_slow("In this game, you will play against the computer.\n")
    print_slow("The goal is to guess a number between 1 and 10.\n")
    print_slow("Let's begin!\n")

    computer_number = random.randint(1, 10)
    player_guess = int(input("Enter your guess: "))

    while player_guess != computer_number:
        if player_guess > computer_number:
            print_slow("Too high! Try again.\n")
        else:
            print_slow("Too low! Try again.\n")
        player_guess = int(input("Enter your guess: "))

    print_slow("You won! The number was " + str(computer_number) + ".\n")
    play_again = input("Do you want to play again (y/n)? ")
    if play_again == 'y':
        start_game()
    else:
        print_slow("Thank you for playing!\n")
        sys.exit()

start_game()
