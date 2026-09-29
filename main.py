# day 1 on 20th july 2026
#
# def greet(name):
#
#     print(f"Hello {name} I am coming home,")
#     print("and will be staying for a while")
#
# greet("Dad")
# import math
# def greet_with(name, location):
#     print(f"Hello there {name}")
#     print(f"You must be from {location}")
#
# greet_with(location="Keringet", name="Riodes")
#
# def calculate_love_score(name1, name2):
#     combined_names = (name1 + name2).lower()
#     t = combined_names.count("t")
#     r = combined_names.count("r")
#     u = combined_names.count("u")
#     e = combined_names.count("e")
#
#     total = t + r + u + e
#
#     l = combined_names.count("l")
#     o = combined_names.count("o")
#     v = combined_names.count("v")
#     e = combined_names.count("e")
#
#     total_love = l + o + v + e
#
#     love_score = str(total) + str(total_love)
#     print(f"Your love score is {love_score}%")
#
#
# calculate_love_score("Riodes Kipkirui", "Ebby Chepkorir")

# def caesar_cipher(text, shift):
#     result = ""
#     shift = shift % 26
#
#     for char in text:
#         if char.isupper():
#             new_char = chr((ord(char) - 65 + shift) % 26 + 65)
#             result += new_char
#         elif char.islower():
#             new_char = chr((ord(char) - 97 + shift) % 26 + 97)
#             result += new_char
#         else:
#             result += char
#
#     return result
#
# secret_message = caesar_cipher("Hi there, did you get my message!", 5)
# print(secret_message)
#
# decoded_message = caesar_cipher(secret_message, -5)
# print(decoded_message)


# def encrypt(original_text, shift_num):
#     result = ""
#
#     for letter in original_text:
#         if letter in alphabet:
#             new_shift = alphabet.index(letter) + shift_num
#             new_shift = new_shift % 26
#             result += alphabet[new_shift]
#
#         else:
#             result += letter
#
#
#     print(f"Your new encrypted message is: {result} ")
#
#
# encrypt(original_text=text, shift_num=shift)
#
# new_message = input(print("Would you like to decrypt the message? "))


# import art
# print(art.logo)

# print("      ****WELCOME TO THE CAESAR CIPHER MESSANGER*****     ")
#
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
#             'v', 'w', 'x', 'y', 'z']
#
# def caesar_cipher(result, shift_num, encode_or_decode):
#     original_text = ""
#
#     if direction == "decode":
#         shift_num *= -1
#
#     for letter in result:
#
#         if letter not in alphabet:
#             original_text += letter
#
#         else:
#             new_shift = alphabet.index(letter) + shift_num
#             new_shift %= len(alphabet)
#             original_text += alphabet[new_shift]
#     print(f"Your new {encode_or_decode}d message is: {original_text}")
#
#
# should_continue = True
#
# while should_continue:
#
#     direction = (input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")).lower()
#     text = input("Please input your text here: \n").lower()
#     shift = int(input("What is the shift number for your text?: \n"))
#
#
#     caesar_cipher(result=text, shift_num=shift, encode_or_decode=direction)
#
#     restart = input("Type 'yes' to continue or 'no' to stop.\n").lower()
#     if restart == 'no':
#         should_continue = False
#         print("Goodbye")

#
# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }
#
# student_grades = {}
# for student in student_scores:
#     score = student_scores[student]
#     if score >= 91:
#         student_grades[student] = 'Outstanding'
#     elif score >= 81:
#         student_grades[student] = 'Exceeds Expectations'
#     elif score >= 71:
#         student_grades[student] = 'Acceptable'
#     else:
#         student_grades[student] = 'Fail'
#
# print(student_grades)
#
# nested_list = ["a", "b", ["ab", "bs"]]
# print(nested_list[2][1])

# travel_log = {
#     "France": {
#         "cities_visited": ["Paris", "Lille", "Metz"],
#         "total_visits": 15
#     },
#     "England": {
#         "cities_visited": ["London", "Manchester", "Birmingham"],
#         "total_visits": 30
#     },
# }
# print(travel_log["England"]["cities_visited"][2])
#
# print("***WELCOME TO THE SILENT BIDDING CONTEST***")
#
# def find_highest_bidder(bidding_dictionary):
#     winner = ""
#     highest_bid = 0
#     for bidder in bidding_dictionary:
#         bid_amount = bidding_dictionary[bidder]
#         if bid_amount > highest_bid:
#             highest_bid = bid_amount
#             winner = bidder
#
#
#     print(f"The winner is: {winner} with a bid of: ${highest_bid}")
#
#
# bids = {}
# bidding = True
# while bidding:
#     name = input("What is your name?: ")
#     bid = int(input("How much are you willing to bid?: $"))
#     bids[name] = bid
#     any_more = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
#     if any_more == "no":
#         bidding = False
#         find_highest_bidder(bids)
#     elif any_more == "yes":
#         print("\n" * 50)
#
#
#

