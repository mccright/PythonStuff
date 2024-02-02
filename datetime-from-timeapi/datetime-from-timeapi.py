#!/usr/bin/python
# -*- coding: utf-8 -*-
# This is just some problem-solving for an unrelated project.
# This code started with https://github.com/veebch/clock/blob/main/webtime.py.
# Thank you veebch (https://fosstodon.org/@veeb)
#
# Look into how we might help simplify this exercise:
# Read: "Ten Python datetime pitfalls, and what libraries are \
# (not) doing about it." By Arie Bovenberg
# https://dev.arie.bovenberg.net/blog/python-datetime-pitfalls/

import time
import requests

# This URL will return my time via my time zone.  
# If you need a variable other than 'timezone' see:
# https://timeapi.io/swagger/index.html
# TimeZones are: https://en.wikipedia.org/wiki/Tz_database and see a list at: 
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
time_url = "https://timeapi.io/api/TimeZone/zone?timeZone=America/Chicago"   

def get_timeapi_time(time_url):
    response = requests.get(time_url)    
    parsed = response.json()
    # "currentLocalTime" is string($date-time)
    datetime_str = str(parsed["currentLocalTime"])
    timezone_str = str(parsed["timeZone"])
    # print(datetime_str)
    year = (datetime_str[0:4])
    month = twodigits(int(datetime_str[5:7]))
    day = twodigits(int(datetime_str[8:10]))
    hour = twodigits(int(datetime_str[11:13]))
    minute = twodigits(int(datetime_str[14:16]))
    second = twodigits(int(datetime_str[17:19]))
    timefrominternet = (year,
                    month,
                    day,
                    hour,
                    minute,
                    second,
                    timezone_str)
    # print(str(timefrominternet))
    return timefrominternet


# Takes a single digit integer and turns it into a two digit string
# (or a two digit number and does nothing to it).
def twodigits(digit):     
    digitstring=str(digit)        
    if len(digitstring)==1:
        digitstring= "0"+digitstring
    return digitstring

def cleanuptime(timefromtime):
    splittime=timefromtime.split(':')
    timefromtimehour=int(splittime[0])
    timefromtimemin=int(splittime[1])
    timefromtimesecs=int(splittime[2])
    cleaneduptime= twodigits(timefromtimehour) + ":" + twodigits(timefromtimemin) + ":" + twodigits(timefromtimesecs)
    # print(cleaneduptime)
    return cleaneduptime


# Not used yet...
def writestringtofile(stringforfile):
    internalstring = str(stringforfile)
    try:
        file = open ("file.txt", "w+")  # write to file, even if it doesn't exist
        file.write(internalstring)
        file.close()
    except:  # open failed
        print('cannot open file')
    return


if __name__ == '__main__':
    # print("Local time is:")
    # localtimestring=str(time.localtime()[3])+':'+str(time.localtime()[4])+':'+str(time.localtime()[5]) # Get the current time string from the rtc
    # print(f"{cleanuptime(localtimestring)}")
    # print(time.gmtime())
    # print('getting time from the internet')
    timefromtimeapi = get_timeapi_time(time_url)
    print(f"{timefromtimeapi[0]}-{timefromtimeapi[1]}-{timefromtimeapi[2]}  {timefromtimeapi[3]}:{timefromtimeapi[4]}:{timefromtimeapi[5]}  tz: {timefromtimeapi[6]}")




