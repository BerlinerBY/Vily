import polib
import pandas as pd
import numpy as np

def parse(category_id: int, file_name: str):
    print("    Open file")


    pofile = polib.pofile(f"../../files_input/{file_name}.po")

    col_type = [
        ('item_id', 'str'), 
        ('lang_version_for_tr', 'str'), 
        ('category_id', 'int')
        ]
    df = pd.DataFrame(np.empty(0, dtype=col_type))

    data = []

    print("    Parse data")

    for entry in pofile:
        if entry.comment:
            print(f"#. {entry.comment}")
        if entry.occurrences:
            print(f"#: {entry.occurrences}")
        if entry.flags:
            print(f"#, fuzzy  {entry.flags}")
        print(entry.msgid)
        print(entry.msgstr)
        print("----------")
        print(entry)
        print("----------")
        print()

        row_for_df = {
            "item_id": entry.msgid,
            "lang_version_for_tr": entry.msgstr,
            "category_id": category_id
            }
        df.loc[len(df)] = row_for_df

        row = {
            "item_id": entry.msgid,
            "first_version": entry.msgstr,
            "category_id": category_id,
            "context": str(entry)
        }
        data.append(row)

    print('    Save data to xlsx')
    df.to_excel(f"../../xlsx_files_temp/{file_name}.xlsx")

    return data