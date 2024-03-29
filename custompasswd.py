import string
import secrets
import sys

# Python 3.7 will stop getting security updates in June 2023. 
# 3.8, 3.9, 3.10, and 3.11 are available and you should
# upgrade if you are using 3.7 or below.

MIN_PYTHON_MAJOR_VERSION = 3
MIN_PYTHON_MINOR_VERSION = 10

# Check for Python 3 to support our usage of the print statement - 3.10 is arbitrary
if sys.version_info < (MIN_PYTHON_MAJOR_VERSION, MIN_PYTHON_MINOR_VERSION):
    raise Exception("This script uses features only available in Python 3.x or higher")

# This approach is taken from the Python documentation on "secrets"
# https://docs.python.org/3/library/secrets.html
# I often use it in stead of the native generator in my password manager.
additional_characters = ";?~_,%@#.$^-:"
alphabet = string.ascii_letters + string.digits + additional_characters
while True:
    password = ''.join(secrets.choice(alphabet) for i in range(14))
    if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and sum(c.isdigit() for c in password) >= 3):
        break
print(f"{password}")
