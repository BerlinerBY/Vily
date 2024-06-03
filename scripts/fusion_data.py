import json
import pandas as pd

def fusion(file_name: str, data: dict):
    df = pd.read_excel(f"../../xlsx_files/{file_name}.xlsx")

    bel_arr = df[' lang_version_for_tr'].to_list()

    if len(bel_arr) == len(data):
        print(f"    {len(bel_arr)} == {len(data)}")
        for i in range(len(data)):
            try:
                data[i]["bel_version"] = bel_arr[i].strip()
            except AttributeError:
                print(f"bel_arr[i]: {bel_arr[i]}")
    else:
        print(f"    {len(bel_arr)} != {len(data)}")

    return data