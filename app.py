from random import *

game_min_number = 1
game_max_number = 100
game_lives = 10
winning_number = randint(game_min_number, game_max_number)
global_user_input = 0
lives_left = game_lives
guessed_numbers = []

messages = {
                "welcome": "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n******* Welcome to the worlds best game *******",
                "aim_of_game": "- The goal is to guess the number created by the computer",
                "configure_settings": "- Do you want to configure game settings or stick to the defautl?\n- Press 'y' to stick to customize settings or 'n' to stick to default\n:",
                "enter_min_number": "What do you want the 'MIN' number to be?\n:",
                "enter_max_number": "What do you want the 'MAX' number to be?\n:",
                "warning_number": "You have to print number\n",
                "warning_character": "\nYou have to print either 'y' or 'n'",
                "warning_number_used": "You have already guessed this number",
                "warning_number_out_of_bounds": "Number is not between games minimum or maximum number",
                "default_settings": "\n\n\n        Starting with default settings\n",
                "confirmation_of_settings": "\n\n\n             Settings have been set\n",
                "enter_lives": "How many lives do you want?\n:"
            }

def query_and_get_lives_left_plural():
    if (lives_left == 1): return "life"
    else: return "lives"

def print_lives_left():
    print(str(lives_left) + " " + query_and_get_lives_left_plural() + " left\n")

def print_winning_message():
    print("You win with " + str(lives_left) + " " + query_and_get_lives_left_plural() + " left\n")

def print_hint(user_input):
    if (user_input < winning_number): print("Number is Higher")
    else: print("Number is Lower")

def prompt_desired_settings():
    global winning_number

    global game_min_number
    input_min = ""
    while (input_min.isdigit() == False):
        try:
            input_min = int(input(messages["enter_min_number"]))
            break
        except ValueError:
            print(messages["warning_number"])
    game_min_number = input_min

    global game_max_number
    input_max = ""
    while (input_max.isdigit() == False):
        try:
            input_max = int(input(messages["enter_max_number"]))
            break
        except ValueError:
            print(messages["warning_number"])
    game_max_number = input_max

    global lives_left
    input_lives = ""
    while (input_lives.isdigit() == False):
        try:
            input_lives = int(input(messages['enter_lives']))
            break
        except ValueError:
            print(messages["warning_number"])
    lives_left = input_lives

    winning_number = randint(game_min_number, game_max_number)
    print(messages["confirmation_of_settings"])

def prompt_game_settings():
    is_default = ""
    while(is_default != "y" or is_default != "n"):
        is_default = input(messages["configure_settings"])
        if (is_default.lower() == "y"):
            prompt_desired_settings()
            break
        elif (is_default.lower() == "n"):
            print(messages["default_settings"])
            break
        else:
            print(messages["warning_character"])

def number_has_been_used(input):
    for i in guessed_numbers:
        if i == input:
            return True

def numbe_is_out_of_bounds(input):
    if (input < game_min_number or input > game_max_number):
        return True

def start_game():
    global global_user_input
    global winning_number
    global lives_left

    print(messages["welcome"])
    print(messages["aim_of_game"])
    prompt_game_settings()
    print("       You have been gifted with " + str(lives_left) + " lives\n")

    while (global_user_input != winning_number and lives_left > 0):
        try:

            user_input = int(input("Enter a number between " + str(game_min_number) + " and " + str(game_max_number) + ", or press ctrl + c to exit\n:"))
            if (user_input == winning_number):
                print_winning_message()
                guessed_numbers.append(user_input)
                break
            elif (lives_left == 1):
                print("Game Over! The number was " + str(winning_number))
                guessed_numbers.append(user_input)
                lives_left -=1
            elif (number_has_been_used(user_input)):
                print(messages["warning_number_used"])
                print_hint(user_input)
            elif (numbe_is_out_of_bounds(user_input)):
                print(messages["warning_number_out_of_bounds"])
                print_hint(user_input)
            else:
                print_hint(user_input)
                lives_left -= 1
                guessed_numbers.append(user_input)

            global_user_input = user_input
            print_lives_left()

        except ValueError:
            print(messages["warning_number"])
            continue

def review_game_stats():
    print("\n\n\n\n\n******* Review you stats *******")

start_game()
review_game_stats()

# TODO
# Review stats
# Levels?
# minus
# Games?