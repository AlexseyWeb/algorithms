"""
Working with JSON format on Python

"""
import json

try:
    json_str = '{"name": "Alexsey", "age": 33, "sallary": 124000, "status":{"rating": 20, "stroke": true}}'

    man = json.loads(json_str)
except json.JSONDecodeError as err:
    print(err)

print(type(man))
for k, v in man.items():
    print(f"key -> {k} and value -> {v}")

# convert dictionary into json format
mans = {"name": "Sergey", "age": 29, "sallary": 180000, "children": [], }
json_mans = json.dumps(mans, indent=4)
print(type(json_mans))
print(json_mans)
