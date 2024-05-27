import requests
import json

def push(data: list):
    print("    Load data")
    req = requests.post("http://127.0.0.1:8000/api/items/upload", json=data)
    print(req.json())