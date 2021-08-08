import os
import sys
import json
import requests
from time import sleep

# This is just a reminder for me.  I did not create this idea.
# This is an idiom from ipinfo and in example code all over the Internet.

def main():
    #os.system('cls' if os.name == 'nt' else 'clear')
    try:
        ipaddress = input("ip address: ")
        sleep(1)
        url = "https://ipinfo.io/{}".format(ipaddress)
        response = requests.get(url)
        jsonstr=json.loads(response.text)
        print("IP\t\t: {}".format(jsonstr['ip']))
        print("Hostname\t: {}".format(jsonstr['hostname']))
        print("City\t\t: {}".format(jsonstr['city']))
        print("Region\t\t: {}".format(jsonstr['region']))
        print("Country\t\t: {}".format(jsonstr['country']))
        print("Postcode\t: {}".format(jsonstr['postal']))
        print("Timezone\t: {}".format(jsonstr['timezone']))
        print("Organization\t: {}".format(jsonstr['org']))
        print("Location\t: {}".format(jsonstr['loc']))
    except Exception as e:
        print("Failed this run. Error: {} -- {}".format(e, (sys.exc_info())))


def main_iterate():
    # os.system('cls' if os.name == 'nt' else 'clear')
    try:
        ipaddress = input("ip address: ")
        sleep(1)
        url = "https://ipinfo.io/{}".format(ipaddress)
        response = requests.get(url)
        json_str = json.loads(response.text)
        for key in json_str:
            print(key, ' = ', json_str[key])
    except Exception as e:
        print("Failed this run. Error: {} -- {}".format(e, (sys.exc_info())))
        exit()


if __name__ == "__main__":
    print("First, hard code specific key/value pairs.")
    main()
    print("Now, iterate through every key/value pair.")
    main_iterate()
