#!/usr/bin/python3

import sys

# Leap years occur every four years, with 
# exceptions for years divisible by 100 but not by 400. 
# The most recent leap years were 2020 and 2024, and 
# the next one will be in 2028
#
# Yes, maybe I could better emulate Falk Hüffner's work using
# the Python ctypes module...but it seemed like there was a material
# performance and simplicity hit.  I'll leave that to someone else.
# https://runebook.dev/en/articles/python/library/ctypes/ctypes.c_uint32


def is_leap_year(year: int) -> bool:
    # This is the standard way...
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def is_leap_year_fast(y: int) -> bool: 
    # This interesting function is based on a C function by Falk Hüffner. See:
    # https://hueffner.de/falk/blog/a-leap-year-check-in-three-instructions.html
    return ((y * 1073750999) & 3221352463) <= 126976


def main(num_args: int, usage: str):
    if len(sys.argv) != num_args:
        this_script = sys.argv[0]
        usage_message = usage.replace("script_name", str(this_script))
        print(usage_message)
        sys.exit(1)
    else:
        # use abs() to deal convert negative numbers to positive
        if int(sys.argv[1]) < 0:
            print(f"You entered a negative number.\nWe will convert it and check for leap.")
        print(f"\t{is_leap_year(abs(int(sys.argv[1])))}")
        print(f"\t{is_leap_year_fast(abs(int(sys.argv[1])))}")


if __name__ == '__main__':
    main(2, 'USAGE: python3 script_name <year_to_test, only use with positive numbers>')
