# Utility to spill http response codes
# I then grep for what I need.
import sys
from http import HTTPStatus

# Python 3.7 will stop getting security updates in June 2023. 
# 3.8, 3.9, 3.10, and 3.11 are available and you should
# upgrade if you are using 3.7 or below.


MIN_PYTHON_MAJOR_VERSION = 3
MIN_PYTHON_MINOR_VERSION = 10

# Check for Python 3 to support our usage of the print statement
if sys.version_info < (MIN_PYTHON_MAJOR_VERSION, MIN_PYTHON_MINOR_VERSION):
    raise Exception("This script uses features only available in Python 3.x or higher")

for response_code in list(HTTPStatus):
    print(f"{response_code.value} {response_code.phrase}, {response_code.description}")