# def format_name(f_name, l_name):
#     print(f_name.title() + l_name.title())
#
#
# format_name("rIodes", "kipKIRui")

# def is_leap_year(year):
#     year = int(year)
#     if year % 4 and year % 400 or year % 100 == 0:
#         return f"The year {year} is a leap year"
#     elif year % 100 and year % 400 == 0:
#         return f"The year {year} is a leap year"
#     else:
#         return f"The year {year} is not leap year"
#
#
# output = is_leap_year(input("Which year would you like to check: "))
# print(output)

# def is_leap_year(year):
#     year = int(year)
#     if year % 4 == 0 and year % 400 == 0:
#         return True
#     elif year % 100 == 0 and year % 400 == 0:
#         return True
#     else:
#         return False
#
#
# output = is_leap_year(input("Which year would you like to check: "))
# print(output)
#
# def is_leap_year(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False


# def add(n1, n2):
#     return n1 + n2
#
#
# def subtract(n1, n2):
#     return n1 - n2
#
#
# def multiply(n1, n2):
#     return n1 * n2
#
#
# def divide(n1, n2):
#     return n1 / n2
#
#
# print(add(2, multiply(5, divide(8, 4))))

# def outer_function(a, b):
#     def inner_function(c, d):
#         return c + d
#
#     return inner_function(a, b)
#
#
# result = outer_function(5, 10)
# print(result)

# def my_function(a):
#     if a < 40:
#         return
#         print("Terrible")
#     if a < 80:
#         return "Pass"
#     else:
#         return "Great"
# print(my_function(25))

# print("""
#                                     ****WELCOME TO MY CALCULATOR****
#
#      _____________________
#     |  _________________  |
#     | | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------.
#     | |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
#     |  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
#     | | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
#     | |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
#     | | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
#     | |___|___|___| |___| | | |  \ '.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ '.___.'\  | |
#     | | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
#     | |___|___|___| |___| | | |              | || |              | || |              | || |              | |
#     | | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
#     | |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------'
#     |_____________________|
#
# """)
#
# def all_ops():
#     x = float(input("Please input the first number: "))
#     print(" +\n -\n *\n /")
#     operator = input("Choose an operator: ")
#     y = float(input("Please input the second number: "))
#
#     def add(n1, n2):
#         return n1 + n2
#
#
#     def subtract(n1, n2):
#         return n1 - n2
#
#
#     def multiply(n1, n2):
#         return n1 * n2
#
#
#     def divide(n1, n2):
#         return n1 / n2
#
#
#     calculation = {
#         "+": add,
#         "-": subtract,
#         "*": multiply,
#         "/": divide,
#     }
#
#     output = calculation[operator](x, y)
#     print(f"{x} {operator} {y} = {output}")
#
#
# all_ops()
#
#
# continue_calc = True
# while continue_calc:
#     cont = input("Type 'yes' to continue or 'no' to stop and exit the calculator : ").lower()
#     if cont == 'yes':
#         print(all_ops())
#     elif cont == 'no':
#         continue_calc = False
#     else:
#         print("Please input a valid response!!")
#
#


# play_now = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

# def add(n1, n2):
#     return n1 + n2
#
#
# first_card = random.choice(cards)
# print(first_card)
#
# def blackjack_game():
#     for card in cards:
#         card_no = random.choice(cards)
#         if play_now == 'y':
#
#             print(f"[{card_no}] [{first_card + card_no}])
#             if card_no + first_card <= 21:
#                 print()
#
#         elif
#
#
#
# blackjack = True
# while blackjack:

# def calc_user_score():
#     user_cards.append(deal_cards())
#     return sum(user_cards)
#
#
# print(f"[{calc_user_score()}]")
#
#
# def calc_comp_score():
#     comp_cards.append(deal_cards())
#     return sum(comp_cards)
#
#
# print(f"[{calc_comp_score()}]")

