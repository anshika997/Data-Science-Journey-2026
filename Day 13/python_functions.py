def greet():
    print("Hello Python")

greet()
print("-" * 50)

def add(a, b):
    return a + b

print(add(5, 3))
print("-" * 50)

def subtract(a, b):
    return a - b

print(subtract(10, 4))
print("-" * 50)

def multiply(a, b):
    return a * b

print(multiply(6, 7))
print("-" * 50)

def divide(a, b):
    return a / b

print(divide(20, 4))
print("-" * 50)

def even_or_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(even_or_odd(9))
print("-" * 50)

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))
print("-" * 50)

def find_max(a, b, c):
    return max(a, b, c)

print(find_max(10, 25, 15))
print("-" * 50)

print("Functions executed successfully")
