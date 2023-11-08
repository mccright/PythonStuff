#!/usr/bin/env python3
#
# Return a terse weather report using data from an api.openweathermap.org service.

import os
import sys
import datetime
import configparser
import json
import requests


# Get value from a config file: https://github.com/mccright/PythonStuff/blob/main/otherNotes.md#get-values-from-a-config-file

def get_config(filename, section, val):
    config = configparser.ConfigParser()
    config.read([filename])
    # create an object for a specific config file section
    weather = config[section]
    # now get the values from that object
    return weather.get(val)


# Thank you Matt Arderne at https://gist.github.com/RobertSudwarts/acf8df23a16afdb5837f?permalink_comment_id=3769668#gistcomment-3769668 
# for the calculate_bearing(d) function  

def calculate_bearing(d):
    dirs = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
    ix = int(round(d / (360. / len(dirs))))
    return dirs[ix % len(dirs)]


if __name__ == '__main__':
  
    try:
        owmtoken = get_config('weather.ini', 'weather', 'owmtokenA')
        # os.environ['WEATHER1'] # os.getenv('WEATHER1', default=None)
        # print(f"{owmtoken}")
        cityname = input("City Name: ")
        cityname = cityname + str(",us")
        url = (f"https://api.openweathermap.org/data/2.5/weather?appid={owmtoken}&lang=en&units=imperial&q={cityname}")
        response = requests.get(url)
        jsonstr = json.loads(response.text)
        posixdt = datetime.datetime.fromtimestamp(int(jsonstr['dt']))
        reporttime = datetime.date.strftime(posixdt, "%Y-%m-%M %R")
        winddir = calculate_bearing(jsonstr['wind']['deg'])
        print(f"{reporttime}, {jsonstr['main']['temp']}°F, feels like {jsonstr['main']['feels_like']}°F, wind {winddir} {jsonstr['wind']['speed']} m/h, {jsonstr['weather'][0]['description']}, humidity {jsonstr['main']['humidity']}%")

    except Exception as e:
        print("Failed this run. Error: {} -- {}".format(e, (sys.exc_info())))

