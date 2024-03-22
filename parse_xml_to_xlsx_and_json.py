import xml.etree.ElementTree as ET
from lxml import etree
import time
import pandas as pd
import numpy as np

t0 = time.time()
print("Open file")

### IMPORTANT
category_id = 3
name = "heroes.string_table"

tree = etree.parse(f"xml_files/{name}.xml")
root = tree.getroot()

col_type = [
    ('xml_id', 'str'), 
    ('eng_version_for_tr', 'str'), 
    ('category_id', 'int')
    ]
df = pd.DataFrame(np.empty(0, dtype=col_type))

data = []

print("Parse data")
for i in range(len(root[0])):
    if i % 100 == 0:
        print(i)
    id = tree.xpath('//root/language[@id="english"]/entry/@id')[i]
    row_for_df = {
        "xml_id": id,
        "eng_version_for_tr":tree.xpath(f'//root/language[@id="english"]/entry[@id="{id}"]')[0].text,
        "category_id": 1
    }
    df.loc[len(df)] = row_for_df

    try:
        row = {
            "xml_id": id, 
            "eng_version": tree.xpath(f'//root/language[@id="english"]/entry[@id="{id}"]')[0].text,
            "ru_version": tree.xpath(f'//root/language[@id="russian"]/entry[@id="{id}"]')[0].text,
            "category_id": category_id
        }
    except IndexError:
        row = {
            "xml_id": id, 
            "eng_version": tree.xpath(f'//root/language[@id="english"]/entry[@id="{id}"]')[0].text,
            "ru_version": tree.xpath(f'//root/language[@id="english"]/entry[@id="{id}"]')[0].text,
            "category_id": category_id
        }
    data.append(row)

print('Save data to xlsx')
df.to_excel(f"xlsx_files_temp/{name}.xlsx")

print('Save data to json')
import json
with open(f'json_temp/{name}.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
t1 = time.time()
print(t1 - t0)
