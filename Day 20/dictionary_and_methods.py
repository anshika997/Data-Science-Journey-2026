data = {
    "name": "Anshika",
    "age": 20,
    "branch": "CSE"
}

print(data)

value = data.get("name")
print(value)

keys = data.keys()
print(keys)

values = data.values()
print(values)

items = data.items()
print(items)

data["college"] = "Sage University"
print(data)

data.update({"age": 21})
print(data)

removed_value = data.pop("branch")
print(removed_value)
print(data)

last_item = data.popitem()
print(last_item)
print(data)

copy_dict = data.copy()
print(copy_dict)

data.clear()
print(data)

dict1 = {"a": 1, "b": 2}
dict2 = dict(dict1)
print(dict2)

for key in dict1:
    print(key, dict1[key])
