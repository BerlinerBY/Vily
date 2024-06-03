import xml.etree.ElementTree as ET
from lxml import etree
import pandas as pd
import numpy as np

def parse(category_id: int, file_name: str):
    print("    Open file")

    # Change it to set other language
    first_lang = "english"
    second_lang = "russian"

    tree = etree.parse(f"../../files_input/{file_name}.xml")
    root = tree.getroot()

    col_type = [
        ('item_id', 'str'), 
        ('lang_version_for_tr', 'str'), 
        ('category_id', 'int')
        ]
    df = pd.DataFrame(np.empty(0, dtype=col_type))

    data = []

    print("    Parse data")
    i = 0
    while i < len(root[0]):
        if i % 100 == 0:
            print(f"    Progress: {i} or {(i/len(root[0])) * 100}%")
        id = tree.xpath(f'//root/language[@id="{first_lang}"]/entry/@id')[i]

        if len(tree.xpath(f'//root/language[@id="{first_lang}"]/entry[@id="{id}"]')) > 1:
            first_item = tree.xpath(f'//root/language[@id="{first_lang}"]/entry[@id="{id}"]')
            second_item = tree.xpath(f'//root/language[@id="{second_lang}"]/entry[@id="{id}"]')
            for y in range(len(first_item)):
                row_for_df = {
                    "item_id": id,
                    "lang_version_for_tr": first_item[y].text,
                    "category_id": category_id
                }
                df.loc[len(df)] = row_for_df

                try:
                    row = {
                        "item_id": id, 
                        "first_version": first_item[y].text,
                        "second_version": second_item[y].text,
                        "category_id": category_id
                    }
                except IndexError:
                    row = {
                        "item_id": id, 
                        "first_version": first_item[y].text,
                        "second_version": first_item[y].text,
                        "category_id": category_id
                    }
                data.append(row)
            i += len(tree.xpath(f'//root/language[@id="{first_lang}"]/entry[@id="{id}"]'))
        else:
            row_for_df = {
                "item_id": id,
                "lang_version_for_tr":tree.xpath(f'//root/language[@id="{first_lang}"]/entry[@id="{id}"]')[0].text,
                "category_id": category_id
            }
            df.loc[len(df)] = row_for_df

            try:
                row = {
                    "item_id": id, 
                    "first_version": tree.xpath(f'//root/language[@id="{first_lang}"]/entry[@id="{id}"]')[0].text,
                    "second_version": tree.xpath(f'//root/language[@id="{second_lang}"]/entry[@id="{id}"]')[0].text,
                    "category_id": category_id
                }
            except IndexError:
                row = {
                    "item_id": id, 
                    "first_version": tree.xpath(f'//root/language[@id="{first_lang}"]/entry[@id="{id}"]')[0].text,
                    "second_version": tree.xpath(f'//root/language[@id="{first_lang}"]/entry[@id="{id}"]')[0].text,
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