#
# logo = ("""                 **** WELCOME TO MY NEW BLACKJACK GAME ****
#
#                 .------.            _     _            _    _            _
#                 |A_  _ |.          | |   | |          | |  (_)          | |
#                 |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
#                 | \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
#                 |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <__
#                 '-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\__/
#                       |  \/ K|                            _/ |
#                       '------'                           |__/
#     """)
#
# import random
#
#
# def deal_cards():
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     card = random.choice(cards)
#     return card
#
#
# def calc_score(cards):
#     if sum(cards) == 21 and len(cards) == 2:
#         return 0
#
#     if 11 in cards and sum(cards) > 21:
#         cards.remove(11)
#         cards.append(1)
#
#     return sum(cards)
#
# def compare(u_score, c_score):
#     if u_score == c_score:
#         return "DRAW"
#     elif c_score == 0:
#         return "Lose, opponent has a Blackjack"
#     elif u_score > 21:
#         return "You went over, You lose"
#     elif c_score > 21:
#         return "Opponent went over, You win"
#     elif u_score > c_score:
#         return "You win"
#     else:
#         return "you lose"
#
#
# def play_game():
#     print(logo)
#     user_cards = []
#     comp_cards = []
#     comp_score = -1
#     user_score = -1
#
#     is_game_over = False
#
#     for _ in range(2):
#         user_cards.append(deal_cards())
#         comp_cards.append(deal_cards())
#
#     while not is_game_over:
#         user_score = calc_score(user_cards)
#         comp_score = calc_score(comp_cards)
#
#         print(f"Your cards: {user_cards} and your current score is: {user_score}")
#         print(f"Comp's first card: {comp_cards[0]}")
#
#         if user_score == 0 or comp_score == 0 or user_score > 21:
#             is_game_over = True
#         else:
#             play_now = input("Would you like to continue game of Blackjack? Type 'y' to continue or 'n' to pass: ")
#             if play_now == 'y':
#                 user_cards.append(deal_cards())
#
#             else:
#                 is_game_over = True
#
#     while comp_score != 0 and comp_score < 17:
#         comp_cards.append(deal_cards())
#         comp_score = calc_score(comp_cards)
#
#     print(f"Your final hand was: {user_cards}, final score: {user_score}")
#     print(f"Comp's last hand was: {comp_cards}, final score: {comp_score}")
#     print(compare(user_score, comp_score))
#
# while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
#    print("\n" * 25)
#    play_game()
#
#

# import math
#
#
# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(math.isqrt(num)) + 1):
#         if num % i == 0:
#             return False
#     return True
#
#
# is_prime(num=int(input("Please input the number you would like to check: ")))
#
#
#
# num_logo = ("""
#                                  ****WELCOME TO THE NUMBER GUESSING GAME****
#                ___                         _____                    __                __
#               / _ \_   _  ___  ___ ___    /__   \ |__   ___      /\ \ \_   _ _ __ ___ | |__   ___ _ __
#              / /_\/ | | |/ _ \/ __/ __|    / /\/ '_ \ / _ \    /  \/ / | | | '_ ' _ \| '_ \ / _ \ '__|
#             / /_\\| |_| |  __/\__ \__ \    / /  | | | |  __/   / /\  /| |_| | | | | | | |_) |  __/ |
#             \____/ \__,_|\___||___/___/   \/   |_| |_|\___|   \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|
#
# """)
#
# import random
#
#
# EASY_TURNS = 10
# HARD_TURNS = 5
#
# def calc_difficulty():
#     level_choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
#     if level_choice == 'easy':
#         return EASY_TURNS
#     elif level_choice == 'hard':
#         return HARD_TURNS
#
#
# def check_no(num_choice, actual_answer, turns):
#     """checks number against num_choice, returns the number of turns remaining.
#     :rtype: object
#     """
#     if num_choice > actual_answer:
#         print("Too high!, try again.")
#         return turns - 1
#     elif num_choice < actual_answer:
#         print("Too low!, try again.")
#         return turns - 1
#     elif num_choice == actual_answer:
#         print(f"You win! the number was: {actual_answer}")
#
#
# def game():
#     print(num_logo)
#     print("I am thinking of a number between 1 and 100 ")
#
#     number = random.randint(1, 100)
#     print(f"pssst!! the number is: {number}.")
#
#
#     turns = calc_difficulty()
#
#
#     num_choice = 0
#     while num_choice != number:
#         print(f"You have {turns}, turns to find the number.")
#         num_choice = int(input("Make a guess: "))
#         turns = check_no(num_choice, number, turns)
#         if turns == 0:
#             print("You've run out of guesses. YOU LOSE!!")
#             return
#
# game()


