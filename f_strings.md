# F Strings 
 
(*copied from https://github.com/blutterfly/python/blob/main/docs/examples/f_strings.md on 2025-10-21 - thank you 'butterfly'/Larry Prestosa*)  
Also see: https://cheatography.com/brianallan/cheat-sheets/python-f-strings-number-formatting/  
and https://cheatography.com/brianallan/cheat-sheets/python-f-strings-basics/  

F-strings (formatted string literals) in Python provide a concise and readable way to format strings.  

Below are some examples showcasing different use cases:  

---

### 1. Basic Usage

```python
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")
```

Output:

```
My name is Alice and I am 30 years old.
```

---

### 2. Expressions Inside F-strings

```python
a = 10
b = 5
print(f"Sum: {a + b}, Product: {a * b}, Division: {a / b:.2f}")
```

Output:

```
Sum: 15, Product: 50, Division: 2.00
```

---

### 3. Calling Functions Inside F-strings

```python
def greet(name):
    return f"Hello, {name}!"

print(f"{greet('Bob')}")
```

Output:

```
Hello, Bob!
```

---

### 4. Formatting Numbers

```python
# 'num' below is a float
num = 1234567.89123
print(f"Comma separated: {num:,}")
print(f"Rounded to 2 decimals: {num:.2f}")
print(f"Scientific notation: {num:.2e}")
print(f"f strings can print() integers in hex or binary format, not floats.")
# Convert the float into an integer
num = int(num)
print(f"Hexadecimal: {num:x}")
print(f"Binary: {int(num)} -> {num:b}")

```

Output:

```
Comma separated: 1,234,567.89123
Rounded to 2 decimals: 1234567.89
Scientific notation: 1.23e+06
f strings can print() integers in hex or binary format, not floats.
Hexadecimal: 1234567 -> 12d687
Binary: 1234567 -> 100101101011010000111
```
<small>(*Code correction updates on "Formatting Numbers" section, 2025-10-21 McCright*)</small>

---

### 5. Padding and Alignment

```python
text = "Python"
print(f"Left aligned:   |{text:<10}|")
print(f"Right aligned:  |{text:>10}|")
print(f"Center aligned: |{text:^10}|")
print(f"Padded with *:  |{text:*^10}|")
```

Output:

```
Left aligned:   |Python    |
Right aligned:  |    Python|
Center aligned: |  Python  |
Padded with *:  |Python|
```

---

### 6. Boolean Values

```python
value = True
print(f"Boolean as integer: {int(value)}")
```

Output:

```
Boolean as integer: 1
```

---

### 7. Formatting Dates and Time

```python
from datetime import datetime

now = datetime.now()
print(f"Current Date: {now:%Y-%m-%d}")
print(f"Current Time: {now:%H:%M:%S}")
```

Output:

```
Current Date: 2025-02-27
Current Time: 14:23:45
```

---

### 8. Nesting F-strings

```python
name = "Charlie"
age = 25
info = f"Name: {name}, Age: {age}"
print(f"User Info: {info}")
```

Output:

```ini
User Info: Name: Charlie, Age: 25
```

---

### 9. Using Dictionaries Inside F-strings

```python
person = {"name": "David", "age": 35}
print(f"Name: {person['name']}, Age: {person['age']}")
```

Output:

```
Name: David, Age: 35
```

---

### 10. Using Lists and Tuples Inside F-strings

```python
fruits = ["Apple", "Banana", "Cherry"]
print(f"My favorite fruit is {fruits[1]}.")

coords = (10.5, 20.8)
print(f"Coordinates: x={coords[0]}, y={coords[1]}")
```

Output:

```
My favorite fruit is Banana.
Coordinates: x=10.5, y=20.8
```

---

### 11. Using Object Attributes in F-strings

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

my_car = Car("Toyota", "Camry")
print(f"My car is a {my_car.make} {my_car.model}.")
```

Output:

```
My car is a Toyota Camry.
```

---

### 12. Using Object Methods in F-strings

```python
class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        return "Woof!"

dog = Dog("Rex")
print(f"{dog.name} says {dog.bark()}")
```

Output:

```
Rex says Woof!
```

---

### 13. Using Ternary Operator Inside F-strings

```python
x = 10
y = 20
print(f"The bigger number is {x if x > y else y}.")
```

Output:

```
The bigger number is 20.
```

---

### 14. Multiline F-strings

```python
name = "Eve"
age = 28
bio = f"""
Name: {name}
Age: {age}
Location: New York
"""
print(bio)
```

Output:

```
Name: Eve
Age: 28
Location: New York
```

---

### 15. Escaping Braces in F-strings

```python
print(f"Use {{ and }} to display curly braces.")
```

Output:

```
Use { and } to display curly braces.
```

---

### 16. Lambda Functions Inside F-strings

```python
square = lambda x: x ** 2
print(f"5 squared is {square(5)}")
```

Output:

```
5 squared is 25
```
<small>(*Code correction updates on "Lambda Functions Inside F-strings" section, 2025-10-22 McCright*)</small>

---

These examples cover basic usage, expressions, function calls, formatting, object attributes, data structures, and advanced techniques in f-strings. Would you like any additional modifications or explanations? 🚀

