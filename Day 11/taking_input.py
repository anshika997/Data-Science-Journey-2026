name = input("Enter your name: ")
age = input("Enter your age: ")

print(name)
print(age)
print("-" * 50)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print("-" * 50)

price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

print(price * quantity)
print("-" * 50)

marks1 = int(input("Enter marks 1: "))
marks2 = int(input("Enter marks 2: "))
marks3 = int(input("Enter marks 3: "))

total = marks1 + marks2 + marks3
average = total / 3

print(total)
print(average)
print("-" * 50)

text = input("Enter a word: ")
print(text.upper())
print(text.lower())
print(len(text))
print("-" * 50)

x = int(input("Enter a number: "))
print(x % 2 == 0)
print("-" * 50)

print("Input operations completed successfully")
