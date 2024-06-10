"""
Your job is to complete the definitions of each function mentioned in the comments so that it achieves its indicated behavior.

Do not run this file directly.
Rather, call whichever functions defined in this file that you want to run from within the file named main.py and run that file directly.
"""

import random

import random

def get_random_int(min_val, max_val):
    """
    Returns a random integer between min_val and max_val (inclusive).
    
    Args:
        min_val (int): The minimum value for the random integer.
        max_val (int): The maximum value for the random integer.
        
    Returns:
        int: A random integer between min_val and max_val (inclusive).
    """
    return random.randint(min_val, max_val)

def get_guess(max_val):
    """
    Prompts the user to guess a random integer between 1 and max_val (inclusive).
    
    Args:
        max_val (int): The maximum value for the random integer.
        
    Returns:
        int or bool: -1 if the user's input is invalid, True if the user guesses correctly,
                     False if the user guesses incorrectly.
    """
    # Generate a random integer between 1 and max_val (inclusive)
    random_int = get_random_int(1, max_val)
    
    # Prompt the user to guess the random integer
    guess = input(f"Guess an integer between 1 and {max_val}: ")
    
    # Check if the user's input is a valid integer within the range
    try:
        guess_int = int(guess)
        if 1 <= guess_int <= max_val:
            # Compare the user's guess with the random integer
            if guess_int == random_int:
                return True
            else:
                return False
        else:
            # User's input is out of range
            return -1
    except ValueError:
        # User's input is not an integer
        return -1


def play_game():
    """
    Plays a game where the user guesses 4 random integers between 1 and 5.
    Prints the percentage of correct guesses at the end.
    """
    max_val = 5
    num_guesses = 4
    correct_guesses = 0

    for _ in range(num_guesses):
        guess_result = get_guess(max_val)

        if guess_result == -1:
            print("Invalid response!")
            return
        elif guess_result:
            print("Correct!")
            correct_guesses += 1
        else:
            print("Wrong!")

    success_rate = (correct_guesses / num_guesses) * 100
    print(f"You guessed {success_rate}% of the random numbers correctly.")
