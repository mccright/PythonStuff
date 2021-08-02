# PythonStuff:  
## Some Python code that I tend to copy & morph  

* '[minpyver.py](https://github.com/mccright/PythonStuff/blob/main/minpyver.py)' - In some situations it is important to use a very specific Python version.  
  Yes, it might be better to just add:  
```python
if sys.version_info < (3, 7):
    raise Exception("Use only with Python 3.7 or higher")
```
* [Postman](https://www.postman.com/downloads/) is great for most use cases, but I still sometimes need to poke at a simple API that accepts a POST with a secret in the POST data when my code is not working as expected.  Here is a simple model for starting this kind of work in: [https://github.com/mccright/PythonStuff/tree/main/simplePOST2API](https://github.com/mccright/PythonStuff/tree/main/simplePOST2API)  
```python
(env) C:\temp\prob>python simpleAPIClient.py --help
usage: sampleAPIClient [-h] [-d] [-t] [-s] [-p] [-x PROXY_URL] -u API_URL

sampleAPIClient: an API Client POST skeleton for problem-solving

optional arguments:
  -h, --help            show this help message and exit
  -d, --debug           Use to send debug logging to console
  -t, --timing          Use to send timing to console
  -s, --disable_cert_security
                        Use to disable SSL security checking. This can be a security risk concern. Use with caution.
  -p, --proxy_needed    Use to enable a proxy
  -x PROXY_URL, --proxy_url PROXY_URL
                        When enabling a proxy, this is the full URL
  -u API_URL, --api_url API_URL
                        Target api-endpoint - full URL

(env) C:\temp\prob>
```
  * *This is not a point-and-shoot utility.*  
  * At a minimum, you need to modify the code: Replace the "HEADER_PARAMS" and " POST_DATA" dicts with content relevant to your problem/target.  
  * Don't assume that I know what I am doing.  This served its purpose on some weekend work.  It has not seen many different use cases yet and may have serious limitations.  
  * This is not an attempt to deal with APIs that are protected by one or another OAuth implementation or other *session*-related interface.  Its target are those simple POST-and-done APIs that ought to be simple to use, but sometimes are not.  

* Sometimes you need to know what types of files are in a github repo along with their layout in order to prepare for a risk-reasonable static analysis.  
  * [getGHtree.py](https://github.com/mccright/FortifyStuff/blob/master/Scripts/getGHtree.py) is a model for extracting a list of files in tree format from user repositories.  
  * [getGHorgtree.py](https://github.com/mccright/FortifyStuff/blob/master/Scripts/getGHorgtree.py) is a model for extracting a list of files in tree format from non-public organization repositories.  


## Python conventions

* Put a space before a comment: `# This is a comment`  
* Don't make lines longer than ~80 characters  
* Constants in all-caps: `MY_CONSTANT`  
* Use underscores to separate words in variable names: `my_variable`  
* Avoid meaningless variable names. Avoid numbers in variable names. Wrong: `thing1`, `thing2`. Right: `cat_list`, `fluffy_cat_list`.  
* When ambiguous, put variable type in name: `my_list` or `my_set`. This is particularly important for collections. Is it a `dict` or a `list`?  
* Document code with triple quotes (multiline comments): `"""My documentation"""`  
* Write functions when you find yourself repeating code  
* When importing modules, don't import specific functions. Import the whole module, and use the module name and function together. Right: `import time; time.sleep(1)`. Wrong: `from time import sleep; sleep(1)`.  (Are there exceptions to this *rule*?)  
* When you find yourself checking if items are in a `list`, use a `set`  
* Write a snippet of documentation at the top of your file to help you remember what the file does.  
* Write inputs and outputs to functions in a comment in the function body.  
(The original *conventions* in this list are from a readme by https://github.com/georgeberry.  Thank you George Berry.)  
