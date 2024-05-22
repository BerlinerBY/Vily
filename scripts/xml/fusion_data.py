import json
import pandas as pd
import numpy as np

name = "steamdeck.string_table"

df = pd.read_excel(f"../../xlsx_files/{name}.xlsx")

bel_arr = df[' eng_version_for_tr'].to_list()

data = []

with open(f"../../json_temp/{name}.json", "r") as file:
    data = json.load(file)

if len(bel_arr) == len(data):
    print(f"{len(bel_arr)} == {len(data)}")
    for i in range(len(data)):
        data[i]["bel_version"] = bel_arr[i].strip()
else:
    print(f"{len(bel_arr)} != {len(data)}")

with open(f'../../json_files/{name}.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)