# File Read Write  
(*copied from https://github.com/blutterfly/python/blob/main/docs/examples/file_io.md on 2025-10-21 - thank you 'butterfly'/Larry Prestosa*)  

## File IO  

Quick reference and examples on writing, saving, and reading files.   
Along with template functions for working with plain text, CSV, and JSON files.  

---

## 1. Plain Text File  

Plain text files are the simplest type of file. You can write strings to them or read their content as text.  

### Template Function for Plain Text Files  

 Writing to a Plain Text File  

```python
def write_to_text_file(file_path, text):
    with open(file_path, 'w') as file:  # Open file in write mode
        file.write(text)  # Write text to the file
```

 Reading from a Plain Text File  

```python
def read_from_text_file(file_path):
    with open(file_path, 'r') as file:  # Open file in read mode
        return file.read()  # Return the content of the file
```

 Example Usage  

```python
write_to_text_file('example.txt', 'Hello, World!')
content = read_from_text_file('example.txt')
print(content)
```

---

## 2. CSV File  

CSV (Comma-Separated Values) files are used to store tabular data.  

### Template Function for CSV Files  

 Writing to a CSV File  

```python
import csv

def write_to_csv(file_path, data):
    with open(file_path, 'w', newline='') as file:  # Open file in write mode
        writer = csv.writer(file)
        writer.writerows(data)  # Write rows of data
```

 Reading from a CSV File  

```python
def read_from_csv(file_path):
    with open(file_path, 'r') as file:  # Open file in read mode
        reader = csv.reader(file)
        return list(reader)  # Convert rows to a list
```

 Example Usage  

```python
data = [
    ['Name', 'Age', 'Grade'],
    ['Alice', 16, 'A'],
    ['Bob', 17, 'B']
]
write_to_csv('students.csv', data)

content = read_from_csv('students.csv')
for row in content:
    print(row)
```

---

## 3. JSON File  

JSON (JavaScript Object Notation) is used to store structured data, such as dictionaries or lists.  

### Template Function for JSON Files  

 Writing to a JSON File.  

```python
import json

def write_to_json(file_path, data):
    with open(file_path, 'w') as file:  # Open file in write mode
        json.dump(data, file, indent=4)  # Write data to the file in JSON format
```

 Reading from a JSON File.  

```python
def read_from_json(file_path):
    with open(file_path, 'r') as file:  # Open file in read mode
        return json.load(file)  # Load data from JSON file
```

 Example Usage.  

```python
data = {
    'students': [
        {'name': 'Alice', 'age': 16, 'grade': 'A'},
        {'name': 'Bob', 'age': 17, 'grade': 'B'}
    ]
}
write_to_json('students.json', data)

content = read_from_json('students.json')
print(content)
```

---

### Summary of File Types.  

| File Type | Python Module | Best for                          |
|-----------|---------------|------------------------------------|
| Plain Text| `open()`       | Storing simple text or logs       |
| CSV       | `csv`          | Tabular data                     |
| JSON      | `json`         | Structured data (hierarchical)   |

Each of these functions can be adapted based on specific requirements.  


### Other Related Reminders:
* Python data I/O Cheat Sheet. [https://www.fabriziomusacchio.com/.../python_data_io](https://www.fabriziomusacchio.com/teaching/python_cheat_sheets/python_data_io)  
* Python File I/O Cheat Sheet. [https://www.cse.msu.edu/.../files-cheat-sheet.pdf](https://www.cse.msu.edu/~ldillon/cse-ctl/Spring2019/Meeting05/files-cheat-sheet.pdf)  
