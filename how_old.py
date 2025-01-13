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
def youragenow(birthyear: int, birthmonth: int, birthday: int):
    # Description: Calculate the difference between input date and now.
    # Input: int birthyear, int birthmonth, int birthday.
    # Output: a string with diff in years months days.
    rd = relativedelta(datetime.now(), datetime(int(birthyear), int(birthmonth), int(birthday)) )
    years = f'{rd.years} years, ' if rd.years > 0 else ''
    months = f'{rd.months} months, ' if rd.months > 0 else ''
    days = f'{rd.days} days' if rd.days > 0 else ''
    return f'{years}{months}{days}'


if len(sys.argv) != 4:
    print(f"Not enough arguments.\n Need <birthyear> <birthmonth> <birthday> on the command line.")
    sys.exit(0)

birthyear = sys.argv[3]
birthmonth = sys.argv[1]
birthday = sys.argv[2]
# birthhour = sys.argv[4]
print(f"                    ---------------------------")
print(f"Given that input -> {youragenow(int(birthyear), int(birthmonth), int(birthday))} old.")
print(f"                    ---------------------------")


