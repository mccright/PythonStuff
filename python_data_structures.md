## Data Structures  
(*Original version copied from https://github.com/blutterfly/python/blob/main/docs/examples/data_structures.md on 2025-10-21 - thank you "`Butterfly`"*, then edited over time...)  

Introduction of (a few) python data structures:  
* [List](#list_data_type)  
* [Dictionary](#dictionary_data_type)  
* [Set](#set_data_type)  
* [DataFrame](#dataframe_data_type)  
* [Tuple](#tuple_data_type)  
* [Comparisons of these data structures](#comparisons_data_type)  
* [Additional resources](#additional_resources_data_type)  

---
<a name="list_data_type"></a>
### 1. Lists  

Lists are used to store multiple items in a single variable.  
List items can be of any data type.  And a list can contain different data types.  
Lists are ordered. They are changeable. They allow duplicate values.  
List items are indexed, the first item has index [0], the second item has index [1] etc.  
When you add new items to a list, they are placed at the end of the list.  
Lists are created using square brackets.  

Creating a List  

```python
fruits = ["apple", "banana", "cherry"]
print(fruits)
```

or use the list() constructor  

```python
fruits = list(("apple", "banana", "cherry"))
print(fruits)
```


Accessing Items  

```python
print(fruits[0])  # First item
print(fruits[-1])  # Last item
```

Modifying Lists  

```python
fruits.append("orange")  # Add an item
fruits[1] = "blueberry"  # Change an item
print(fruits)
```

Iterating Through a List  

```python
for fruit in fruits:
    print(fruit)
```

Common List Methods  

- `append(item)`: Add an item
- `remove(item)`: Remove an item
- `len(list)`: Get the number of items
- `sort()`: Sort the list

Exercise:  

1. Create a list of your favorite hobbies.  
2. Add a new hobby to the list.  
3. Print each hobby using a loop.  

### Additional Resources:  
* Python List Cheat Sheet. [https://www.cse.msu.edu/.../listAndTuplesCheatSheet.pdf](https://www.cse.msu.edu/~ldillon/cse-ctl/Spring2019/Meeting06/listAndTuplesCheatSheet.pdf)  
* Python Lists. [w3schools.com/python/python_lists.asp](https://www.w3schools.com/python/python_lists.asp)  

---
<a name="dictionary_data_type"></a>
### 2. Dictionaries  

Dictionaries store data in key-value pairs.  
A dictionary is a collection. As of Python version 3.7 dictionary items are ordered (*its items have a defined order, and that order will not change*). It is changeable (*we can change, add or remove items after the dictionary has been created*).  And it does not permit duplicates (*it cannot have two items with the same key*).  
Values in dictionary items can be of any data type.  
Dictionaries are written with curly brackets, and have keys and values.  

  Creating a Dictionary  

```python
student = {"name": "Alex", "age": 16, "grade": "A"}
print(student)
```

  Accessing Items  

```python
print(student["name"])  # Access value by key
```

  Adding/Updating Keys  

```python
student["school"] = "High School"  # Add a new key
student["grade"] = "A+"  # Update value
print(student)
```

  Iterating Through a Dictionary  

```python
for key, value in student.items():
    print(key, ":", value)
```

  Common Dictionary Methods  

- `keys()`: Get all keys  
- `values()`: Get all values  
- `items()`: Get all key-value pairs  

  Exercise:  

1. Create a dictionary with details about your favorite book (title, author, year).  
2. Add a new key for the genre.  
3. Print all the keys and values.  

#### Additional Resources:  
* Dictionaries Cheat Sheet. [https://www.cse.msu.edu/.../cheatSheet.pdf](https://www.cse.msu.edu/~ldillon/cse-ctl/Spring2019/Meeting08/cheatSheet.pdf)  
* Python Dictionaries. [w3schools.com/python/python_dictionaries.asp](https://www.w3schools.com/python/python_dictionaries.asp)

---
<a name="set_data_type"></a>
### 3. Sets 

Sets are used to store multiple items in a single variable.  
Sets are unordered.  
Set **items** are unchangeable and are not indexed -- but you can remove items and add new items.  
A set cannot contain duplicate members.  
Set items can be of any data type and a given set can contain different data types.  
Sets are written with curly brackets.  

Creating a Set  

```python
fruits = {"apple", "banana", "cherry"}
print(fruits)
```

or we can use the set() constructor  

```python
fruits = set(("apple", "banana", "cherry"))
print(fruits)
```

Because there is no index, we cannot access items in a set via an index or a key.  
That said, we can loop through the set items via a for loop.  
We can also see if a specified value is exists in a set via the "in" keyword.  

```python
fruits = {"apple", "banana", "cherry"}

for x in fruits:
  print(x) 

print("apple" not in thisset)  # returns False

```


#### Additional Resources:  
* Dictionaries Cheat Sheet. [https://www.cse.msu.edu/.../cheatSheet.pdf](https://www.cse.msu.edu/~ldillon/cse-ctl/Spring2019/Meeting08/cheatSheet.pdf)  
* Python Sets. [w3schools.com/python/python_sets.asp](https://www.w3schools.com/python/python_sets.asp)  
...Start at: https://www.w3schools.com/python/python_sets_access.asp  

---
<a name="dataframe_data_type"></a>
### 4. DataFrames (Using pandas)  

 What is a DataFrame?  
A DataFrame is a 2-dimensional table-like data structure in the pandas library. Think of it as a spreadsheet.  

  Setting Up pandas  
Make sure you have pandas installed:  

```bash
pip install pandas
```

  Creating a DataFrame  

```python
import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [16, 17, 16],
    "Grade": ["A", "B", "A"]
}

df = pd.DataFrame(data)
print(df)
```

  Accessing Columns  

```python
print(df["Name"])  # Access a single column
print(df[["Name", "Age"]])  # Access multiple columns
```

  Filtering Rows  

```python
print(df[df["Age"] > 16])  # Students older than 16
```

  Adding a New Column  

```python
df["Passed"] = [True, False, True]
print(df)
```

  Iterating Through Rows  

```python
for index, row in df.iterrows():
    print(row["Name"], "is", row["Age"], "years old.")
```

  Exercise:  

1. Create a DataFrame with data about your favorite movies (columns: Title, Year, Genre).  
2. Add a new column for Rating.  
3. Filter the movies to show only those released after 2010.  

---
<a name="tuple_data_type"></a>
### 5. Tuples  

Tuples are used to store multiple items in a single variable.  
A tuple is a collection which is ordered and **unchangeable**.  
  * Tuple items have a defined order, and that order will not change.  
  * We cannot change, add or remove items after the tuple has been created.  
Tuple items are indexed, the first item has index [0], the second item has index [1] etc.  
  * Tuple indexes enable duplicate values.  
Tuples are written with round brackets.  

Creating a Tuple  

```python
fruits = ("apple", "banana", "cherry", "blueberry")
print(fruits)
```

or we can use the tuple() constructor  

```python
fruits = tuple(("apple", "banana", "cherry", "blueberry"))
print(fruits)
```


Accessing Items  

```python
print(fruits[0])   # First item
print(fruits[-1])  # Last item
print(fruits[0:2]) # Range = first 3 items
print(fruits[:2])  # Range = first 3 items
print(fruits[1:])  # Range = last 3 items
```

Unpacking Tuples  

```python
fruits = tuple(("apple", "banana", "cherry", "blueberry"))
(Central_Asia New_Guinea Northern_Hemisphere North_America) = fruits  # Unpack Tuple items
```

Iterating Through a Tuple  

```python
for fruit in fruits:
    print(fruit)
```

or use tuple index numbers  

```python
for i in range(len(fruits)):
  print(fruits[i])
```

 Tuple Methods  

count()	# Returns the number of times a specified value occurs in a tuple  
index()	# Searches the tuple for a specified value and returns the position of where it was found  

#### Additional Resources:  
* Dictionaries Cheat Sheet. [https://www.cse.msu.edu/.../cheatSheet.pdf](https://www.cse.msu.edu/~ldillon/cse-ctl/Spring2019/Meeting08/cheatSheet.pdf)  
* Python Sets. [w3schools.com/python/python_tuples.asp](https://www.w3schools.com/python/python_tuples.asp)  
  - Unpack Tuples. [w3schools.com/python/python_tuples_unpack.asp](https://www.w3schools.com/python/python_tuples_unpack.asp)  


---
<a name="comparisons_data_type"></a>
### Comparing Lists, Dictionaries, DataFrames Sets and Tuples  

|Feature           |List                    |Dictionary            |DataFrame        | Set              | Tuple           |
|------------------|------------------------|----------------------|-----------------|------------------|-----------------|
|Data Organization |Ordered, items by index |Key-value pairs       |Rows and columns |Ordered, no dups  |Ordered, immutable|
|Access Method     |By index                |By key                |By row/column    |Loop through      |By index          |
|Ideal Use Case    |Simple collections      |Mapping relationships |Tabular data     |Resist duplicates |                  |

---

### 5. Final Project Idea: Student Report System  

Build a system that:  

1. Stores student data in a DataFrame.  
2. Allows adding a new student (Name, Age, Grade).  
3. Filters students by a minimum grade.  
4. Prints all student data.  

 Example Code for the System:  

```python
import pandas as pd

# Initial data
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [16, 17, 16],
    "Grade": ["A", "B", "A"]
}
df = pd.DataFrame(data)

# Add a new student
new_student = {"Name": "Daisy", "Age": 17, "Grade": "A+"}
df = df.append(new_student, ignore_index=True)

# Filter by grade
print("Students with grade A or higher:")
print(df[df["Grade"] >= "A"])
```


<a name="additional_resources_data_type"></a>
#### Additional Resources:  
* Python Collections: [docs.python.org/3/library/collections.html#module-collections](https://docs.python.org/3/library/collections.html#module-collections)  
* Python Sequences: [python.org/3/reference/datamodel.html#sequences](https://docs.python.org/3/reference/datamodel.html#sequences)  
* Python Set Types: [python.org/3/reference/datamodel.html#set-types](https://docs.python.org/3/reference/datamodel.html#set-types)  
* Python Data Structures: [python.org/3/tutorial/datastructures.html](https://docs.python.org/3/tutorial/datastructures.html)  
* Sets: [python.org/3/tutorial/datastructures.html#sets](https://docs.python.org/3/tutorial/datastructures.html#sets)  
* Tuples and Sequences: [python.org/3/tutorial/datastructures.html#tuples-and-sequences](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)  
* More on Lists: [python.org/3/tutorial/datastructures.html#more-on-lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)  
* Dictionaries: [python.org/3/tutorial/datastructures.html#dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)  
* Dictionaries: [python.org/3/reference/datamodel.html#dictionaries](https://docs.python.org/3/reference/datamodel.html#dictionaries)  
* Python Data Types: [wikibooks.org/wiki/Python_Programming/Data_Types](https://en.wikibooks.org/wiki/Python_Programming/Data_Types)  
