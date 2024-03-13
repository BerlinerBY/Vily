import xml.etree.ElementTree as ET
from lxml import etree
import pandas as pd
import numpy as np

col_type = [
    ('id_item', 'str'), 
    ('bel_version', 'str'), 
    ('eng_version', 'str'), 
    ('ru_version', 'str')
    ]

df = pd.DataFrame(np.empty(0, dtype=col_type))

print(df)

tree = etree.parse("xml_files/curios.string_table.xml")
root = tree.getroot()
print(len(root[0]))

for i in range(len(root[0])):
    row = {
        "id_item": tree.xpath('//root/language[@id="english"]/entry/@id')[i],
        "bel_version": tree.xpath('//root/language[@id="belarus"]/entry')[i].text,
        "eng_version": tree.xpath('//root/language[@id="english"]/entry')[i].text,
        "ru_version": tree.xpath('//root/language[@id="russian"]/entry')[i].text,
    }
    df.loc[len(df)] = row

print(df)
df.to_excel("curios_table.xlsx")
print('Done')
