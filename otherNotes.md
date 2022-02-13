# Short Reminders  

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
['ConnectTimeout', 'ConnectionError', 'DependencyWarning', 'FileModeWarning', 'HTTPError', 'NullHandler', 'PreparedRequest', 'ReadTimeout', 'Request', 'RequestException', 'RequestsDependencyWarning', 'Response', 'Session', 'Timeout', 'TooManyRedirects', 'URLRequired', '__author__', '__author_email__', '__build__', '__builtins__', '__cached__', '__cake__', '__copyright__', '__description__', '__doc__', '__file__', '__license__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__title__', '__url__', '__version__', '_check_cryptography', '_internal_utils', 'adapters', 'api', 'auth', 'certs', 'chardet', 'check_compatibility', 'codes', 'compat', 'cookies', 'delete', 'exceptions', 'get', 'head', 'hooks', 'logging', 'models', 'options', 'packages', 'patch', 'post', 'put', 'request', 'session', 'sessions', 'status_codes', 'structures', 'urllib3', 'utils', 'warnings']
>>> dir(requests.urllib3)
['HTTPConnectionPool', 'HTTPResponse', 'HTTPSConnectionPool', 'PoolManager', 'ProxyManager', 'Retry', 'Timeout', '__all__', '__author__', '__builtins__', '__cached__', '__doc__', '__file__', '__license__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_collections', 'absolute_import', 'add_stderr_logger', 'connection', 'connection_from_url', 'connectionpool', 'contrib', 'disable_warnings', 'encode_multipart_formdata', 'exceptions', 'fields', 'filepost', 'get_host', 'logging', 'make_headers', 'packages', 'poolmanager', 'proxy_from_url', 'request', 'response', 'util', 'warnings']
>>> dir(requests.exceptions)
['BaseHTTPError', 'ChunkedEncodingError', 'ConnectTimeout', 'ConnectionError', 'ContentDecodingError', 'FileModeWarning', 'HTTPError', 'InvalidHeader', 'InvalidProxyURL', 'InvalidSchema', 'InvalidURL', 'MissingSchema', 'ProxyError', 'ReadTimeout', 'RequestException', 'RequestsDependencyWarning', 'RequestsWarning', 'RetryError', 'SSLError', 'StreamConsumedError', 'Timeout', 'TooManyRedirects', 'URLRequired', 'UnrewindableBodyError', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
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
config.read('example.ini')
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
Sometimed it is important to use the default gateway interface.  
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


### Notes on Python Types  
|Type   |  Description  |
|-------|---------------|
|int    |  |
|long   |  |
|float  |  |
|complex|  |
|boolean|  |

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
|list| A mutable sequence, in square brackets [] |
|tuple | An imutable sequence, in parentheses () |
|dict  | A 'key, value' storage, in curly braces {} |
|set| A collection of unordered unique elements without duplicates |
|str| An immutable sequence of characters |
|unicode| An immutable sequence of Unicode encoded characters |

### Notes on the Python Standard Library resources  


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
* Python utility scripts to help automate mundane/repetitive/specific performance testing tasks: [https://github.com/hseera/python-utilities](https://github.com/hseera/python-utilities)  
* Get detail about the OS: [https://github.com/hseera/get-System-Information](https://github.com/hseera/get-System-Information)  
* Broad set of examples [https://github.com/yennanliu/utility_Python/](https://github.com/yennanliu/utility_Python/)  
* Another useful collection of examples: [https://github.com/cherkavi/python-utilities](https://github.com/cherkavi/python-utilities)  
* Reminder to self - Look at these utilities: [https://github.com/karldoenitz/PythonUtils](https://github.com/karldoenitz/PythonUtils)  
* "Seamless FastAPI Configuration with ConfZ." by Silvan Melchior [https://blog.devgenius.io/seamless-fastapi-configuration-with-confz-90949c14ea12](https://blog.devgenius.io/seamless-fastapi-configuration-with-confz-90949c14ea12) and [https://github.com/silvanmelchior/FastAPI_ConfZ_Demo](https://github.com/silvanmelchior/FastAPI_ConfZ_Demo)  
* Some example Utility functions [https://github.com/ukncsc/viper/blob/master/viper/common/utils.py](https://github.com/ukncsc/viper/blob/master/viper/common/utils.py)  
* I see a lot of references to 'httpx' - "a fully featured HTTP client library for Python 3" [https://github.com/encode/httpx](https://github.com/encode/httpx).  I need to do some experimenting and see what the advantages might be.  

  
### Notes on home cluster project  
See starter: [https://github.com/orenzp/gitops](https://github.com/orenzp/gitops)  
