# Day 05: List Comprehension in Python

# 1. Basic List Comprehension
numbers = [1, 2, 3, 4, 5]
squares = [x * x for x in numbers]
print("Squares:", squares)


# 2. List Comprehension with Condition
even_numbers = [x for x in numbers if x % 2 == 0]
print("Even Numbers:", even_numbers)


# 3. Traditional Loop vs List Comprehension
# Traditional way
double_numbers = []
for x in numbers:
    double_numbers.append(x * 2)

print("Doubled (Loop):", double_numbers)

# List comprehension way
double_numbers_lc = [x * 2 for x in numbers]
print("Doubled (List Comprehension):", double_numbers_lc)


# 4. List Comprehension with Strings
names = ["Anshika", "Rahul", "Amit", "Sneha"]
short_names = [name for name in names if len(name) <= 5]
print("Short Names:", short_names)


# 5. Nested List Comprehension
matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [num for row in matrix for num in row]
print("Flattened Matrix:", flattened)


# 6. List Comprehension with if-else
result = ["Even" if x % 2 == 0 else "Odd" for x in numbers]
print("Even/Odd Result:", result)
