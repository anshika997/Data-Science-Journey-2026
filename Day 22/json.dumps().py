import json

data = {
    "name": "Anshika",
    "age": 20,
    "branch": "CSE"
}

json_data = json.dumps(data)
print(json_data)
print(type(json_data))
