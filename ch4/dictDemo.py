import json

test = { "name": "Akshay", "age": 29, "nested": {"key1": "val1", "key2": "val2"} }

strJson = json.dumps(test)
print(strJson)

print(test["name"])
print(test["age"])

