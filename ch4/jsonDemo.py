import json

strJson = "{ \"name\": \"Aks\\\"hay\", \"lastname\": \"Dandekar\" }"

strJson = '{ "fullname": { "name": "Akshay", "surname": "dandekar" }, "age": 29 }'

print(strJson)



strTest = "sjdkbjks\"dhgdj"
nameDictionary = json.loads(strJson)


print(nameDictionary)
print(nameDictionary["name"])