# degugging

# def my_function():
#     for i in range(1, 21):
#         if i == 20:
#             print("This is your code.")
#
#
# my_function()
#
# from random import randint
#
# dice_images = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣"]
# dice_num = randint(0, 5)
# print(dice_images[dice_num])

#
# year = int(input("What's your birth year?: "))
#
# if year > 1980 and year <= 1994:
#         print("You are a millenial.")
#
# elif year > 1994:
#     print("You are a Gen-Z.")
#
# try:
#     age = int(input("Please input your age here: "))
# except ValueError:
#     print("Invalid input!!, try again with a numerical format like 18.")
#     age = int(input("Please input your age here: "))
#
# print(f"You are eligible to drive at the age: {age}.")
#
# word_per_page = ""
# pages = int(input("Number of pages from the book: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(f"The total number of words in the book is: {total_words}")

#
# import random
#
#
# def add(n1, n2):
#     return n1 + n2
#
#
# def mutate(a_list):
#     b_list = []
#     new_item = 0
#     for item in a_list:
#         new_item = item * 2
#         new_item += random.randint(1, 3)
#         new_item = add(new_item, item)
#         b_list.append(new_item)
#     print(b_list)
#
#
# mutate([1, 2, 3, 5, 8, 13])

# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
#
#
# is_leap(year=input("Please put your year here: "))

# import random
#
# # Sample Dataset: Celebs/Entities with their follower counts (in millions)
#
# logo_2 = """
#                       --- WELCOME TO THE HIGHER OR LOWER GAME ---
#
#                             __  ___       __
#                            / / / (_)___ _/ /_  ___  _____
#                           / /_/ / / __ '/ __ \/ _ \/ ___/
#                          / __  / / /_/ / / / /  __/ /
#                         /_/ ///_/\__, /_/ /_/\___/_/
#                            / /  /____/_      _____  _____
#                           / /   / __ \ | /| / / _ \/ ___/
#                          / /___/ /_/ / |/ |/ /  __/ /
#                         /_____/\____/|__/|__/\___/_/
#
# """
#
# mini_logo = """
#      _    __
# #     | |  / /____
# #     | | / / ___/
# #     | |/ (__  )
# #     |___/____(_)
# #
# # """
# #
# print(logo_2)
# print(mini_logo)
#
# DATA = [
#     {"name": "Cristiano Ronaldo",
#      "value": 630,
#      "description": "Footballer",
#      "country": "Portugal"},
#     {"name": "Lionel Messi",
#      "value": 500,
#      "description": "Footballer",
#      "country": "Argentina"},
#     {"name": "Selena Gomez",
#      "value": 420,
#      "description": "Musician and Actress",
#      "country": "United States"},
#     {"name": "Kylie Jenner",
#      "value": 390,
#      "description": "Reality TV Star & Businesswoman",
#      "country": "United States"},
#     {"name": "Dwayne Johnson",
#      "value": 380,
#      "description": "Actor and Wrestler",
#      "country": "United States"},
#     {"name": "Ariana Grande",
#      "value": 370,
#      "description": "Musician",
#      "country": "United States"},
#     {"name": "Kim Kardashian",
#      "value": 360,
#      "description": "Reality TV Star",
#      "country": "United States"},
#     {"name": "Beyoncé",
#      "value": 310,
#      "description": "Musician",
#      "country": "United States"},
#     {"name": "Taylor Swift",
#      "value": 280,
#      "description": "Musician",
#      "country": "United States"},
#     {"name": "National Geographic",
#      "value": 280,
#      "description": "Magazine/Media",
#      "country": "United States"},
# ]
#
#
# def format_data(account):
#     """Takes an account dictionary and returns printable string format."""
#     name = account["name"]
#     description = account["description"]
#     country = account["country"]
#     return f"{name}, a {description} from {country}."
#
#
# def check_answer(guess, a_value, b_value):
#     """
#     Takes the user's guess and follower counts,
#     returns True if they got it right, or False if wrong.
#     """
#     if a_value > b_value:
#         return guess == "a"
#     else:
#         return guess == "b"
#
# print(logo_2)
# def play_game():
#     score = 0
#     continue_playing = True
#
#     account_a = random.choice(DATA)
#     account_b = random.choice(DATA)
#
#     a_value = account_a["value"]
#     b_value = account_b["value"]
#
#     while continue_playing:
#         if account_a == account_b:
#             account_b = random.choice(DATA)
#
#         print(f"\nCompare A: {format_data(account_a)}")
#         print(mini_logo)
#         print(f"Against B: {format_data(account_b)}")
#
#         guess = input("Type 'A' for lower or 'B' for higher,Who do you think has more followers?:").lower()
#
#         print("\n" * 30)
#         print(logo_2)
#
#         while guess not in ["a", "b"]:
#             guess = input("Please input a valid response!!, try again:")
#
#         correct_answer = check_answer(guess, a_value, b_value)
#         if correct_answer:
#             score += 1
#             print(f"That's correct! your score is now : {score}")
#             account_a = account_b
#             account_b = random.choice(DATA)
#
#         else:
#             correct_answer = False
#             print(f"Wrong answer,GAME OVER YOU LOST!! Final score is: {score}")
#             return
#
# if __name__ == "__main__":
#     play_game()

