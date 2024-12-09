# PythonStuff:  

## Some Free Python App Hosting Options  
*from a longer list by Nik Tomazic at: [https://testdriven.io/blog/heroku-alternatives/](https://testdriven.io/blog/heroku-alternatives/)*  

* **PythonAnywhere** [https://www.pythonanywhere.com/](https://www.pythonanywhere.com/)  
* **Render** [https://render.com/](https://render.com/), and  [https://render.com/docs/free](https://render.com/docs/free)  
* **Fly.io** [https://fly.io/](https://fly.io/), and [https://community.fly.io/t/i-dont-understand-free-tier/5145/2](https://community.fly.io/t/i-dont-understand-free-tier/5145/2)  
* **Vercel** [https://vercel.com/](https://vercel.com/), Python can only be used as serverless functions [https://vercel.com/guides/does-vercel-offer-free-trial](https://vercel.com/guides/does-vercel-offer-free-trial)  
* **Netlify**: Python can only be used as serverless functions [https://www.netlify.com/](https://www.netlify.com/)  
* **Binder**:[https://mybinder.org/](https://mybinder.org/) for hosting/sharing Jupyter notebooks  


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

Or check out a more comprehensive description of setting up a new environment at [https://github.com/mccright/PythonStuff/blob/main/New-environment-notes.md](https://github.com/mccright/PythonStuff/blob/main/New-environment-notes.md)  


Get the Python Launcher for Unix: [https://github.com/brettcannon/python-launcher](https://github.com/brettcannon/python-launcher)  

### minpyver  
Sometimes it is important to enforce a minimum Python version.  See Nicholas Hairs' "[Summary of Major Changes Between Python Versions](https://www.nicholashairs.com/posts/major-changes-between-python-versions/)" for a history of some reasons why that is...  
* '[minpyver.py](https://github.com/mccright/PythonStuff/blob/main/minpyver.py)' - In some situations it is important to use a very specific Python version.  
  Yes, it might be better to just add:  

```python
if sys.version_info < (3, 10):
    raise Exception("Use only with Python 3.10 or higher")
```

### Python Logging  
I have another repo with with some Python logging content [https://github.com/mccright/PythonLoggingExamples/](https://github.com/mccright/PythonLoggingExamples/)  

### Python Regex Cheatsheet  
From [Debuggex](https://www.debuggex.com/): [https://www.debuggex.com/cheatsheet/regex/python](https://www.debuggex.com/cheatsheet/regex/python)  
### Python re(gex) -- a magical tool for text processing  
By Sundeep Agarwal [https://learnbyexample.github.io/py_regular_expressions/](https://learnbyexample.github.io/py_regular_expressions/) or the entire book in a single markdown file at [https://github.com/learnbyexample/py_regular_expressions/blob/master/py_regex.md](https://github.com/learnbyexample/py_regular_expressions/blob/master/py_regex.md) with supporting code at [https://github.com/learnbyexample/py_regular_expressions](https://github.com/learnbyexample/py_regular_expressions)  

### stringSearch  
* This is a harness for evaluating the contents of files (in a directory and all child directories) using a collection of your own regex's.  If you need specialized secrets-hunting utilities, see [TruffleHog](https://github.com/dxa4481/truffleHog) or Burp Suite Extension [SecretFinder](https://github.com/m4ll0k/SecretFinder/blob/master/BurpSuite-SecretFinder/SecretFinder.py).  I used ideas & code from both of them in this string search utility.  

### simpleAPIClient [REST]  
* [Postman](https://www.postman.com/downloads/) is great for most use cases (or try [Darren Burns](https://github.com/darrenburns)' [posting](https://github.com/darrenburns/posting)), but I still sometimes need to poke at a simple API that accepts a POST with a secret in the POST data when my code is not working as expected.  Here is a simple model for starting this kind of work in: [https://github.com/mccright/PythonStuff/tree/main/simplePOST2API](https://github.com/mccright/PythonStuff/tree/main/simplePOST2API)  

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

Sometimes you need to know what types of files are in a github repo along with their layout in order to prepare for a risk-reasonable static analysis.  
  * [getGHtree.py](https://github.com/mccright/FortifyStuff/blob/master/Scripts/getGHtree.py) is a model for extracting a list of files in tree format from user repositories.  
  * [getGHorgtree.py](https://github.com/mccright/FortifyStuff/blob/master/Scripts/getGHorgtree.py) is a model for extracting a list of files in tree format from non-public organization repositories.  


### Get Accurate time from NTP Servers  
* [ntp.py](https://github.com/mccright/PythonStuff/blob/main/ntpTime/ntp.py) will [fetch accurate time from pool.ntp.org](https://github.com/mccright/PythonStuff/tree/main/ntpTime).  I generally use this idiom for timestamps. Use of [pool.ntp.org](https://en.wikipedia.org/wiki/NTP_pool) from inside your organization may be inappropriate or or it may be inaccessible ([NTP](https://en.wikipedia.org/wiki/Network_Time_Protocol) may be blocked at your network perimeter).  In that case, your organization may have an "internal" NTP server.  If so, replace "pool.ntp.org" with your trusted server.  


### getSomeIPInfo  
* [getSomeIPInfo](https://github.com/mccright/PythonStuff/blob/main/getSomeIPInfo.py) is just a reminder for me about navigating simple json.  First using hard-coded references, and then iterating through every key/value pair.  Both approaches have their place.  There is another example used in [getGHtree.py](https://github.com/mccright/FortifyStuff/blob/master/Scripts/getGHtree.py) and [getGHorgtree.py](https://github.com/mccright/FortifyStuff/blob/master/Scripts/getGHorgtree.py).  


### useRandomUserAgent  
* [useRandomUserAgent](https://github.com/mccright/PythonStuff/blob/main/useRandomUserAgent.py) is just a reminder for me about rotating my user_agent strings.  


### checkResponseCodes  
* [checkResponseCodes](https://github.com/mccright/PythonStuff/blob/main/checkResponseCodes.py) is a list of all the http Codes from the IANA Hypertext Transfer Protocol (HTTP) Status Code Registry in the form of a long 'case statement.'  I wanted it around so that I could copy out the subset that I needed at any given time.  It is not meant to be used as is.  


### http-response-codes  
* [http-response-codes](https://github.com/mccright/PythonStuff/blob/main/http-response-codes.py) is a CLI script that emits a list of all the http Codes from your current http module plus their short description & long description.  
I usually pipe its output through grep for the code I am trying to understand.  I found that when troubleshooting people's cloud-hosted lambdas & functions I run into more *obscure* response codes and need to check their meaning.  


### createRandomStrings.py  
* [createRandomStrings](https://github.com/mccright/PythonStuff/blob/main/createRandomStrings.py) is some unfinished experimenting with different ways to create 'unique' strings, a common requirement...  


### encryptstr.py  
[encryptstr](https://github.com/mccright/PythonStuff/blob/main/encryptTest/encryptstr.py) is a sketal set of AES-CBC string encryption/decryption functions.  

### temp-file-in-mem.py  
[temp-file-in-mem.py](https://github.com/mccright/PythonStuff/blob/main/temp-file-in-mem.py) illustrates how to create and use an in-memory tmp file.  Native Python provides a range of objects for data storage, so this is likely only needed for odd, one-off use cases that require a *fast and lean* queue/buffer, building a stream, holding text for # processing *later*, etc. and something like a Python list won't do.  

### get-pdf-text.py  
[get-pdf-text](https://github.com/mccright/PythonStuff/blob/main/extract-pdf-text/get-pdf-text.py) is an informal approach to using 'pypdf' to extract text from PDF files that often works well-enough for me. It is constructed from examples in the [pypdf docs](https://pypdf.readthedocs.io/en/stable/user/extract-text.html).  `pypdf` can [extract a range of PDF components](https://pypdf2.readthedocs.io/en/3.0.0/_modules/PyPDF2/_reader.html).  

### c2f.py and f2c.py  
[c2f.py](https://github.com/mccright/PythonStuff/blob/main/c2f.py) and [f2c.py](https://github.com/mccright/PythonStuff/blob/main/f2c.py) are used to quickly convert Celsius To Fahrenheit and Fahrenheit to Celsius on the command line.  

### otherNotes.md  
* [otherNotes.md](https://github.com/mccright/PythonStuff/blob/main/otherNotes.md) is just a collection of short code fragments that act as reminders for me.  


## AWS Lambdas  
* Starter project [https://github.com/serverless/examples/tree/master/aws-python-simple-http-endpoint](https://github.com/serverless/examples/tree/master/aws-python-simple-http-endpoint)  
* 25 model projects [https://github.com/serverless/examples](https://github.com/serverless/examples)  

## Minify HTML  
* There is a Python module [minify-html](https://pypi.org/project/minify-html) with source at [https://github.com/wilsonzlin/minify-html](https://github.com/wilsonzlin/minify-html)  

## Scrape some text on the Web  
* A Python package & command-line tool to gather text on the Web: [https://github.com/adbar/trafilatura](https://github.com/adbar/trafilatura)  

## Run your Jupyter notebook on the command line  
[https://github.com/jsvine/nbexec](https://github.com/jsvine/nbexec)  

## Python and Visual Studio Code (VSCode)  
See: "Python Development in Visual Studio Code." by Jon Fincher  
[https://realpython.com/python-development-visual-studio-code/](https://realpython.com/python-development-visual-studio-code/)  
and
"Advanced Visual Studio Code for Python Developers." by Anthony Shaw  
[https://realpython.com/advanced-visual-studio-code-python/](https://realpython.com/advanced-visual-studio-code-python/)  


## Python Enhancement Proposal 20 -- PEP-20  
(available via: ```import this```)  
The Zen of Python by Tim Peters (1999).  This is often described as the core philosophy of Python.  
[https://peps.python.org/pep-0020/#the-zen-of-python](https://peps.python.org/pep-0020/#the-zen-of-python)  
or  
[https://github.com/python/peps/blob/main/pep-0020.txt](https://github.com/python/peps/blob/main/pep-0020.txt)  


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
  * And use [Python f-strings](https://fstring.help/) to make your work easier.  
* Use *[better-exceptions](https://github.com/Qix-/better-exceptions)* during local development, and use care to keep it out of your production deployments.  
* Another approach would be to use [pymg](https://github.com/mimseyedi/pymg), a CLI tool that can interpret Python files by the Python interpreter and display the error message in a more readable way if an exception occurs [https://github.com/mimseyedi/pymg](https://github.com/mimseyedi/pymg)  
* What is the difference between using  "_" and "__" in variable or function names?  The responses get at some Python conventions: [https://old.reddit.com/r/learnpython/comments/s5z0l8/can_someone_explain_and_in_python_clearly_for_me/](https://old.reddit.com/r/learnpython/comments/s5z0l8/can_someone_explain_and_in_python_clearly_for_me/)  


## External References  

* "Avoiding Silent Failures in Python: Best Practices for Error Handling." By Bob Belderbos, 2023-08-07 [https://pybit.es/articles/python-errors-should-not-pass-silently](https://pybit.es/articles/python-errors-should-not-pass-silently/)  
* "Python Quirks." [https://writing.peercy.net/p/python-quirks](https://writing.peercy.net/p/python-quirks)  
* "WTF Python!-- Exploring and understanding Python through surprising snippets."  [https://github.com/satwikkansal/wtfpython](https://github.com/satwikkansal/wtfpython)  
* "Python Data Science Handbook." By Jake VanderPlas. [https://github.com/jakevdp/PythonDataScienceHandbook](https://github.com/jakevdp/PythonDataScienceHandbook) and [https://jakevdp.github.io/PythonDataScienceHandbook/](https://jakevdp.github.io/PythonDataScienceHandbook/)  
* A package that can save you some typing whenever you will be accepting command line arguments. Just run *duckargs* with the arguments your program will accept along with example values for options, and duckargs will generate the python code for a program that uses argparse to handle those arguments. [https://github.com/eriknyquist/duckargs](https://github.com/eriknyquist/duckargs)  
* Python Concepts by CodingAcademy: [https://github.com/Codecademy/docs/tree/main/content/python/concepts](https://github.com/Codecademy/docs/tree/main/content/python/concepts)  
* Simple file upload using Flask: [https://roytuts.com/python-flask-file-upload-example/](https://roytuts.com/python-flask-file-upload-example/) and consider enhancing it with [Flask ReUploaded](https://flask-reuploaded.readthedocs.io/en/latest/).  
* Flasgger is a Flask extension to extract OpenAPI-Specification from all Flask views registered in your API. Flasgger also comes with SwaggerUI embedded so you can access http://localhost:5000/apidocs and visualize and interact with your API resources.[https://github.com/flasgger/flasgger](https://github.com/flasgger/flasgger)  
* Some example Flask methods [https://github.com/MartinHeinz/LifestyleTracker/blob/master/app/__init__.py](https://github.com/MartinHeinz/LifestyleTracker/blob/master/app/__init__.py)  
* "Flask-Backbone -- Your Next Flask Boilerplate..." [https://abstractkitchen.com/blog/flask-backbone/](https://abstractkitchen.com/blog/flask-backbone/) and the code at [https://github.com/abstractkitchen/flask-backbone](https://github.com/abstractkitchen/flask-backbone)  
* "A Gentle Introduction to AWS Lambda." Matt Bacchi, 2022-02-01 [https://bacchi.org/posts/gentle-intro-lambda/](https://bacchi.org/posts/gentle-intro-lambda/)  
* Python Graph Gallery: A Collection of Hundreds of Charts Made With Python [https://www.python-graph-gallery.com/](https://www.python-graph-gallery.com/) especially time series graphing [https://www.python-graph-gallery.com/basic-time-series-with-matplotlib](https://www.python-graph-gallery.com/basic-time-series-with-matplotlib)  
* Six books about Python and data science (PDFs hosted by [Riccardo Rigon](https://orcid.org/0000-0002-7668-5806)): https://osf.io/fmkwy/  
* See the responses to a question about Python type hints (especially the response by 'BerislavLopac') [https://news.ycombinator.com/item?id=30288000](https://news.ycombinator.com/item?id=30288000)  
* "How to Pickle and Unpickle Objects in Python." [https://stackabuse.com/how-to-pickle-and-unpickle-objects-in-python/](https://stackabuse.com/how-to-pickle-and-unpickle-objects-in-python/)  
* Fetch a git repository (from GitHub or locally), build a container image based on the specifications found in the repository & optionally launch the container that you can use to explore the repository [https://github.com/jupyterhub/repo2docker](https://github.com/jupyterhub/repo2docker)  
* A Python exception library to ease handling and displaying exceptions -- *Caution: It may be unsafe for some use cases* [https://github.com/MasoniteFramework/exceptionite](https://github.com/MasoniteFramework/exceptionite)  
* Python Concepts by CodingAcademy: [https://github.com/Codecademy/docs/tree/main/content/python/concepts](https://github.com/Codecademy/docs/tree/main/content/python/concepts)  
* Coding Docs by CodingAcademy: [https://github.com/Codecademy/docs](https://github.com/Codecademy/docs)  
* "Learn Python 3." by  Sonny Li, David Patlut and Tim Liedtke, [https://www.codecademy.com/learn/learn-python-3](https://www.codecademy.com/learn/learn-python-3) with supporting materials at https://github.com/Codecademy/learn-python[https://github.com/Codecademy/learn-python](https://github.com/Codecademy/learn-python)  
* "An introduction to Python for non-programmers using inflammation data." by Software-Carpentry [https://github.com/swcarpentry/python-novice-inflammation](https://github.com/swcarpentry/python-novice-inflammation)  
* "Introduction to Python for non-programmers with a focus on plotting and data analysis." by Software-Carpentry [https://github.com/swcarpentry/python-novice-gapminder](https://github.com/swcarpentry/python-novice-gapminder)  
* Python CheatSheets: [https://github.com/afizs/python-notes/blob/main/resources/cheatsheets.md](https://github.com/afizs/python-notes/blob/main/resources/cheatsheets.md)  
* Local hosting of a Python CheatSheet from gto76: [https://github.com/mccright/python-cheatsheet/blob/main/README.md](https://github.com/mccright/python-cheatsheet/blob/main/README.md)  
* 'A Dense' Python CheatSheet: [https://github.com/kieranholland/best-python-cheat-sheet](https://github.com/kieranholland/best-python-cheat-sheet)  
* Python CheatSheet: [https://github.com/jwasham/coding-interview-university/blob/main/extras/cheat%20sheets/python-cheat-sheet-v1.pdf](https://github.com/jwasham/coding-interview-university/blob/main/extras/cheat%20sheets/python-cheat-sheet-v1.pdf)  
* Grokking the Coding Interview Patterns for Coding Questions (*Python code in 16 problem categories*):  [https://github.com/cl2333/Grokking-the-Coding-Interview-Patterns-for-Coding-Questions](https://github.com/cl2333/Grokking-the-Coding-Interview-Patterns-for-Coding-Questions)  
* Python code for ~1000 situations: [https://github.com/cl2333/Leetcode/tree/master/Python](https://github.com/cl2333/Leetcode/tree/master/Python)  
* 11 Approaches to File Handling in Python: [https://github.com/balapriyac/File-Handling-in-Python/tree/main/Code](https://github.com/balapriyac/File-Handling-in-Python/tree/main/Code) or look at what GitHub returns on this topic: [https://github.com/topics/file-handling-in-python?l=python](https://github.com/topics/file-handling-in-python?l=python)  
* Coding Interview Python Language Essentials: [https://github.com/jwasham/coding-interview-university/blob/main/extras/cheat%20sheets/Coding%20Interview%20Python%20Language%20Essentials.pdf](https://github.com/jwasham/coding-interview-university/blob/main/extras/cheat%20sheets/Coding%20Interview%20Python%20Language%20Essentials.pdf)  

