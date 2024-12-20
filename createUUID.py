#!/usr/bin/env python3
import string
import sys
import uuid


# For a practical example using uuid4 to generate unique IDs for records in
# an SQLite database see:
# https://blog.devops.dev/unleashing-the-power-of-uuid-in-python-a-comprehensive-guide-440a42d7b520
# 
# For an example of testing the validity of a uuid see:
# https://www.geeksforgeeks.org/how-to-check-uuid-validity-in-python/

def build_string_with_uuid():
    # Build a uuid as specified in RFC 4122: https://datatracker.ietf.org/doc/html/rfc4122.html
    # This approach absolutely does NOT generate random strings because of the predictable dash chars.
    # Rather, it generates unique strings that can be used for a variety of purposes 
    # that some might think of as "random."
    # https://docs.python.org/3/library/uuid.html#uuid.UUID.is_safe
    # Python 3.7 or above for UUID.is_safe support
    # Some code from:
    # https://github.com/finos/htc-grid/blob/main/source/control_plane/python/lambda/submit_tasks/submit_tasks.py
    if sys.version_info < (3, 7):
        raise Exception("Use only with Python 3.7 or higher")
    utility_UUID = uuid.uuid4(),  # Unique-enough identifier
    return str(utility_UUID)

if __name__ == '__main__':
    # Experimenting with creating a 'unique' uuid strings, a common requirement. 
    # ...think, database keys, filenames, API tokens, session identifier and more
    print(f"{build_string_with_uuid()}")






