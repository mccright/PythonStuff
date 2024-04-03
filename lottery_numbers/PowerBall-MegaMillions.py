#!/usr/bin/env python3

"""
Powerball and Mega-Millions are played by selecting six numbers.  
Powerball:     Five numbers between 1-69 and one “Powerball” number between 1-26.  
Mega-Millions: Five numbers between 1-70 and one “Mega Ball” number between 1-25.  

See [Powerball](https://www.usamega.com/powerball/faq) and 
[Mega-Millions](https://www.usamega.com/mega-millions/faq)  

Each play is $2.00
REMEMBER: The odds are not in your favor. 
https://en.wikipedia.org/wiki/Powerball#Power_Play
https://en.wikipedia.org/wiki/Mega_Millions#Winning_and_probability

This script spits out sets of numbers matching the rules for these games.
It uses secrets to generate each set to maximize entropy (think 'random').  
No need to think about your numbers, nor worry about the Lottery empire
or someone else generating your numbers for you.  
"""
import argparse
import secrets
import sys

# The 'secrets' module arrived with Python 3.6.
# 3.8, 3.9, 3.10 and 3.11 are available, and you should
# upgrade if you are using 3.7 or below.

MIN_PYTHON_MAJOR_VER = 3
MIN_PYTHON_MINOR_VER = 7

PB_FIRST_FIVE_UNIVERSE = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                          16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                          29, 20, 31, 32, 33, 34, 35, 36, 37, 38, 39, 30, 41,
                          42, 43, 44, 45, 46, 47, 48, 49, 40, 51, 52, 53, 54,
                          55, 56, 57, 58, 59, 50, 61, 62, 63, 64, 65, 66, 67,
                          68, 69]
PB_POWERBALL_UNIVERSE = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
                         17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
MM_FIRST_FIVE_UNIVERSE = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                          16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                          29, 20, 31, 32, 33, 34, 35, 36, 37, 38, 39, 30, 41,
                          42, 43, 44, 45, 46, 47, 48, 49, 40, 51, 52, 53, 54,
                          55, 56, 57, 58, 59, 50, 61, 62, 63, 64, 65, 66, 67,
                          68, 69, 70]
MM_MEGABALL_UNIVERSE = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
                        17, 18, 19, 20, 21, 22, 23, 24, 25]
# Set the MAX_RUNS var to some sane maximum for your use case
MAX_RUNS: int = 30


def print_powerball_candidate(powerball_first_group: int, powerball_length: int):
    todays_powerball_bet: [] = select_some(PB_FIRST_FIVE_UNIVERSE, powerball_first_group)
    print(f"PowerBall: ", end="")
    print_items_sorted(todays_powerball_bet)
    print(f"+", end=" ")
    powerball_number: [] = select_some(PB_POWERBALL_UNIVERSE, powerball_length)
    print_items_sorted(powerball_number)
    print("")


def print_megamil_candidate(mega_ball_first_group: int, mega_ball_length: int):
    todays_mega_ball_bet: [] = select_some(MM_FIRST_FIVE_UNIVERSE, mega_ball_first_group)
    print(f"Mega-Ball: ", end="")
    print_items_sorted(todays_mega_ball_bet)
    print(f"+", end=" ")
    mega_ball_number: [] = select_some(MM_MEGABALL_UNIVERSE, mega_ball_length)
    print_items_sorted(mega_ball_number)
    print("")


def print_separator():
    print(f"- - - - - - - - - - - - - - -")


def select_some(the_group: [], num_to_get: int) -> []:
    match = False
    while match == False:
        secure_random = secrets.SystemRandom()
        # sample() eliminates duplicates
        # list_of_items = secure_random.sample(the_group, num_to_get)
        # choices() permits duplicates... not useful without checking
        list_of_items = secure_random.choices(the_group, k = num_to_get)
        # set() removes duplicates.
        if sorted(list_of_items) != sorted(list(set(list_of_items))):
            # print(f"Duplicates found in {sorted(list_of_items)} vs \
            # {sorted(list(set(list_of_items)))}!!!!!")
            # Generate another list_of_items, hopefully without duplicates
            continue
        else:
            match = True
    return list_of_items


def print_items(list_of_items: []):
    length_of_list = len(list_of_items) - 1
    int_i: int = 0
    while length_of_list >= int_i:
        print(f"{list_of_items[int_i]}", end=" ")
        int_i = int_i + 1


def print_items_sorted(list_of_items: []):
    length_of_list = len(list_of_items) - 1
    list_of_items_sorted = sorted(list_of_items)
    int_i: int = 0
    while length_of_list >= int_i:
        print(f"{list_of_items_sorted[int_i]}", end=" ")
        int_i = int_i + 1


def main():
    # Check for Python 3 - 3.6 is rqd for secrets module
    if sys.version_info < (MIN_PYTHON_MAJOR_VER, MIN_PYTHON_MINOR_VER):
        raise Exception("This script requires Python 3.6 or higher")

    # Thank you 'marshki' for this argparse idea/model 
    # https://github.com/marshki/PowerballPy/
    parser = argparse.ArgumentParser(description="Generate candidate \
    Powerball and Mega-Millions plays")
    parser.add_argument("-n", "--num_plays", type=int, default=1, \
    help="Generate this many candidate Powerball and Mega-Millions plays")

    args = parser.parse_args()

    try:
        if args.num_plays < 1 or args.num_plays > MAX_RUNS:
            raise argparse.ArgumentTypeError(f"Number of candidate plays \
must be a positive integer less than {MAX_RUNS}.")
    except argparse.ArgumentTypeError as error:
        parser.error(str(error))

    num_candidate_plays: int = args.num_plays
    counter: int = 1
    powerball_first_group = 5
    powerball_length = 1
    mega_ball_first_group = 5
    mega_ball_length = 1
    while num_candidate_plays >= counter:
        # This approach is taken from the Python documentation on "secrets"
        # https://docs.python.org/3/library/secrets.html

        print_powerball_candidate(powerball_first_group, powerball_length)
        print_megamil_candidate(mega_ball_first_group, mega_ball_length)
        print_separator()
        counter = counter + 1


if __name__ == '__main__':
    main()
