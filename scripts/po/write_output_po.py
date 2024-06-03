import requests
import polib

def get_categories():
    req = requests.get("http://127.0.0.1:8000/api/categories")
    data = req.json()
    return data

def get_data(category_id: int):
    req = requests.get(f"http://127.0.0.1:8000/api/category/{category_id}")
    data = req.json()
    return data

def create_po(data):
    po = polib.POFile()
    po.metadata = {
        'Project-Id-Version': '1.0',
        'Report-Msgid-Bugs-To': 'you@example.com',
        'POT-Creation-Date': '2007-10-18 14:00+0100',
        'PO-Revision-Date': '2007-10-18 14:00+0100',
        'Last-Translator': 'you <you@example.com>',
        'Language-Team': 'English <yourteam@example.com>',
        'MIME-Version': '1.0',
        'Content-Type': 'text/plain; charset=utf-8',
        'Content-Transfer-Encoding': '8bit',
    }
    
    for i in range(len(data)):
        po_d = polib.pofile(
            data[i]["context"]
        )

        entry = polib.POEntry(
            msgid=data[i]["item_id"],
            msgstr=data[i]["bel_version"],
            occurrences=po_d[0].occurrences,
            comment=po_d[0].comment,
            flags=po_d[0].flags,
        )
        print(entry)
        po.append(entry)
    
    po.save("../../files_output/be.po")


print(f"Start")
for elem in get_categories():
    c_id = elem["id"]
    c_title = elem["title"]
    data = get_data(c_id)

    print(f"    ------------")
    print(f"    {c_id} --- {len(data)} --- {c_title}")

    if not create_po(data=data):
        print(f"    Something went wrong")
        print(f"    c_title: {c_title}")
        break

    print(f"    Writed")

print(f"Done")