# TODO: 1. prompt the user by asking what they would like.
# import math

# Coffee Menu Dictionary containing recipe requirements and prices
# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "milk": 200,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }
#
#
# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }
#
# money = 0.0
#
# #  TODO: 4. check if the resources are sufficient for the order.
#
#
# ordering_coffee = True
# while ordering_coffee:
#     order = input("Hello, what would you like to order today? ")
#     try:
#         if order == "off":
#             ordering_coffee = False
#             print("The machine is now turned off.")
#     except KeyError:
#         print("")
#
#     def place_order():
#         cost = MENU[order]["cost"]
#         print(f"Your order will cost: ${cost}")
#         water_amt = MENU[order]["ingredients"]["water"]
#         milk_amt = MENU[order]["ingredients"]["milk"]
#         coffee_amt = MENU[order]["ingredients"]["coffee"]
#
#         #  TODO: 2. turn off the coffee machine if the user enters off to the prompt.
#
#         #  TODO: 3. print a report on the remaining resources used to make the coffee.
#
#         water = resources["water"]
#         milk = resources["milk"]
#         coffee = resources["coffee"]
#
#         pennies_tally = float(input("How many pennies do you have?"))
#         nickles_tally = float(input("How many nickles do you have?"))
#         dimes_tally = float(input("How many dimes do you have?"))
#         quarters_tally = float(input("How many quarters do you have?"))
#
#         def calc_resources():
#             av_water = int(water - water_amt)
#             av_milk = int(milk - milk_amt)
#             av_coffee = int(coffee - coffee_amt)
#             if av_water < 0:
#                 return "Not enough water in store."
#             if av_milk < 0:
#                 return "not enough milk in store."
#             if av_coffee < 0:
#                 return "Not enough coffee in store."
#             else:
#                 return f"water: {av_water}ml\nmilk: {av_milk}ml\nmilk: {av_coffee}g money: ${cost}"
#
#         calc_resources()
#
#
#         #  TODO: 5. process the coins and ensure they are enough to complete the purchase of the order.
#
#         #  TODO: 6. check the transaction and ensure it's successfull.
#         #           if the user inserted too much money, the machine should offer change.
#
#         #  TODO: 7. make the order(coffee)
#         #             if transaction is a success do this;
#         #                     display  report before and after the order then
#         #                             print here's your order, Enjoy
#
#         def calc_cost():
#             cost1 = pennies_tally * 0.01
#             cost2 = nickles_tally * 0.05
#             cost3 = dimes_tally * 0.10
#             cost4 = quarters_tally * 0.25
#             total_cost = float(cost1 + cost2 + cost3 + cost4)
#
#             if total_cost < cost:
#                 print("Insufficient amount to purchase the order 😞😞.")
#                 return
#             elif total_cost > cost:
#                 change = round(total_cost - cost, 2)
#                 print(f"Here's your change {change}")
#                 print(f"Here's your {order}, enjoy😊😊.")
#                 return
#             else:
#
#                 return
#         calc_cost()
#
#
#     place_order()
#
#
# # trial 2
#
# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }
#
# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }
#
# money = 0.0
#
#
# def print_report():
#     """TODO 3: Print a report of remaining resources and earnings."""
#     print(f"\n--- Resource Report ---")
#     print(f"Water: {resources['water']}ml")
#     print(f"Milk: {resources['milk']}ml")
#     print(f"Coffee: {resources['coffee']}g")
#     print(f"Money: ${money:.2f}")
#     print("-----------------------\n")
#
#
# def is_resource_sufficient(order_ingredients):
#     """TODO 4: Check if there are enough ingredients in stock."""
#     for item in order_ingredients:
#         if order_ingredients[item] > resources[item]:
#             print(f"Sorry, there is not enough {item}.")
#             return False
#     return True
#
#
# def process_coins():
#     """TODO 5: Calculate total value of coins inserted."""
#     print("Please insert coins.")
#     quarters = int(input("How many quarters? ")) * 0.25
#     dimes = int(input("How many dimes? ")) * 0.10
#     nickels = int(input("How many nickels? ")) * 0.05
#     pennies = int(input("How many pennies? ")) * 0.01
#     return quarters + dimes + nickels + pennies
#
#
# def make_coffee(drink_name, order_ingredients):
#     """TODO 7: Deduct ingredients from resources and serve coffee."""
#     for item in order_ingredients:
#         resources[item] -= order_ingredients[item]
#     print(f"Here is your {drink_name} ☕. Enjoy!")
#
#
# # Main Game Loop
# ordering_coffee = True
#
# while ordering_coffee:
#     user_action = input("What would you like? (espresso/latte/cappuccino): ").lower()
#
#     # TODO 2: Turn off machine
#     if user_action == "off":
#         ordering_coffee = False
#         print("Machine shutting down. Goodbye!")
#
#     # TODO 3: Print report
#     elif user_action == "report":
#         print_report()
#
#     # Handle drink orders
#     elif user_action in MENU:
#         drink = MENU[user_action]
#
#         # 1. Check if resources are sufficient
#         if is_resource_sufficient(drink["ingredients"]):
#
#             # 2. Process payment
#             payment = process_coins()
#             drink_cost = drink["cost"]
#
#             # TODO 6: Check transaction success
#             if payment >= drink_cost:
#                 change = round(payment - drink_cost, 2)
#                 if change > 0:
#                     print(f"Here is ${change} in change.")
#
#                 # Add drink cost to total machine earnings
#                 money += drink_cost
#
#                 # TODO 7: Make coffee and update inventory
#                 make_coffee(user_action, drink["ingredients"])
#             else:
#                 print("Sorry, that's not enough money. Money refunded.")
#     else:
#         print("Invalid option. Please choose a valid drink, 'report', or 'off'.")
#

