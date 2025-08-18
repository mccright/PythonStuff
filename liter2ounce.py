#!/usr/bin/python3

import sys

# Ounces to Liters and Liters to Ounces conversion formulas
#
# Liters = ounces / 33.814
# Ounces = liters * 33.814

def l2o(f_value):
    liters = float(f_value)
    ounces = (liters * 33.814)
    return ounces


def main(num_args: int, usage: str):
    if len(sys.argv) != num_args:
        this_script = sys.argv[0]
        usage_message = usage.replace("script_name", str(this_script))
        print(usage_message)
        sys.exit(1)
    else:
        print(f"{l2o(sys.argv[1]):.2f}")


if __name__ == '__main__':
    main(2, 'USAGE: python3 script_name <volume_in_ounces>')
