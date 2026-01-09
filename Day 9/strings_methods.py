s1 = "Python Programming"
s2 = 'Hello World'
s3 = """This is
a multi-line
string"""

print(s1)
print(s2)
print(s3)
print("-" * 50)

text = "Python"
print(text[0])
print(text[-1])
print("-" * 50)

print(text[0:4])
print(text[:3])
print(text[2:])
print(text[::-1])
print("-" * 50)

a = "Hello"
b = "Python"
print(a + " " + b)
print("-" * 50)

print("Hi " * 3)
print("-" * 50)

print(len("Programming"))
print("-" * 50)

name = "pYtHoN"
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.title())
print(name.swapcase())
print("-" * 50)

msg = "   hello python   "
print(msg.strip())
print(msg.lstrip())
print(msg.rstrip())
print("-" * 50)

lang = "I love Java"
print(lang.replace("Java", "Python"))
print("-" * 50)

sentence = "Python is very easy to learn"
print(sentence.split())
print("-" * 50)

words = ["Python", "is", "awesome"]
print(" ".join(words))
print("-" * 50)

text = "Programming"
print(text.find("g"))
print(text.index("g"))
print("-" * 50)

fruit = "banana"
print(fruit.count("a"))
print("-" * 50)

print("Python".startswith("Py"))
print("Python".endswith("on"))
print("-" * 50)

print("Python".isalpha())
print("12345".isdigit())
print("Python123".isalnum())
print("   ".isspace())
print("-" * 50)

word = "Python"
print(word.center(10, "*"))
print(word.ljust(10, "-"))
print(word.rjust(10, "-"))
print("-" * 50)

name = "Anshika"
age = 20
print(f"My name is {name} and I am {age} years old.")
print("My name is {} and I am {} years old.".format(name, age))
print("-" * 50)

text = "hello"
print("Strings are immutable in Python")
print("-" * 50)

print("All important Python string functions covered successfully!")
