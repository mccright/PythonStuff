#!/usr/bin/python3

import sys

# Celsius To Fahrenheit and Fahrenheit to Celsius conversion formulas
#
# Celsius = (Fahrenheit – 32) * 5/9
# Fahrenheit = (Celsius * 9/5) + 32

def f2c(f_value):
    fahrenheit = float(f_value)
    celsius = (fahrenheit - 32) * 5/9
    return celsius


def main(num_args: int, usage: str):
    if len(sys.argv) != num_args:
        this_script = sys.argv[0]
        usage_message = usage.replace("script_name", str(this_script))
        print(usage_message)
        sys.exit(1)
    else:
        print(f"{f2c(sys.argv[1]):.2f}")


if __name__ == '__main__':
    main(2, 'USAGE: python3 script_name <temp_in_fahrenheit>')
