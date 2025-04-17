# Validating Data With Python  

### Dates
* A useful collection of regexes for dates, times, and timezones: [https://github.com/Pithikos/python-reusables/blob/master/datetime/pattern_matching.py](https://github.com/Pithikos/python-reusables/blob/master/datetime/pattern_matching.py)  
* A simple validation library for validating simple values [https://github.com/kvesteri/validators](https://github.com/kvesteri/validators)  


### Debugging your Regex  
(*See section "Regex Debugging via Parse Tree" in [https://stackabuse.com/hidden-features-of-python/](https://stackabuse.com/hidden-features-of-python/)*)  

Using regular expression-based validations can be a challenge.  Building a regex for given real-world validations can be complex and hard to understand.  

The re module in Python has a re.DEBUG flag which can help you debug regular expressions.  The re.DEBUG flag only works with re.compile().  It does not work with the re.match() or re.search() functions.  

Here is a simplistic model to validate a date (for example: 2023-09-06) using the re.DEBUG flag:

```python
import re

re.compile("\d{4}-\d{2}-\d{2}", re.DEBUG)
```

or only *slightly* better: 

```python
import re

re.compile("(0?[\d]{1}|0?[\d]{2}|0?[\d]{3}|1[\d]{3}|2[\d]{3})(\/|-|\.)(0?[1-9]|1[0-2])(\/|-|\.)(0[1-9]|1[0-9]|2[0-9]|30|31)", re.DEBUG)
```

Caution! Both of the examples above will accept some invalid dates.  See [https://regexlib.com/Search.aspx?k=date&c=5&m=4&ps=100](https://regexlib.com/Search.aspx?k=date&c=5&m=4&ps=100) for other date validation regex examples.  


### What about checking for an IP address?  

```python
import re

re.compile("((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)", re.DEBUG)
```



* Test your regex on line: [https://regex101.com/](https://regex101.com/) or  
* test your regex with: [https://pythex.org/](https://pythex.org/)  