# TODO 7: Switch to vscode for the current program in moringa scool coding IDE vscode and google colab
#
# name = input("What is your name: ")
# age = input("What is your age: ")
# country = input("What is your country: ")
# language = input("What is your favourite programming language: ")
# print(f"Hello, my name is {name} and I am {age} years old living in {country} and
# my favourite programming language is {language}.")
#
#
# num = int(input("Enter a number: "))
# num2 = int(input("Enter another number: "))
# print(f"The sum of the two numbers is {num + num2}.")
# diff = num - num2
# if diff < 0:
#   diff = diff * -1
# print(f"The difference of the two numbers is {diff}.")
# print(f"The product of the two numbers is {num * num2}.")
#
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print(f"{num} is an even number.")
# else:
#     print(f"{num} is an odd number.")
#
# num1 = (input("Enter a number: "))
# num2 = (input("Enter another number: "))
# if num1 > num2:
#     print(f"{num1} is bigger than {num2}.")
# elif num1 == num2:
#   print("Numbers are equal.")
# else:
#   print("num2 is bigger than num1")

# TODO: Continue with the 100 days of code.
#
# list = ["hbsabas", "bsudeiws", "aduybs"]
# list[-1]

# Initial contact list
# contact_list = [
#     ("Alice", 1234567890, "alice@email.com"),
#     ("Bob", 9876543210, "bob@email.com")
# ]
#
# # Adding a new contact
# new_contact = ("Charlie", 5555555555, "charlie@email.com")
# contact_list.append(new_contact)
#
# # Updating Bob's email address
# contact_list[1] = ("Bob", 9876543210, "bob@newemail.com")
# # print(contact_list)
#
# my_name = ("alex",)
# print(my_name)
# for letter in my_name:
#     if "x" in letter:
#       print(True)
#     else:
#       print(False)
# without_first = my_name[0][1:]
# print(without_first)
#
# import random
#
#
# player = int(input("Please choose 1, 2, or 3: "))
# playing = True
# while playing:
#     print("\n\t1: Rock")  # 1 = Rock
#     print("\t2: Paper")  # 2 = Paper
#     print("\t3: Scissors")  # 3 = Scissors
#
#     # Choose!
#     computer = random.randint(1, 3)
#
#     if player > 3:
#         player = int(input("Please choose 1, 2, or 3: "))
#     else:
#         print("Your choice was: ", player)
#         print("The computer chose: ", computer)
#
#     while player > 0 and player <= 3:
#
#         if player == 1 and computer == 2:
#             print("Computer Wins")
#             break
#         elif player == 1 and computer == 3:
#             print("Player Wins")
#             break
#         elif player == 2 and computer == 1:
#             print("Player Wins")
#             break
#         elif player == 2 and computer == 3:
#             print("Computer Wins")
#             break
#         elif player == 3 and computer == 1:
#             print("Computer Wins")
#             break
#         elif player == 3 and computer == 2:
#             print("Player Wins")
#             break
#         else:
#             print("Tie! No winner.")
#             break
#     break
#
#
# name = "Riodes"
# r = len(name)
# print(r)
# breakfast_text = "oats, banana, tea"
# breakfast = breakfast_text.split(", ")
# print(len(breakfast))
# lengths = [len(i) for i in breakfast]
# print(breakfast)
# print(lengths)
# for i in breakfast:
#   lengths = len(i)
# print(breakfast)
# print(lengths)
#
# numbers = [8, 6, 4, 2, 445, 434, 7821, 6321, 57, 98, 87]
# numbers.sort()
# print(numbers)
#
# course = "Data science"
# first_char = course[4]
# print(first_char)
#
# course = "Data science student in moringa school"
# first_char = course[-6:]
# print(first_char)
#

