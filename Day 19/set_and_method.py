data = {10, 20, 30, 40}

print(data)

data.add(50)
print(data)

data.update([60, 70])
print(data)

data.remove(30)
print(data)

removed_element = data.pop()
print(removed_element)
print(data)

data.discard(100)
print(data)

copy_set = data.copy()
print(copy_set)

data.clear()
print(data)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union_set = set1.union(set2)
print(union_set)

intersection_set = set1.intersection(set2)
print(intersection_set)

difference_set = set1.difference(set2)
print(difference_set)

symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)

print(set1.issubset(union_set))
print(set1.issuperset({1, 2}))
print(set1.isdisjoint({7, 8}))
