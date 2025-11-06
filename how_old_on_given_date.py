import os
import sys
from datetime import *
from dateutil.relativedelta import *
from dateutil.tz import *
import calendar

# experimenting again with dateutil.relativedelta():
# https://dateutil.readthedocs.io/en/stable/index.html

# This function started with code from:
# https://levlaz.org/pretty-print-relative-dates-in-python/
# I later received a question about "how old was <indiviual-in-question> 
# on a specific date?" and added the ability to specify a given date.
# There is nothing special about "birthdate," it can be any starting date.
def yourageattarget(birthyear: int, birthmonth: int, birthday: int, targetyear: int, targetmonth: int, targetday: int):
    """
    Description: Calculate the difference between input 
    birthdate and a given date
    Input: int birthyear, int birthmonth, int birthday, int targetyear, int targetmonth, int targetday.
    Output: a string with diff in years months days.
    """
    try:
        rd = relativedelta(datetime(int(targetyear), int(targetmonth), int(targetday)), datetime(int(birthyear), int(birthmonth), int(birthday)) )
        years = f'{rd.years} years, ' if rd.years > 0 else ''
        months = f'{rd.months} months, ' if rd.months > 0 else ''
        days = f'{rd.days} days' if rd.days > 0 else ''
    except Exception as e:
        print(f"Exception doing relativedelta(): {e}")
        sys.exit()
    if f'{years}{months}{days}' == '':
        print("Your input for birthdate cannot be today or in the future.")
        print(f"Try again with <birthmonth> <birthday> <birthyear> <targetmonth> <targetday> <targetyear> on the command line.")
        sys.exit()
    else:
        return f'{years}{months}{days}'


def check_input(inputs: list) -> tuple:
    if len(inputs) != 7:
        print(f"Not enough arguments.\n Need <birthmonth> <birthday> <birthyear> <targetmonth> <targetday> <targetyear> on the command line.")
        sys.exit(0)

    if all(elements.isnumeric() for elements in (inputs[1:])) != True:
        print(f"Some input was not numeric.\n Need <birthmonth> <birthday> <birthyear> <targetmonth> <targetday> <targetyear> on the command line.")
        sys.exit(0)

    if (int(inputs[1]) <= 12 and int(inputs[4]) <= 12):
       # Do nothing. Month is valid.
        birthmonth = int(inputs[1])
        targetmonth = int(inputs[4])
    else:
        print("Invalid month. Your input for birthmonth was not between 1 and 12.")
        print(f"Need <birthmonth> <birthday> <birthyear> <targetmonth> <targetday> <targetyear> on the command line.")
        sys.exit(0)

    if (int(inputs[2]) <= 31 and int(inputs[5]) <= 31):
       # Do nothing. Gross day validation is OK.
        birthday = int(inputs[2])
        targetday = int(inputs[5])
    else:
        print("Invalid day. Your input for birthday was not between 1 and 31.")
        print(f"Need <birthmonth> <birthday> <birthyear> <targetmonth> <targetday> <targetyear> on the command line.")
        sys.exit(0)

    if (len(inputs[3]) == 4 and len(inputs[6]) == 4):
        birthyear = inputs[3]
        targetyear = inputs[6]
    else:
        print("Invalid year length. \nYour input for birthyear was not 4 digits long.")
        print(f"Need <birthmonth> <birthday> <birthyear> <targetmonth> <targetday> <targetyear> on the command line.")
        sys.exit(0)

    return birthyear, birthmonth, birthday, targetyear, targetmonth, targetday


if __name__ == '__main__':
    inputs: list = sys.argv
    # Validate the input
    birthyear, birthmonth, birthday, targetyear, targetmonth, targetday = check_input(inputs)

    # birthhour = sys.argv[4]
    print(f"                    ---------------------------")
    print(f"birthmonth = {birthmonth}, birthday = {birthday}, birthyear = {birthyear}\r\ntargetmonth = {targetmonth}, targetday = {targetday}, targetyear = {targetyear}")
    print(f"                    ---------------------------")
    print(f"Given that input -> {yourageattarget(int(birthyear), int(birthmonth), int(birthday), int(targetyear), int(targetmonth), int(targetday))} old.")
    print(f"                    ---------------------------")

