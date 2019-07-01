from random import randint
from time import sleep

"""this program is going to play
a game where the user guesses the 
sum of the dice roll"""


def get_user_guess():
    guess = int(raw_input("Guess a number: "))
    return guess


def roll_dice(number_of_sides):
    first_roll = randint(1, number_of_sides)
    second_roll = randint(1, number_of_sides)
    max_val = number_of_sides * 2
    print("The maximum possible value is: %d") % max_val
    guess = get_user_guess()
    if guess > max_val:
        print("Invalid input")
    else:
        print("Rolling...")
        sleep(2)
        print("%d") % first_roll
        sleep(1)
        print("%d") % second_roll
        total_roll = first_roll + second_roll
        print("Total roll is: %d") % total_roll
        print("Result...")
        sleep(1)
        if guess == total_roll:
            print("You win!")
        else:
            print("You lose!")


roll_dice(6)
