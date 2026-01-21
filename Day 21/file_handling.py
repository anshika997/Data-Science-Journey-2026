# write to a file
file = open("sample.txt", "w")
file.write("Hello, this is file handling in Python.\n")
file.write("This file is created using write mode.\n")
file.close()

# read from a file
file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()

# append to a file
file = open("sample.txt", "a")
file.write("This line is added using append mode.\n")
file.close()

# read file line by line
file = open("sample.txt", "r")
for line in file:
    print(line.strip())
file.close()

# using with statement
with open("sample.txt", "r") as file:
    data = file.read()
    print(data)
