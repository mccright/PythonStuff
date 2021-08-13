#!/usr/bin/env python3
import errno
import re
import sys
import time
from urllib.error import HTTPError
from urllib.error import URLError
from urllib.error import ContentTooShortError
from urllib import request
import random_user_agent
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem


# This is example code, waste no time here:
# 'url' below is the target url:
url = sys.argv[1]
# 'search' below is a string to check for on the target response:
search = sys.argv[2]

start = 0
end: time = 0
exitCode = 0


start = time.time()

# you can also import SoftwareEngine, HardwareType, SoftwareType, Popularity from random_user_agent.params
# you can also set number of user agents required by providing `limit` as parameter

software_names = [SoftwareName.CHROME.value]
operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]

user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)

# Get list of user agents.
user_agents = user_agent_rotator.get_user_agents()

# Get Random User Agent String.
user_agent = user_agent_rotator.get_random_user_agent()

req = request.Request(url)
req.add_header('User-Agent', user_agent)

# If you are going to be checking your logs at the target server
# get your external IP address:
external_ip = request.urlopen('http://ifconfig.me/ip').read()
print("External IP: " + str(external_ip))
# Print the user_agent string for debugging, or comment it out.
print(f"user_agent: {user_agent}")

try:
    page = request.urlopen(req).read().decode("utf8", 'ignore')
except HTTPError as e:
    print('HTTPError: ' + e.__str__())
    exitCode = errno.ENOENT
    exit(exitCode)
except ContentTooShortError as e:
    print('ContentTooShortError: ' + e.__str__())
    exitCode = errno.ENOENT
    exit(exitCode)
except URLError as e:
    print("URLError: " + e.__str__())
    exitCode = errno.ENOENT
    exit(exitCode)
except UnicodeEncodeError as e:
    print("UnicodeEncodeError: " +  e.__str__())
    exitCode = errno.ENOENT
    exit(exitCode)
except IOError as e:
    print("IOError: " + e.reason.decode("utf8", 'ignore'))
    exitCode = errno.ENOENT
    exit(exitCode)
except Exception as e:
    print("Exception: " + e.__cause__)
    exitCode = errno.ENOENT
    exit(exitCode)

end = time.time()

err = ''
exitCode = 0
matches = re.search(search, page)
if matches is None:
    err = "\nSearch string not found"
    exitCode = errno.ENOENT
else:
    print('Search regex found: ' + search)
print('Page loaded in {time}s.{error}'.format(time=round(end-start, 2), error=err))
