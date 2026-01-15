# String Formatting and f-Strings in Python

## Introduction

String formatting is used to insert variables or values inside a string.  
Instead of writing multiple print statements or using concatenation, formatting makes code clean and readable.

Python supports multiple ways of string formatting:
1. Using commas in print
2. Using `%` operator
3. Using `str.format()`
4. Using f-strings (recommended)

---

## Method 1: Using Comma in print

```python
name = "Anshika"
age = 20

print("My name is", name, "and my age is", age)
