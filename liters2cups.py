#!/usr/bin/python3

import sys

# cups to Liters and Liters to cups conversion formulas
#
# Liters = cups / 4.226753
# cups = liters * 4.226753

def c2l(f_value):
    liters = float(f_value)
    cups = (liters * 4.226753)
    return cups


def main(num_args: int, usage: str):
    if len(sys.argv) != num_args:
        this_script = sys.argv[0]
        usage_message = usage.replace("script_name", str(this_script))
        print(usage_message)
        sys.exit(1)
    else:
        print(f"{c2l(sys.argv[1]):.2f}")


if __name__ == '__main__':
    main(2, 'USAGE: python3 script_name <volume_in_ounces>')
