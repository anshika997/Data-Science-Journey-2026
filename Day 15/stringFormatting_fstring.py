name = "Anshika"
age = 20
print("My name is", name, "and my age is", age)
print("-" * 50)

print("My name is %s and my age is %d" % (name, age))
price = 45.5678
print("Price is %.2f" % price)
print("-" * 50)

print("My name is {} and my age is {}".format(name, age))
print("My name is {0} and my age is {1}".format(name, age))
print("My name is {n} and my age is {a}".format(n=name, a=age))
print("-" * 50)

print(f"My name is {name} and my age is {age}")
print("-" * 50)

a = 10
b = 5
print(f"Sum is {a + b}")
print(f"Difference is {a - b}")
print(f"Product is {a * b}")
print(f"Division is {a / b}")
print("-" * 50)

text = "python"
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
print(f"Length: {len(text)}")
print("-" * 50)

pi = 3.14159
print(f"Pi value is {pi:.2f}")
print("-" * 50)

num = 7
print(f"{num} is Even" if num % 2 == 0 else f"{num} is Odd")
print("-" * 50)

print("String formatting executed successfully")
