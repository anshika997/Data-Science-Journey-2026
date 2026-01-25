# Lambda Functions in Python

# A lambda function is a small anonymous function
# It can have multiple arguments but only one expression


# 1. Basic lambda function
add = lambda a, b: a + b
print("Addition:", add(5, 3))


# 2. Lambda with single argument
square = lambda x: x * x
print("Square:", square(4))


# 3. Lambda with condition
check_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print("Number Type:", check_even(7))


# 4. Lambda with list
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print("Doubled List:", doubled)


# 5. Lambda with filter
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers:", even_numbers)


# 6. Lambda with sorted
students = [("Anshika", 90), ("Rahul", 85), ("Amit", 92)]
sorted_students = sorted(students, key=lambda x: x[1])
print("Sorted by Marks:", sorted_students)
