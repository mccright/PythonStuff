# PythonStuff:  
## Some Python code that I tend to copy & morph  

### New environment?  Install Python:  
Debian-based Linux, for example, Ubuntu or one of its variants:  
```bash
sudo apt-get update
sudo apt-get install python3 python3-venv python3-pip
```
RedHat/Fedora-based Linux:  
```bash
sudo dnf install python3
```


### minpyver  
* '[minpyver.py](https://github.com/mccright/PythonStuff/blob/main/minpyver.py)' - In some situations it is important to use a very specific Python version.  
  Yes, it might be better to just add:  
```python
if sys.version_info < (3, 7):
    raise Exception("Use only with Python 3.7 or higher")
```

### stringSearch  
* This is a harness for evaluating the contents of files (in a directory and all child directories) using a collection of your own regex's.  If you need specialized secrets-hunting utilities, see [TruffleHog](https://github.com/dxa4481/truffleHog) or Burp Suite Extension [SecretFinder](https://github.com/m4ll0k/SecretFinder/blob/master/BurpSuite-SecretFinder/SecretFinder.py).  I used ideas & code from both of them in this string search utility.  

### simpleAPIClient [REST]  
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


### getSomeIPInfo  
* [getSomeIPInfo](https://github.com/mccright/PythonStuff/blob/main/getSomeIPInfo.py) is just a reminder for me about navigating simple json.  First using hard-coded references, and then iterating through every key/value pair.  Both approaches have their place.  There is another example used in [getGHtree.py](https://github.com/mccright/FortifyStuff/blob/master/Scripts/getGHtree.py) and [getGHorgtree.py](https://github.com/mccright/FortifyStuff/blob/master/Scripts/getGHorgtree.py).  


### useRandomUserAgent  
* [useRandomUserAgent](https://github.com/mccright/PythonStuff/blob/main/useRandomUserAgent.py) is just a reminder for me about rotating my user_agent strings.  


### checkResponseCodes  
* [checkResponseCodes](https://github.com/mccright/PythonStuff/blob/main/checkResponseCodes.py) is a list of all the http Codes from the IANA Hypertext Transfer Protocol (HTTP) Status Code Registry in the form of a long 'case statement.'  I wanted it around so that I could copy ot the subset that I needed at any given time.  It is not meant to be used as is.  


### http-response-codes  
* [http-response-codes](https://github.com/mccright/PythonStuff/blob/main/http-response-codes.py) is a CLI script that emits a list of all the http Codes from your current http module plus their short description & long description.  
I usually pipe its output through grep for the code I am trying to understand.  I found that when troubleshooting people's cloud-hosted lambdas & functions I run into more *obscure* response codes and need to check their meaning.  


### createRandomStrings.py  
* [createRandomStrings](https://github.com/mccright/PythonStuff/blob/main/createRandomStrings.py) is some unfinished experimenting with different ways to create 'unique' strings, a common requirement...  


### encryptstr.py  
[encryptstr](https://github.com/mccright/PythonStuff/blob/main/encryptTest/encryptstr.py) is a sketal set of AES-CBC string encryption/decryption functions.  


### otherNotes.md  
* [otherNotes.md](https://github.com/mccright/PythonStuff/blob/main/otherNotes.md) is just a collection of short code fragments that act as reminders for me.  


## AWS Lambdas  
* Starter project [https://github.com/serverless/examples/tree/master/aws-python-simple-http-endpoint](https://github.com/serverless/examples/tree/master/aws-python-simple-http-endpoint)  
* 25 model projects [https://github.com/serverless/examples](https://github.com/serverless/examples)  


## Python and Visual Studio Code (VSCode)  
See: "Python Development in Visual Studio Code." by Jon Fincher  
[https://realpython.com/python-development-visual-studio-code/](https://realpython.com/python-development-visual-studio-code/)  
and
"Advanced Visual Studio Code for Python Developers." by Anthony Shaw  
[https://realpython.com/advanced-visual-studio-code-python/](https://realpython.com/advanced-visual-studio-code-python/)  


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
* Debugging has its place, but [don't hesitate to use *print()* statements](https://adamj.eu/tech/2021/10/08/tips-for-debugging-with-print/). 
(The original *conventions* in this list are from a readme by https://github.com/georgeberry.  Thank you George Berry.)  
* Use *[better-exceptions](https://github.com/Qix-/better-exceptions)* during local development, and use care to keep it out of your production deployments.  
* What is the difference between using  "_" and "__" in variable or function names?  The responses get at some Python conventions: [https://old.reddit.com/r/learnpython/comments/s5z0l8/can_someone_explain_and_in_python_clearly_for_me/](https://old.reddit.com/r/learnpython/comments/s5z0l8/can_someone_explain_and_in_python_clearly_for_me/)  


## External References  
* Simple file upload using Flask: [https://roytuts.com/python-flask-file-upload-example/](https://roytuts.com/python-flask-file-upload-example/) and consider enhancing it with [Flask ReUploaded](https://flask-reuploaded.readthedocs.io/en/latest/).  
