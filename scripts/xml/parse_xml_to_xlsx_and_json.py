import xml.etree.ElementTree as ET
from lxml import etree
import time
import pandas as pd
import numpy as np
import json



def parse(category_id: int, file_name: str):
    print("    Open file")

    tree = etree.parse(f"../../files_input/{file_name}.xml")
    root = tree.getroot()

    col_type = [
        ('xml_id', 'str'), 
        ('eng_version_for_tr', 'str'), 
        ('category_id', 'int')
        ]
    df = pd.DataFrame(np.empty(0, dtype=col_type))

    data = []

    print("    Parse data")
    i = 0
    while i < len(root[0]):
        if i % 100 == 0:
            print(f"    Progress: {i} or {(i/len(root[0])) * 100}%")
        id = tree.xpath('//root/language[@id="english"]/entry/@id')[i]

        if len(tree.xpath(f'//root/language[@id="english"]/entry[@id="{id}"]')) > 1:
            eng_item = tree.xpath(f'//root/language[@id="english"]/entry[@id="{id}"]')
            ru_item = tree.xpath(f'//root/language[@id="russian"]/entry[@id="{id}"]')
            for y in range(len(eng_item)):
                row_for_df = {
                    "xml_id": id,
                    "eng_version_for_tr": eng_item[y].text,
                    "category_id": category_id
                }
                df.loc[len(df)] = row_for_df

                try:
                    row = {
                        "xml_id": id, 
                        "eng_version": eng_item[y].text,
                        "ru_version": ru_item[y].text,
                        "category_id": category_id
                    }
                except IndexError:
                    row = {
                        "xml_id": id, 
                        "eng_version": eng_item[y].text,
                        "ru_version": eng_item[y].text,
                        "category_id": category_id
                    }
                data.append(row)
            i += len(tree.xpath(f'//root/language[@id="english"]/entry[@id="{id}"]'))
        else:
            row_for_df = {
                "xml_id": id,
                "eng_version_for_tr":tree.xpath(f'//root/language[@id="english"]/entry[@id="{id}"]')[0].text,
                "category_id": category_id
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

            i += 1





    print('    Save data to xlsx')
    df.to_excel(f"../../xlsx_files_temp/{file_name}.xlsx")

    # print('Save data to json')
    # with open(f'../../json_temp/{file_name}.json', 'w', encoding='utf-8') as f:
    #     json.dump(data, f, ensure_ascii=False, indent=4)

    return data
