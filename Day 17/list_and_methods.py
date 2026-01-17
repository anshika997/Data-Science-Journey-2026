numbers = [10, 20, 30, 40]

numbers.append(50)
print(numbers)

numbers.insert(2, 25)
print(numbers)

numbers.extend([60, 70])
print(numbers)

numbers.remove(30)
print(numbers)

removed_element = numbers.pop()
print(removed_element)
print(numbers)

index_value = numbers.index(25)
print(index_value)

count_value = numbers.count(20)
print(count_value)

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

copied_list = numbers.copy()
print(copied_list)

numbers.clear()
print(numbers)