# TODO: Minimum password length
#
#
# logging_in = True
# while logging_in:
#     min_length = 8
#     # Get user input
#     password = input("Enter your password: ")
#
#     # Check password length
#     password_length = len(password)
#     if password_length < min_length:
#         print(f"Password is too short. Minimum length is {min_length} characters.")
#     else:
#         # Initialize tracking variables
#         has_uppercase = False
#         has_lowercase = False
#         has_number = False
#         has_symbol = False
#
#         # Validate character types
#         for char in password:
#             if char.isupper():
#                 has_uppercase = True
#             elif char.islower():
#                 has_lowercase = True
#             elif char.isdigit():
#                 has_number = True
#             elif not char.isalnum():  # Check for symbols (not alphanumeric)
#                 has_symbol = True
#
#         # Evaluate password strength
#         if has_uppercase and has_lowercase and has_number and has_symbol:
#             logging_in = False
#             print("Strong password! You're using a good mix of characters.")
#         else:
#             print("Password could be improved. Consider including:")
#             if not has_uppercase:
#                 print("- Uppercase letters (A-Z)")
#             if not has_lowercase:
#                 print("- Lowercase letters (a-z)")
#             if not has_number:
#                 print("- Numbers (0-9)")
#             if not has_symbol:
#                 print("- Symbols (e.g., !@#$%^&*)")
#
# subject_mark_math = int(input("Enter the marks for the subjects above:"))
# subject_mark_eng = int(input("Enter the marks for the subjects above:"))
# subject_mark_kisw = int(input("Enter the marks for the subjects above:"))
# subject_mark_phy = int(input("Enter the marks for the subjects above:"))
# subject_mark_bio = int(input("Enter the marks for the subjects above:"))
# subject_mark_Geo = int(input("Enter the marks for the subjects above:"))

#
# checking = True
#
# while checking:
#     subjects = ["Maths", "English", "Kiswahili", "Physics", "Biology", "Chemistry", "Geography", "Building_and_Construction "]
#     subject_marks = [0]
#
#     for subject in subjects:
#         subject_mark = float(input(f"Enter the marks for the subject {subject}:"))
#         if subject_mark >= 101 or subject_mark < 0:
#             print("Enter a valid subject mark")
#         subject_marks.append(subject_mark)
#
#     l_s_sci = min(subject_marks[3:6])
#     x = len(subject_marks)
#
#
#
#     grade = ""
#     def grading(result):
#         if result >= 70:
#             grade = "A"
#             print(f"Excellent!, You got an {grade}.")
#         elif result >= 60:
#             grade = "B"
#             print(f"Very Good!, You got a {grade}.")
#         elif result >= 50:
#             grade = "C"
#             print(f"Average!, You got a {grade}.")
#         elif result >= 40:
#             grade = "D"
#             print(f"Pass!, You got a {grade}.")
#         else:
#             grade = "E"
#             print(f"Fail!, You got an {grade}.")
#
#
#     result = sum(subject_marks) - (l_s_sci) / (x - 1)
#     # result = int(input("Enter your results here:"))
#
#     grading(result)


