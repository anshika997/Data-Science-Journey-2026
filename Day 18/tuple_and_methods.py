data = (10, 20, 30, 20, 40)

print(data)

value_count = data.count(20)
print(value_count)

index_value = data.index(30)
print(index_value)

length = len(data)
print(length)

maximum = max(data)
print(maximum)

minimum = min(data)
print(minimum)

total = sum(data)
print(total)

new_tuple = data + (50, 60)
print(new_tuple)

repeated_tuple = data * 2
print(repeated_tuple)

for item in data:
    print(item)
