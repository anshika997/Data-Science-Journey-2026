# Match Case in Python

## Introduction

`match case` is used to compare one value with multiple options.  
It works like switch–case in other programming languages such as C and Java.

This feature was introduced in Python version 3.10.

Use `match case` when:
- You have fixed choices
- You want clean and readable code
- You want to avoid long if–elif–else blocks

---

## Basic Syntax

```python
match value:
    case option1:
        statement
    case option2:
        statement
    case _:
        default statement
