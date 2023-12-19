#!/usr/bin/env python3
#
# Return a terse weather report using data from an api.openweathermap.org service.
# Examples:
#  matt@hostname:/testing/$ python3 weather.py
#  2023-12-23 13:23, 42.51°F, feels like 34.74°F, wind S 16.11 m/h, broken clouds, humidity 40%
#
#  matt@hostname:/testing/$ python3 weather.py -c denver
#  2023-12-10 13:10, 62.85°F, feels like 59.83°F, wind SSW 2.71 m/h, clear sky, humidity 21%
#
#  matt@hostname:/testing/$ python3 weather.py -c chicago -n us -f weather.ini
#  2023-12-29 13:29, 31.6°F, feels like 22.51°F, wind SSW 11.5 m/h, scattered clouds, humidity 49%
#
#  matt@hostname:/testing/$ python3 weather.py -c rome -n it
#  2023-12-30 13:30, 49.57°F, feels like 48.79°F, wind SSE 3.44 m/h, clear sky, humidity 62%
#
#  matt@hostname:/testing/$ python3 weather.py -h
#  usage: weather [-h] [-d] [-c CITY_NAME] [-n NATION_NAME] [-f CONFIG_FILE_NAME]
#  
#  weather: a terminal script to fetch current weather from openweathermap.org
#  
#  optional arguments:
#    -h, --help            show this help message and exit
#    -d, --debug           Use to send debug logging to console
#    -c CITY_NAME, --city_name CITY_NAME
#                          Either collect the target city name. Or just use the default city name.
#    -n NATION_NAME, --nation_name NATION_NAME
#                          Either collect the target nation name. Or just use the default country name
#    -f CONFIG_FILE_NAME, --config_file_name CONFIG_FILE_NAME
#                          Name of the configuration file.

import os
import argparse
import sys
import datetime
import configparser
import json
import requests

# Set some defaults
DEFAULT_CITY_NAME="urbandale"
DEFAULT_COUNTRY_NAME="us"
DEFAULT_CONFIG_FILE="weather.ini"

# Get value from a config file: https://github.com/mccright/PythonStuff/blob/main/otherNotes.md#get-values-from-a-config-file
def get_config(filename, section, val):
    config = configparser.ConfigParser()
    config.read([filename])
    # create an object for a specific config file section
    weather = config[section]
    # now get the values from that object
    return weather.get(val)


# set up the parser
parser = argparse.ArgumentParser(
    prog="weather",
    description="weather: a terminal script to fetch current weather from openweathermap.org")

# add all the arguments
parser.add_argument(
    "-d", "--debug",
    required=False,
    default="False",
    action='store_true',
    help="Use to send debug logging to console")

parser.add_argument(
    # Either collect the target city name. Or just use the default city name.
    "-c", "--city_name",
    required=False,
    default=DEFAULT_CITY_NAME,
    # type=ascii,
    action='store',
    help="Either collect the target city name.\nOr just use the default city name.")

parser.add_argument(
    # Either collect the target nation/country name. Or just use the default country name.
    "-n", "--nation_name",
    required=False,
    default=DEFAULT_COUNTRY_NAME,
    # type=ascii,
    action='store',
    help="Either collect the target nation name.\nOr just use the default country name")

parser.add_argument(
    "-f", "--config_file_name",
    required=False,
    default=DEFAULT_CONFIG_FILE,
    # type=ascii,
    action='store',
    help="Name of the configuration file.")

arglist = parser.parse_args()


# Thank you Matt Arderne at https://gist.github.com/RobertSudwarts/acf8df23a16afdb5837f?permalink_comment_id=3769668#gistcomment-3769668 
# for the calculate_bearing(d) function  

def calculate_bearing(d):
    dirs = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
    ix = int(round(d / (360. / len(dirs))))
    return dirs[ix % len(dirs)]
 

if __name__ == '__main__':
  
    try:
        try:
            OWMTOKEN = get_config(arglist.config_file_name, 'weather', 'owmtokenA')
        except Exception as e:
            print("Failure getting config file content. Error: {} -- {}".format(e, (sys.exc_info())))
            exit()
        # os.environ['WEATHER1'] # os.getenv('WEATHER1', default=None)
        try:
            cityname = arglist.city_name
            citynation = cityname + str("," + arglist.nation_name)
        except Exception as e:
            print("Failure getting input or Improper input. Error: {} -- {}".format(e, (sys.exc_info())))
            exit()
        url = (f"https://api.openweathermap.org/data/2.5/weather?appid={OWMTOKEN}&lang=en&units=imperial&q={citynation}")
        # print(f"{url}")
        try:
            response = requests.get(url)
        except requests.exceptions.Timeout as e:
            # ToDo: add retry code/loop
            print(f"Failed with timeout this run.")
            raise SystemExit(e)
        except requests.exceptions.TooManyRedirects as e:
            # Wrong URL?
            print(f"Failed with TooManyRedirects this run. Is the URL correct?: {url}")
            raise SystemExit(e)
        except requests.exceptions.RequestException as e:
        # Some other error -- little chance to recover. bail.
            print(f"Failed with TooManyRedirects this run.")
            raise SystemExit(e)
        jsonstr = json.loads(response.text)
        #print(f"{jsonstr}")
        posixdt = datetime.datetime.fromtimestamp(int(jsonstr['dt']))
        reporttime = datetime.date.strftime(posixdt, "%Y-%m-%M %R")
        winddir = calculate_bearing(jsonstr['wind']['deg'])
        print(f"{reporttime}, {jsonstr['main']['temp']}°F, feels like {jsonstr['main']['feels_like']}°F, wind {winddir} {jsonstr['wind']['speed']} m/h, {jsonstr['weather'][0]['description']}, humidity {jsonstr['main']['humidity']}%")

    except Exception as e:
        print("Failed this run. Error: {} -- {}".format(e, (sys.exc_info())))

