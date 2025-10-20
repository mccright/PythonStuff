#!/usr/bin/python3

import sys

# cups to Liters and Liters to cups conversion formulas
#
# Liters = cups / 4.226753
# cups = liters * 4.226753

def c2l(f_value) -> float:
    cups = float(f_value)
    liters: float = (cups / 4.226753)
    return liters


def main(num_args: int, usage: str):
    if len(sys.argv) != num_args:
        this_script = sys.argv[0]
        usage_message = usage.replace("script_name", str(this_script))
        print(usage_message)
        sys.exit(1)
    else:
        print(f"{c2l(sys.argv[1]):.2f}")


if __name__ == '__main__':
    inputs_4_usage_msg = '<volume_in_cups>'
    usage_msg = f"USAGE: python3 script_name {inputs_4_usage_msg}"
    main(2, usage_msg)
