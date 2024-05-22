from lxml import etree
import requests
import json

def get_categories():
    req = requests.get("http://127.0.0.1:8000/api/categories")
    data = req.json()
    return data

def get_data(category_id: int):
    req = requests.get(f"http://127.0.0.1:8000/api/category/{category_id}")
    data = req.json()
    return data

def add_data_to_xml(filename, data):
    # Parse the existing XML file
    tree = etree.parse(f'../../xml_files/{filename}')
    root = tree.getroot()

    # Create a new language element
    new_language = etree.SubElement(root, "language", {"id": "belarus"})

    # Create new entry elements
    for elem in data:
        new_entry1 = etree.SubElement(new_language, "entry", {"id": elem["xml_id"]})
        new_entry1.text = etree.CDATA(elem["bel_version"])
    
    # Check existing entries and preserve CDATA formatting
    for language_elem in root.findall("language"):
        for entry_elem in language_elem.findall("entry"):
            try:
                entry_elem.text = etree.CDATA(entry_elem.text)
            except TypeError:
                entry_elem.text = "There is an empty entry"

    # Append the new language element to the root
    root.append(new_language)

    etree.indent(root)

    # Write the updated XML tree to the file
    output_tree = etree.ElementTree(root)
    output_tree.write(f'../../xml_files_output/{filename}', pretty_print=True, xml_declaration=True, encoding="utf-8")

    return True

print(f"Start")
for elem in get_categories():
    c_id = elem["id"]
    c_title = elem["title"]
    data = get_data(elem["id"])

    print(f"    ------------")
    print(f"    {c_id} --- {len(data)} --- {c_title}")

    if not add_data_to_xml(c_title, data):
        print(f"    Something went wrong")
        print(f"    c_title: {c_title}")
        break

    print(f"    Writed")

print(f"Done")