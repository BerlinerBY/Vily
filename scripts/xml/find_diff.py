import os
import xml.etree.ElementTree as ET
from lxml import etree

# Find difference between old and new xml-files from other various game versions 
#   (old GOG, new Steam)

old_path = "../../xml_files"
old_file_list = os.listdir(old_path)
print(f"Old xml-files --- {len(old_file_list)}")

new_path = "../../xml_files_steam"
new_file_list = os.listdir(new_path)
print(f"New xml-files --- {len(new_file_list)}")

for file_name in old_file_list:
    old_tree = etree.parse(f"{old_path}/{file_name}")
    old_root = old_tree.getroot()
    new_tree = etree.parse(f"{new_path}/{file_name}")
    new_root = new_tree.getroot()
    print(f"{file_name} : old - {len(old_root[0])}, new - {len(new_root[0])}")

    old_id_list = [
        old_tree.xpath('//root/language[@id="english"]/entry/@id')[i] 
        for i in range(len(old_root[0]))
        ]
    
    new_id_list = [
        new_tree.xpath('//root/language[@id="english"]/entry/@id')[i] 
        for i in range(len(new_root[0]))
        ]
    print(f"{len(old_id_list)}---{len(new_id_list)}")

    dict_of_diff = {
        "old": [],
        "new": [],
    }

    for id in old_id_list:
        if id not in new_id_list:
            print(f"+++++ {id}")
            dict_of_diff["old"].append(id)
    
    for id in new_id_list:
        if id not in old_id_list:
            dict_of_diff["new"].append(id)

    for key, value in dict_of_diff.items():
        print(f"{key} --- {value}")


    print("-----------")
