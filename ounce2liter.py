#!/usr/bin/python3

import sys

# Ounces to Liters and Liters to Ounces conversion formulas
#
# Liters = ounces / 33.814
# Ounces = liters * 33.814

def o2l(f_value):
    ounces = float(f_value)
    liters = (ounces / 33.814)
    return liters


def main(num_args: int, usage: str):
    if len(sys.argv) != num_args:
        this_script = sys.argv[0]
        usage_message = usage.replace("script_name", str(this_script))
        print(usage_message)
        sys.exit(1)
    else:
        print(f"{o2l(sys.argv[1]):.2f}")


if __name__ == '__main__':
    inputs_4_usage_msg = '<volume_in_ounces>'
    usage_msg = f"USAGE: python3 script_name {inputs_4_usage_msg}"
    main(2, usage_msg)
