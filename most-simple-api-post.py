#!/usr/bin/env python
# NOTE: Model code for a one-off simplified http post to a simple API.
#       The most simple idiom of this category.
#       If used repeatedly, implement inputs and error handling.
#       Some APIs may also need to deal with paging of response data.
# USAGE: Copy and morph for your intended use case

import json
import requests

FIRST_VARIABLE = "" # Replace with what is needed for var 1
SECOND_VARIABLE = "" # Replace with what is needed for var 2

def do_the_thing():
    # Causes the action, gets the data, etc.
    # Documentation: https://the.documentation.host/dir/docfile

    header = { # Modify as needed
        "Content-Type": "application/json"
    }

    payload = { # Modify as needed
        "first_placeholder": FIRST_VARIABLE, 
        "second_placeholder": SECOND_VARIABLE 
    }
    try:
        response = requests.post('https://targetHost.targetDomain.dom/the/api', 
                            data=json.dumps(payload),
                            headers=header)
    except Exception as e:
        # use "e" for now, clean up, add safety later
        print(e)
    if response.json()["status"] == "success":
        print('Something relevant ')
    else:
        print(response.text) # print message if unsuccessful, might 
                             # need to safely ASCIIfy it first

if __name__ == '__main__':
    do_the_thing()
