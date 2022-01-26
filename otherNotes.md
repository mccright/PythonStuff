# Short Reminders  

### Use sys.exit(), not exit() or quit()  
A call to [sys.exit()](https://docs.python.org/3/library/sys.html#sys.exit) is translated into an exception so that clean-up handlers ([finally](https://docs.python.org/3/reference/compound_stmts.html#finally) clauses of [try](https://docs.python.org/3/reference/compound_stmts.html#try) statements) can be executed, and so that a debugger can execute a script without running the risk of losing control. The [os._exit()](https://docs.python.org/3/library/os.html#os._exit) function can be used if it is absolutely positively necessary to exit immediately (for example, in the child process after a call to [os.fork()](https://docs.python.org/3/library/os.html#os.fork)).  

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


### Simple File Read-File Write Functions  
This approach is only a quick hack for problem-solving:  
```python
#!/usr/bin/env python3
import os, re, sys


def readFile(filename):
    with open(filename, "rb") as f:
        return f.read().decode("utf-8")


def writeFile(filename, data):
    with open(filename, "wb") as f:
        f.write(data.encode("utf-8"))
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
* Python utility scripts to help automate mundane/repetitive/specific performance testing tasks: [https://github.com/hseera/python-utilities](https://github.com/hseera/python-utilities)  
* Get detail about the OS: [https://github.com/hseera/get-System-Information](https://github.com/hseera/get-System-Information)  
* Broad set of examples [https://github.com/yennanliu/utility_Python/](https://github.com/yennanliu/utility_Python/)  
* Another useful collection of examples: [https://github.com/cherkavi/python-utilities](https://github.com/cherkavi/python-utilities)  
* Reminder to self - Look at these utilities: [https://github.com/karldoenitz/PythonUtils](https://github.com/karldoenitz/PythonUtils)  
* "Seamless FastAPI Configuration with ConfZ." by Silvan Melchior [https://blog.devgenius.io/seamless-fastapi-configuration-with-confz-90949c14ea12](https://blog.devgenius.io/seamless-fastapi-configuration-with-confz-90949c14ea12) and [https://github.com/silvanmelchior/FastAPI_ConfZ_Demo](https://github.com/silvanmelchior/FastAPI_ConfZ_Demo)  

  
### Notes on home cluster project  
See starter: [https://github.com/orenzp/gitops](https://github.com/orenzp/gitops)  
