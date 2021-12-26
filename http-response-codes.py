# Utility to spill http response codes
# I then grep for what I need.
import sys
from http import HTTPStatus

MIN_PYTHON_MAJOR_VERSION = 3
MIN_PYTHON_MINOR_VERSION = 6

# Check for Python 3 to support our usage of the print statement
if sys.version_info < (MIN_PYTHON_MAJOR_VERSION, MIN_PYTHON_MINOR_VERSION):
    raise Exception("This script uses features only available in Python 3.x or higher")

for response_code in list(HTTPStatus):
    print(f"{response_code.value} {response_code.phrase}, {response_code.description}")
