# for loop with range
for i in range(1, 6):
    print(i)

print("-----")

# for loop with list
numbers = [10, 20, 30, 40]
for n in numbers:
    print(n)

print("-----")

# for loop with string
text = "Python"
for ch in text:
    print(ch)

print("-----")

# while loop
i = 1
while i <= 5:
    print(i)
    i += 1

print("-----")

# while loop with condition
x = 10
while x > 0:
    print(x)
    x -= 2

print("-----")

# nested for loop
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

print("-----")

# break statement
for i in range(1, 10):
    if i == 5:
        break
    print(i)

print("-----")

# continue statement
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

print("-----")

# pass statement
for i in range(5):
    pass

print("-----")

# infinite loop example (commented to avoid execution)
# while True:
#     print("Infinite loop")