# 1. Map individual raw subject marks (0-100) to KNEC Grade & Points (1-12)
# def get_subject_points(mark):
#     if mark >= 80:
#         return "A", 12
#     elif mark >= 75:
#         return "A-", 11
#     elif mark >= 70:
#         return "B+", 10
#     elif mark >= 65:
#         return "B", 9
#     elif mark >= 60:
#         return "B-", 8
#     elif mark >= 55:
#         return "C+", 7
#     elif mark >= 50:
#         return "C", 6
#     elif mark >= 45:
#         return "C-", 5
#     elif mark >= 40:
#         return "D+", 4
#     elif mark >= 35:
#         return "D", 3
#     elif mark >= 30:
#         return "D-", 2
#     else:
#         return "E", 1


# # 2. Map the 7-subject average points (1.0 - 12.0) to the Mean Grade
# def get_mean_grade(mean_points):
#     rounded_points = round(mean_points)
#     grade_table = {
#         12: ("A", "Excellent!"),
#         11: ("A-", "Very Good!"),
#         10: ("B+", "Good!"),
#         9: ("B", "Above Average!"),
#         8: ("B-", "Average Plus!"),
#         7: ("C+", "Average (Direct University Degree Entry Qualifiers)!"),
#         6: ("C", "Satisfactory (Diploma Entry)!"),
#         5: ("C-", "Below Average (Diploma Entry)!"),
#         4: ("D+", "Weak (Certificate Entry)!"),
#         3: ("D", "Poor (Certificate Entry)!"),
#         2: ("D-", "Very Poor (Artisan Entry)!"),
#         1: ("E", "Fail (Artisan Entry)!"),
#     }
#     return grade_table.get(rounded_points, ("E", "Fail"))


# # 3. Main processing routine
# def calculate_kcse():
#     subjects = [
#         "Maths",
#         "English",
#         "Kiswahili",
#         "Physics",
#         "Biology",
#         "Chemistry",
#         "Geography",
#         "Building and Construction",
#     ]

#     scores = {}

#     # Input validation loop for each subject
#     for subject in subjects:
#         while True:
#             try:
#                 mark = float(input(f"Enter the marks for {subject} (0-100): "))
#                 if 0 <= mark <= 100:
#                     grade, points = get_subject_points(mark)
#                     scores[subject] = {"mark": mark, "grade": grade, "points": points}
#                     break
#                 else:
#                     print("Error: Marks must be between 0 and 100. Try again.")
#             except ValueError:
#                 print("Error: Please enter a valid numerical value.")

#     # Apply KNEC 7-Subject Selection Rules:
#     # Rule 1: Maths is compulsory
#     maths_pts = scores["Maths"]["points"]

#     # Rule 2: Best of English or Kiswahili
#     eng_pts = scores["English"]["points"]
#     kis_pts = scores["Kiswahili"]["points"]
#     best_lang_pts = max(eng_pts, kis_pts)
#     dropped_lang_pts = min(eng_pts, kis_pts)

#     # Rule 3: 5 next best subjects from all remaining subjects
#     # The pool includes: Sciences, Humanities, Technicals, AND the unselected language
#     other_points = [
#         scores["Physics"]["points"],
#         scores["Biology"]["points"],
#         scores["Chemistry"]["points"],
#         scores["Geography"]["points"],
#         scores["Building and Construction"]["points"],
#         dropped_lang_pts,
#     ]

#     # Sort descending and take top 5
#     other_points.sort(reverse=True)
#     top_5_other_pts = other_points[:5]

#     # Calculate Aggregate (out of 84) and Mean Points (out of 12)
#     selected_7_points = [maths_pts, best_lang_pts] + top_5_other_pts
#     aggregate_points = sum(selected_7_points)
#     mean_points = aggregate_points / 7.0

#     mean_grade, remark = get_mean_grade(mean_points)

#     # Display Results
#     print("\n" + "=" * 45)
#     print(f"{'KCSE CANDIDATE PERFORMANCE SUMMARY':^45}")
#     print("=" * 45)
#     for subj, data in scores.items():
#         print(
#             f"{subj:<28}: {data['mark']:>5.1f}%  | Grade: {data['grade']:<2} ({data['points']} pts)"
#         )

#     print("-" * 45)
#     print(f"Total Aggregate Points : {aggregate_points} / 84")
#     print(f"Mean Grade Points      : {mean_points:.2f} / 12.0")
#     print(f"Overall Mean Grade     : {mean_grade}")
#     print(f"Verdict                : {remark}")
#     print("=" * 45)


# if __name__ == "__main__":
#     calculate_kcse()
