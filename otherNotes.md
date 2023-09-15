# Short Reminders  

### Use Python f-strings  
[Python f-strings](https://fstring.help/)  

### Use sys.exit(), not exit() or quit()  
A call to [sys.exit()](https://docs.python.org/3/library/sys.html#sys.exit) is translated into an exception so that clean-up handlers ([finally](https://docs.python.org/3/reference/compound_stmts.html#finally) clauses of [try](https://docs.python.org/3/reference/compound_stmts.html#try) statements) can be executed, and so that a debugger can execute a script without running the risk of losing control. The [os._exit()](https://docs.python.org/3/library/os.html#os._exit) function can be used if it is absolutely positively necessary to exit immediately (for example, in the child process after a call to [os.fork()](https://docs.python.org/3/library/os.html#os.fork)).  
```python
    try:
        something = try_something_wrong(this_fails)
    except Exception as e:
        print(f"Handling an exception. Error: {e} -- {sys.exc_info()}")
        sys.exit()
```

[exit()](https://docs.python.org/2/library/constants.html#exit) and [quit()](https://docs.python.org/3/library/constants.html#quit) raise the SystemExit exception.  They exist to support interactive Python in the interpreter.  They rely the site module and should only be used in the interpreter and not in production code.  

See also: [https://docs.python.org/3/library/exceptions.html#SystemExit](https://docs.python.org/3/library/exceptions.html#SystemExit) and https://stackoverflow.com/questions/19747371/python-exit-commands-why-so-many-and-when-should-each-be-used/19747562#19747562  


### One-Liner to set up my virtual environment  
```bash
python3 -m virtualenv --python="$(command -v python3)" .env && 
  source .env/bin/activate && 
  python3 -m pip install --upgrade pip virtualenv && 
  python3 -m pip install --upgrade setuptools wheel && 
  python3 -m pip install -r requirements.txt 
```

### Exploring Python Classes Without IDE Magic  
If you are attempting to hack a change in an existing script in a remote server having a bare bones install, autocompletion and built in reflection are generally missing.  Don't forget about simple dir() to explore features in available classes.  It can save you a lot of time and frustration if you do not use a given component or builtin very often.  A simple listing of its features can help jog your memory.  

For example, we can explore requests urllib3 & exceptions:  
```python
>>> dir(requests)
['ConnectTimeout', 'ConnectionError', 'DependencyWarning', 'FileModeWarning', 'HTTPError', 'JSONDecodeError', 'NullHandler', 'PreparedRequest', 'ReadTimeout', 'Request', 'RequestException', 'RequestsDependencyWarning', 'Response', 'Session', 'Timeout', 'TooManyRedirects', 'URLRequired', '__author__', '__author_email__', '__build__', '__builtins__', '__cached__', '__cake__', '__copyright__', '__description__', '__doc__', '__file__', '__license__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__title__', '__url__', '__version__', '_check_cryptography', '_internal_utils', 'adapters', 'api', 'auth', 'certs', 'chardet_version', 'charset_normalizer_version', 'check_compatibility', 'codes', 'compat', 'cookies', 'delete', 'exceptions', 'get', 'head', 'hooks', 'logging', 'models', 'options', 'packages', 'patch', 'post', 'put', 'request', 'session', 'sessions', 'ssl', 'status_codes', 'structures', 'urllib3', 'utils', 'warnings']
>>> dir(requests.urllib3)
['HTTPConnectionPool', 'HTTPResponse', 'HTTPSConnectionPool', 'PoolManager', 'ProxyManager', 'Retry', 'Timeout', '__all__', '__author__', '__builtins__', '__cached__', '__doc__', '__file__', '__license__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_collections', 'absolute_import', 'add_stderr_logger', 'connection', 'connection_from_url', 'connectionpool', 'contrib', 'disable_warnings', 'encode_multipart_formdata', 'exceptions', 'fields', 'filepost', 'get_host', 'logging', 'make_headers', 'packages', 'poolmanager', 'proxy_from_url', 'request', 'response', 'util', 'warnings']
>>> dir(requests.exceptions)
['BaseHTTPError', 'ChunkedEncodingError', 'CompatJSONDecodeError', 'ConnectTimeout', 'ConnectionError', 'ContentDecodingError', 'FileModeWarning', 'HTTPError', 'InvalidHeader', 'InvalidJSONError', 'InvalidProxyURL', 'InvalidSchema', 'InvalidURL', 'JSONDecodeError', 'MissingSchema', 'ProxyError', 'ReadTimeout', 'RequestException', 'RequestsDependencyWarning', 'RequestsWarning', 'RetryError', 'SSLError', 'StreamConsumedError', 'Timeout', 'TooManyRedirects', 'URLRequired', 'UnrewindableBodyError', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
```  

In addition to the ```dir(class_name)``` approach, some classes have *special* features to spill some of their details.  For example, ```pytz``` has ```all_timezones``` and ```common_timezones```


### Simple/Abbreviated Timezone Handling  
// The model for this came from 
// https://medium.com/techtofreedom/5-levels-of-handling-date-and-time-in-python-46b601e47f65
```python
import datetime
import pytz

local = datetime.datetime.now()
print(local.strftime("%d/%m/%Y, %H:%M:%S"))
# 06/07/2022, 14:19:50

CHICAGO = pytz.timezone('America/Chicago')
datetime_CHICAGO = datetime.datetime.now(CHICAGO)
print(datetime_CHICAGO.strftime("%d/%m/%Y, %H:%M:%S"))
# 06/07/2022, 14:19:50

std_UTC = pytz.timezone('UTC')
datetime_UTC = datetime.datetime.now(std_UTC)
print(datetime_UTC.strftime("%d/%m/%Y, %H:%M:%S"))
# 06/07/2022, 19:19:50
```
or another approach for the same experiment:  
```python
from time import gmtime, localtime, strftime, tzset

myDateTime = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
syslogGmtime = strftime("%b %d %H:%M:%S", gmtime())
myLocalTime = strftime("%a, %d %b %Y %H:%M:%S %Z", localtime())
syslogLocaltime = strftime("%b %d %H:%M:%S %Z", localtime())
# Display the results for this experiment
print(f"gmtime function says:              {myDateTime}, GMT")
print(f"localtime function says:           {myLocalTime}")
print(f"syslog time format from gmtime:    {syslogGmtime}")
print(f"syslog time format from localtime: {syslogLocaltime}")
```


### Simple File Read-File Write-File and Patch-File Functions  
This approach is only a quick hack for problem-solving:  
```python
#!/usr/bin/env python3
# This is a fragment used in larger scripts to 
# change the contents of configuration files.
# From: https://github.com/adamrehn/ue4-docker/tree/master/ue4docker/dockerfiles/ue4-source/windows
import os
import re
import sys


def readFile(filename):
    with open(filename, "rb") as f:
        return f.read().decode("utf-8")


def writeFile(filename, data):
    with open(filename, "wb") as f:
        f.write(data.encode("utf-8"))


def patchFile(filename, original, replacement):
    contents = readFile(filename)
    patched = contents.replace(original, replacement)
    writeFile(filename, patched)
    

# This is just an example of how to approach using the patchFile function
if len(sys.argv) != 4:
    print(f"USAGE: python3 {sys.argv[0]} <filename> <existingString> <replacementString>")
    sys.exit(1)
else:
    filename = sys.argv[1]
    existing_string = sys.argv[2]
    replacement_string = sys.argv[3]
    patchFile(filename, existing_string, replacement_string)
```

### Get values from a config file  
Find/set config file location and name  
Then get several values:  
weather_host, timeout, temp_type, wind_speed_type  
Use: [https://docs.python.org/3/library/configparser.html](https://docs.python.org/3/library/configparser.html)  
Assume sample configuration file contents:  
```terminal
[weather]
weather_host: https://openweather.org/api/
timeout: 16
temp_type: F
wind_speed_type: mph
```
Here is a *simple* way to use it:  
```python
import configparser
config = configparser.ConfigParser()
# Probably need a function to safely identify if the 
# config file exists first...
# Simplistic: config.read('example.ini')
# or more realistic:
config.read([
        'example.ini',
        os.path.expanduser('~/example.ini'),
        os.path.join(os.getenv('APPDATA', ''), 'myApp', 'example.ini'),
    ])
# create a *weather* object for a specific config file section
weather = config['weather']
# now get the values from that object
weather_provider = weather.get('weather_host')
request_timeout = weather.getint('timeout')
temp_value_type = weather.get('temp_type')
wind_velocity_type = weather.get('wind_speed_type')
```

### Read lines in a way that is ready for pipelines  
Sophisticated or not, this seems like a common and useful idiom.  
Under many circumstances input/output sanity checking or other *safety* measures will be needed in that while loop.  
```python
import sys
# ...your functions
if __name__ == "__main__":
    line = sys.stdin.readline()
    while line:
        what_I_need = do_something_useful(line)
        # do whatever is needed, I'll just print
        print(f"{what_I_need}")
        # re-fill 'line'
        line = sys.stdin.readline()
```


### Simple interactions with CSV files  
The emphasis here is on "*simple*.  
You can get a lot done with only the csv module [https://docs.python.org/3/library/csv.html](https://docs.python.org/3/library/csv.html)  
Also see: [https://www.webcodegeeks.com/python/csv-processing-using-python/](https://www.webcodegeeks.com/python/csv-processing-using-python/) and  
[https://www.geeksforgeeks.org/working-csv-files-python/](https://www.geeksforgeeks.org/working-csv-files-python/)  
I find this is a useful idiom.  
As usual, there are many circumstances input/output sanity checking or other  
*safety* measures will be needed in the with and loops.  
```python
import csv
from typing import TextIO

csv_data_file = "mydata.csv"
csv_file: TextIO
with open(csv_data_file, 'r', newline='') as csv_file:
    csv_reader = csv.reader(csv_file, quotechar=':', delimiter=';')
    for row in csv_reader:
        if csv_reader.line_num != 0:
            for col in row:
                print(col, end="\t")
        print()
```
or print only specific columns
```python
import csv
from typing import TextIO

csv_data_file = "mydata.csv"
csv_file: TextIO
with open(csv_data_file, 'r', newline='') as csv_file:
    csv_reader = csv.reader(csv_file, quotechar=':', delimiter=';')
    for row in csv_reader:
        if csv_reader.line_num != 1:
            print(f"{row[0]} is {row[1]} years old")
```


### Compare Two Lists  
Identify which strings in list two are not already in list one:  
```python
def compare_lists(list_one_str_file_name, list_two_str_file_name):
    list_one_str_file = list_one_str_file_name
    list_one_str_list = []
    listonestrings = open(list_one_str_file, "r")
    list_one_str_list = listonestrings.readlines()
    print(f"There are {len(list_one_str_list)} strings in List One")

    list_two_str_file = list_two_str_file_name
    list_two_str_list = []
    otherusers = open(list_two_str_file, "r")
    list_two_str_list = otherusers.readlines()
    print(f"There are {len(list_two_str_list)} strings in List Two\n")

    for i in list_two_str_list:
        if i not in list_one_str_list:
            print(f"{i}")
            # The rest of this code requires additional 
            # logging & reporting functions
            logging.info(f"{i}")
            try:
                reportFile.write(f"{i}")
            except IOError as e:
                logging.critical('I/O error on write to file: ' + repr(e))
                logging.critical('Report file name: ' + repr(reportName))
                print('I/O error on write to file: ' + repr(e))
            except Exception:
                logging.critical('Unexpected error on write to file: ' + repr(e))
                logging.critical('Report file name: ' + repr(reportName))
                print("Unexpected error on write to file \'{0}\': {2}".format(reportName,sys.exc_info()[0]))
                raise
    print(f"{report_file_topic} Report Filename: {reportName}")
```


### Abstract common stuff: http headers reminder  
```python
""" Add headers that are commonly required for your operations."""
def _build_headers():
    headers = {
        'Content-Type': 'application/xml',
        'Accept': 'application/json'
    }
    return headers
```
Then here is a simplistic example of using them:
```python
def _get_endpoint_response(content, endpoint_url):
    data = content
    headers = _build_headers()
    response = requests.post(endpoint_url, data=data, headers=headers)
    endpoint_response = (json.dumps(response.json(), indent=4))
    return endpoint_response
```

### Get the default gateway interface  
Sometimes it is important to use the default gateway interface.  
Using the *correct* interface is important for some use cases.  
In some of those use cases, it is also important to know its IP address.  
Get the default interface:  
```python
import netifaces
def default_interface():
    """ Get default gateway interface.
    Some OSes return 127.0.0.1 when using
    socket.gethostbyname(socket.gethostname()),
    so we're attempting to get a kind of valid hostname here.
    FROM: https://github.com/nils-werner/zget/blob/crypto/zget/utils.py
    """
    try:
        return netifaces.gateways()['default'][netifaces.AF_INET][1]
    except KeyError:
        # Sometimes 'default' is empty but AF_INET exists alongside it
        return netifaces.gateways()[netifaces.AF_INET][0][1]
```
And then use that interface name to get its IP address:  
```python
import netifaces
def ip_addr(interface):
    """ Get IP address from interface.
    FROM: https://github.com/nils-werner/zget/blob/crypto/zget/utils.py
    """
    try:
        return netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['addr']
    except KeyError:
        raise InvalidInterface()
```


### Quietly delete a file
```python
def silentremove(filename):
    try:
        return os.remove(filename)
    except Exception:
        pass
```

### Get a password  
If you need to fetch a password from a live user  
```pwinput``` seems better than ```getpass```.  
```python
import pwinput
def getuserpassword():
    # Prompt the user for a password without echoing input 
    # while pushing a mask character in stead.  
    # Reference https://github.com/asweigart/pwinput
    try:
        password = pwinput.pwinput(mask='*', prompt='Enter your password: ')
    except Exception as error:
        print('getuserpassword() failed with: ', error)
    else:
        return password

# testing...
print(f"pw: {getuserpassword()}")
```

### Get a password - Edge Case  
Sometimes you are gathering the password to pass along  
to another process that needs to be successful -- as  
as downstream processes require that success.  
In that case, one approach is to have the user enter  
their password twice and match them...  
```python
def prompt_for_password(retry=None):
    """Prompt user for password if not provided so the 
    password doesn't show up in the bash history.
    """
    if not (hasattr(sys.stdin, 'isatty') and sys.stdin.isatty()):
        # There is no user here, so nothing to do
        return

    if not retry:
        while True:
            try:
                the_password = getpass.getpass('Password: ')
                return the_password
            except EOFError:
                return
    else:
                while True:
            try:
                the_password = getpass.getpass('Password: ')
                rep_passwd = getpass.getpass('Repeat the Password: ')
                if the_password == rep_passwd:
                    return the_password
            except EOFError:
                return

```
Also see "Secure Password Handling in Python" by Martin Heinz [https://martinheinz.dev/blog/59](https://martinheinz.dev/blog/59)  


### Abstract common stuff: json I/O  
```python
def decode_json(json_input):
    return json.loads(json_input)
```
and
```python
def encode_json(json_input):
    return json.dumps(json_input, allow_nan = False)
```


### Graph on the terminal when investigating and exploring  
* asciichart (simplistic) [https://github.com/cashlo/asciichart](https://github.com/cashlo/asciichart)  
* livechart (maybe) [https://github.com/greyltc-org/livechart](https://github.com/greyltc-org/livechart)  
* plotext [https://github.com/piccolomo/plotext](https://github.com/piccolomo/plotext)  
* plotille [https://github.com/tammoippen/plotille](https://github.com/tammoippen/plotille)  
* terminal-plot (for csv) [https://github.com/soraxas/terminal-plot](https://github.com/soraxas/terminal-plot)  
* termplotlib (works for me) [https://github.com/nschloe/termplotlib](https://github.com/nschloe/termplotlib)  
* tplot for creating text-based graphs -- for visualizing data to the terminal or log files. [https://github.com/JeroenDelcour/tplot](https://github.com/JeroenDelcour/tplot)  


### Graphing in general when investigating and exploring  
* "#04 | Data Visualization in Python." Using matplotlib, seaborn and plotly. [https://blog.resolvingpython.com/04-data-visualization-in-python](https://blog.resolvingpython.com/04-data-visualization-in-python)  
* "Three Solutions to ScatterPlot." [https://blog.resolvingpython.com/you-need-to-have-flexible-thinking-when-programming](https://blog.resolvingpython.com/you-need-to-have-flexible-thinking-when-programming)  
* "How to Analyze Data through Visualization -- Understand how Data Visualization can help to analyse patterns that may result in a Linear Regression model." [https://blog.resolvingpython.com/how-to-analyze-data-through-visualization](https://blog.resolvingpython.com/how-to-analyze-data-through-visualization)  
* "PyGWalker: A Python Library for Exploratory Data Analysis with Visualization." "PyGWalker can simplify your Jupyter Notebook data analysis and data visualization workflow, by turning your pandas dataframe (and polars dataframe) into a Tableau-style User Interface for visual exploration." [https://github.com/Kanaries/pygwalker](https://github.com/Kanaries/pygwalker)  

### Single Sign On (SSO) Support  
* In a JupyterHub environment, experiment with OAuthenticator [https://github.com/jupyterhub/oauthenticator](https://github.com/jupyterhub/oauthenticator)  


The Python Language Reference: [https://docs.python.org/3/reference/index.html](https://docs.python.org/3/reference/index.html)  
The Python Standard Library: [https://docs.python.org/3/library/index.html](https://docs.python.org/3/library/index.html)  
Built-in Functions: [https://docs.python.org/3/library/functions.html](https://docs.python.org/3/library/functions.html)  


### Notes on Python Conditionals  
|Keyword      |  Description  |
|-------------|---------------|
| if (exp):   | Only execute if True  |
| else:       | Next step when 'if' is False |
| elif:       | Test multiple conditions |
| while (exp):| Loop while an exp. if True |
| for n in o: |  |
| break       | Escape a loop |
| continue    | Escape current eteration of a loop, begin another |
| try:        | Begin code block that will catch exceptions |
| except (exception):| Check a given exception type, handle exception |
| finally     | Executed upon success or failure |

### Notes on Python Object Types  
|Type   |  Description  |
|-------|---------------|
|list| A sequence type - [mutable sequence, in square brackets](https://www.w3schools.com/python/python_lists.asp) [] |
|tuple | A sequence type - [imutable sequence, in parentheses](https://www.w3schools.com/python/python_tuples.asp) () |
|dict  | A mapping type - ['key, value' storage, in curly braces](https://www.w3schools.com/python/python_dictionaries.asp) {} |
|set| A [collection of unordered unique elements without duplicates](https://www.w3schools.com/python/python_sets.asp) {} |
|frozenset| |
|range | |
|str| A text type -- an [immutable sequence of characters](https://www.w3schools.com/python/python_strings.asp); with [several representations using single, double, or triple quotes](https://www.w3resource.com/python/python-string.php). Today, [Python's strings have 47 methods](https://www.pythonmorsels.com/string-methods/). |
|unicode| An immutable sequence of Unicode encoded characters |
|int | A Numeric type - an integer is a whole number, positive or negative, without decimals, of unlimited length |
|float | A Numeric type - or "floating point number" is a number, positive or negative, containing one or more decimals; or a float can also be scientific numbers with an "e" to indicate the power of 10 |
|complex | A Numeric type - a complex number is written with a "j" as the imaginary part|
|bool | A Boolean type - [Booleans represent one of two values: True or False](https://www.w3schools.com/python/python_booleans.asp) |
|NoneType | 'None' has [a single value 'null' -- used to signify the absence of a value](https://www.w3schools.com/python/ref_keyword_none.asp). The 'None' keyword is not the same as 0, False, or an empty string |
|bytes | A binary sequence type - an [immutable binary object containing single bytes](https://www.w3resource.com/python/python-bytes.php); from the constructor, bytes(), or from literals use a "b" prefix with normal string syntax: b'python' |
|bytearray | A [binary sequence type](https://docs.python.org/3/library/stdtypes.html#binary-sequence-types-bytes-bytearray-memoryview) - a [mutable binary object containing single bytes](https://www.w3resource.com/python/python-bytes.php); from the constructor, bytearray() |
|memoryview | A Binary type - an [object allowing Python code to access the internal data of an object that supports the buffer protocol without copying](https://docs.python.org/3/library/stdtypes.html#memory-views) |

Built-in Types: [https://docs.python.org/3/library/stdtypes.html](https://docs.python.org/3/library/stdtypes.html)  

Date/Time Formatting: [https://www.foragoodstrftime.com/](https://www.foragoodstrftime.com/)  

timeago -- A very simple python lib, used to format datetime with *** time ago statement.  
https://github.com/hustcc/timeago  

Date/Time Tools Plugin -- The QGIS Date/Time Tools plugin provides tools to manipulate date, time, time zones, and times of the sun.  
https://github.com/NationalSecurityAgency/qgis-datetimetools-plugin  


### Notes on Some Python Standard Library resources  


### API Access to Data  
* One FastAPI approach:  
  * **sqlacodegen** is a tool that reads the structure of an existing database and generates the appropriate SQLAlchemy model code [https://github.com/agronholm/sqlacodegen](https://github.com/agronholm/sqlacodegen)  
  * **FastAPIQuickCRUD** is used to generate CRUD methods in FastApi from an SQLAlchemy schema [https://github.com/LuisLuii/FastAPIQuickCRUD](https://github.com/LuisLuii/FastAPIQuickCRUD)  
  * **FastAPI** is a high-performance web framework for building APIs with Python 3.6+ based on standard Python type hints [https://github.com/tiangolo/fastapi](https://github.com/tiangolo/fastapi)  
* Time-Series data notes:  
  * "What Is a Time-Series Plot, and How Can You Create One?" [https://www.timescale.com/blog/what-is-a-time-series-plot-and-how-can-you-create-one/](https://www.timescale.com/blog/what-is-a-time-series-plot-and-how-can-you-create-one/)  
  * "How to Work With Time Series in Python?" [https://www.timescale.com/blog/how-to-work-with-tim/](https://www.timescale.com/blog/how-to-work-with-tim/)  
  * "Tools for Working With Time-Series Analysis in Python" [https://www.timescale.com/blog/tools-for-working-with-time-series-analysis-in-python/](https://www.timescale.com/blog/tools-for-working-with-time-series-analysis-in-python/)  
  * functime is a Python library for production-ready global forecasting and time-series feature engineering (*comes with time-series preprocessing (box-cox, differencing etc), cross-validation splitters (expanding and sliding window), and forecast metrics (MASE, SMAPE etc)*) [https://github.com/descendant-ai/functime](https://github.com/descendant-ai/functime)  
  * "A Guide to Obtaining Time Series Datasets in Python." [How to use the pandas_datareader] By Mehreen Saeed [https://machinelearningmastery.com/a-guide-to-obtaining-time-series-datasets-in-python/](https://machinelearningmastery.com/a-guide-to-obtaining-time-series-datasets-in-python/)  


### Utility classes  
* Python String Utils - A handy library to validate, manipulate and generate strings: [https://github.com/daveoncode/python-string-utils](https://github.com/daveoncode/python-string-utils)  
* List AWS and GCP instances: [https://github.com/google/python-cloud-utils/blob/master/cloud_utils/list_instances.py](https://github.com/google/python-cloud-utils/blob/master/cloud_utils/list_instances.py)  
* Python utilities for AWS: [https://github.com/hseera/aws-python-utilities](https://github.com/hseera/aws-python-utilities)  
* Check an IP address for *cloud* ownership: [https://github.com/nccgroup/cloud_ip_ranges/](https://github.com/nccgroup/cloud_ip_ranges/)  
  * Sometimes you need to know how to block or permit IP address source or destination addresses from a given cloud service provider:  
  * AWS IP Address ranges: [https://ip-ranges.amazonaws.com/ip-ranges.json](https://ip-ranges.amazonaws.com/ip-ranges.json)  
  * Azure IP address ranges: [https://www.microsoft.com/en-us/download/confirmation.aspx?id=56519](https://www.microsoft.com/en-us/download/confirmation.aspx?id=56519) (note: *resists automation*)  
  * Digital Ocean IP address ranges: [http://digitalocean.com/geo/google.csv](http://digitalocean.com/geo/google.csv)  
  * Google Cloud IP address ranges: [https://www.gstatic.com/ipranges/cloud.json](https://www.gstatic.com/ipranges/cloud.json)  
  * Oracle Cloud IP address ranges: [https://docs.cloud.oracle.com/en-us/iaas/tools/public_ip_ranges.json](https://docs.cloud.oracle.com/en-us/iaas/tools/public_ip_ranges.json)  
* A collection of Python scripts: [https://github.com/metafy-social/python-scripts](https://github.com/metafy-social/python-scripts)  
* Python utility scripts to help automate mundane/repetitive/specific performance testing tasks: [https://github.com/hseera/python-utilities](https://github.com/hseera/python-utilities)  
* Get detail about the OS: [https://github.com/hseera/get-System-Information](https://github.com/hseera/get-System-Information)  
* Broad set of examples [https://github.com/yennanliu/utility_Python/](https://github.com/yennanliu/utility_Python/)  
* Another useful collection of examples: [https://github.com/cherkavi/python-utilities](https://github.com/cherkavi/python-utilities)  
* Reminder to self - Look at these utilities: [https://github.com/karldoenitz/PythonUtils](https://github.com/karldoenitz/PythonUtils)  
* "Seamless FastAPI Configuration with ConfZ." by Silvan Melchior [https://blog.devgenius.io/seamless-fastapi-configuration-with-confz-90949c14ea12](https://blog.devgenius.io/seamless-fastapi-configuration-with-confz-90949c14ea12) and [https://github.com/silvanmelchior/FastAPI_ConfZ_Demo](https://github.com/silvanmelchior/FastAPI_ConfZ_Demo)  
* Some example Utility functions [https://github.com/ukncsc/viper/blob/master/viper/common/utils.py](https://github.com/ukncsc/viper/blob/master/viper/common/utils.py)  

### ToDo  
* Try refactoring a couple scripts with **[typer](https://github.com/tiangolo/typer)**, a library for building CLI applications [https://github.com/tiangolo/typer](https://github.com/tiangolo/typer)  
* Do the same refactoring exercise with **[arguably](https://github.com/treykeown/arguably)**, a library for converting functions into command line interfaces (CLIs)  
* Experiment with [Quart](https://github.com/pallets/quart), an async Python web microframework -- an asyncio reimplementation of the popular Flask microframework API.  
* Figure out what [ChatSQL]() is. It is described as "plain text that it is given by the user is converted to mysql queries using ChatGPT" [https://github.com/ademakdogan/ChatSQL](https://github.com/ademakdogan/ChatSQL)  
* See if this tool works: [EPUB Crush](https://github.com/jncraton/epubcrush) compresses EPUB files to reduce size. By default, all images, fonts, scipts, and styles will be removed from the EPUB.  
* I also will experiment some with Juan-Pablo Scaletti's "[proper CLI](https://github.com/jpsca/proper-cli)"  
* Try rewriting some GPS code from C.  For example: https://github.com/DFRobotdl/USB_GPS_EN/blob/main/gps.h  
* Or just try making use of some other GPS code on Github: https://github.com/search?q=GPS+language%3APython+Ublox+&type=repositories&l=Python (Ublox comes from: https://thepihut.com/products/usb-gps-receiver-with-2m-extension-cable-compatible-with-raspberry-pi-lattepanda-jetson-nano#product-reviews)  
* I see a lot of references to 'httpx' - "a fully featured HTTP client library for Python 3" [https://github.com/encode/httpx](https://github.com/encode/httpx).  I need to do some experimenting and see what the advantages might be.  
* Similarly, I see references to 'HTTPie' - [https://kracekumar.com/post/print_http_request/](https://kracekumar.com/post/print_http_request/)  
* Also, I need to get more literate with 'async' - [https://www.b-list.org/weblog/2022/aug/16/async/](https://www.b-list.org/weblog/2022/aug/16/async/) and also see [https://superfastpython.com/python-asyncio/](https://superfastpython.com/python-asyncio/)  
* Build Your Python Project Documentation With MkDocs. By Martin Breuss, 2022-06-15 [https://realpython.com/python-project-documentation-with-mkdocs/](https://realpython.com/python-project-documentation-with-mkdocs/)  
* Tools for Rewriting Python Code [https://lukeplant.me.uk/blog/posts/tools-for-rewriting-python-code/](https://lukeplant.me.uk/blog/posts/tools-for-rewriting-python-code/)  
* Build a starter/skeleton class for interacting with an SQLite database:
  * [https://jcristharif.com/ibis-datasette.html](https://jcristharif.com/ibis-datasette.html)  
  * See if this will help: [https://abstractkitchen.com/blog/flask-backbone/#section7](https://abstractkitchen.com/blog/flask-backbone/#section7)  
* Visual Python Tkinter GUI Creator [https://visualtk.com/](https://visualtk.com/)  
  * "Data and System Visualization Tools That Will Boost Your Productivity" [https://martinheinz.dev/blog/75](https://martinheinz.dev/blog/75) and Jailer [https://wisser.github.io/Jailer/home.htm](https://wisser.github.io/Jailer/home.htm)  
* Review these interesting server projects:  
  * [https://github.com/illBeRoy/tldr-of-the-world-server](https://github.com/illBeRoy/tldr-of-the-world-server)  
  * [https://github.com/flask-restful/flask-restful](https://github.com/flask-restful/flask-restful)  
* Experiment "[Using a Raspberry Pi as a Bluetooth speaker with PipeWire](https://www.collabora.com/news-and-blog/blog/2022/09/02/using-a-raspberry-pi-as-a-bluetooth-speaker-with-pipewire-wireplumber/)"  
* Wherever possible, use PIP_REQUIRE_VIRTUALENV [https://discuss.python.org/t/pip-make-pip-require-virtualenv-the-default/3776](https://discuss.python.org/t/pip-make-pip-require-virtualenv-the-default/3776)  
* Experiment with Refurb, a tool for refurbishing and modernizing Python codebases [https://github.com/dosisod/refurb](https://github.com/dosisod/refurb)  
 
### Notes on home cluster project  
See starter: [https://github.com/orenzp/gitops](https://github.com/orenzp/gitops)  
* Related, "Blueprint/Boilerplate For Python Projects": [https://github.com/MartinHeinz/python-project-blueprint](https://github.com/MartinHeinz/python-project-blueprint)  