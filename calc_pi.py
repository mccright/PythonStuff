#!/usr/bin/env python3
# This model is from Mihalis Tsoukalos in LinuxFormat LXF226 Aug 2017, page 92
# with additions to enforce a maximum and provide feedback to the user.
#
import sys
from mpmath import mp

# Only calculate up to 65,536 digits pi.
# If you want more, change the number below.
max_len = 65536

if len(sys.argv) == 1:
    print(f"Not enough arguments. Need the desired precision on the command line.")
    sys.exit(0)
if sys.argv[1].isdigit():
    if int(sys.argv[1]) <= max_len:
        precision = sys.argv[1]
    else:
        print(f"Maximum pi precision is currently: {str(max_len)}, you entered {str(sys.argv[1])}")
        sys.exit()
else:
    print(f"You entered {str(sys.argv[1])}. \nThis script requires a positive number representing your desired precision. \nMaximum pi precision is currently: {str(max_len)}")
    sys.exit()
mp.dps = precision
print(f"{mp.pi}")

