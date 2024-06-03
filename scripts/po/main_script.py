from os import listdir
from os.path import isfile, join
import requests
import parse_po as parse
import sys
sys.path.append('../..')
from scripts import translate as translate
from scripts import fusion_data as fusion_data
from scripts import push_data_to_db as push

path = "../../files_input"

# files = [f for f in listdir(path) if isfile(join(path, f))]
files = ["en_GB.po"]

for file in files:
    print(f"\n{file}")
    file_name = file[:file.find(".po")]

    # Create a category 
    json_data = {"title": file}
    req = requests.post("http://127.0.0.1:8000/api/category", json=json_data)
    print(req.json())

    # Parse a po-file 
    print("-----------")
    print("Parse a file")
    data = parse.parse(category_id=req.json()["id"], file_name=file_name)
    
    # Translate data with using Google Translater
    print("-----------")
    print("Translate")
    translate.translate(file_name=file_name)

    # Fusion data from dict and xlsx to new dictionary
    print("-----------")
    print("Fusion data")
    f_data = fusion_data.fusion(file_name=file_name, data=data)

    # Push data to db
    print("-----------")
    print("Push data to db")
    push.push(data=f_data)