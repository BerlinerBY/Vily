import requests
import json

name = "miscellaneous.string_table"

print("Open file")
with open(f"json_files/{name}.json", "r") as file:
    data = json.load(file)

print("Load data")
req = requests.post("http://127.0.0.1:8000/api/items/upload", json=data)
print(req.json())