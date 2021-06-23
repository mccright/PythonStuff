# PythonStuff:  
## Some Python code that I tend to copy & morph  

* '[minpyver.py](https://github.com/mccright/PythonStuff/blob/main/minpyver.py)' - In some situations it is important to use a very specific Python version.  
  Yes, it might be better to just add:  
```python
if sys.version_info < (3, 7):
    raise Exception("Use only with Python 3.7 or higher")
```
* Sometimes you need to know what types of files are in a github repo along with their layout in order to prepare for a risk-reasonable static analysis.  
  * [getGHtree.py](https://github.com/mccright/FortifyStuff/blob/master/Scripts/getGHtree.py) is a model for extracting a list of files in tree format from user repositories.  
  * [getGHorgtree.py](https://github.com/mccright/FortifyStuff/blob/master/Scripts/getGHorgtree.py) is a model for extracting a list of files in tree format from non-public organization repositories.  
