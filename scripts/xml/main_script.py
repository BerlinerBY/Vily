from os import listdir
from os.path import isfile, join
import requests
import parse_xml_to_xlsx_and_json as parse
import translate
import fusion_data
import push_data_to_db as push

path = "../../files_input"

files = [f for f in listdir(path) if isfile(join(path, f))]

for file in files:
    print(f"\n{file}")
    file_name = file[:file.find(".xml")]

    # Create a category 
    json_data = {"title": file}
    req = requests.post("http://127.0.0.1:8000/api/category", json=json_data)
    print(req.json())

    # Parse a xml-file 
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