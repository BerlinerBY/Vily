# Алгарытм перакладу
## 1. Збор дадзеных

Запускаем `parse_xml_to_xlsx_and_json.py` 

1. Генеруем json-файл фармату і захоўваем у дырэкторыю json_temp:

```JSON
[
    {
        "xml_id": "str_curio_content_nothing",
        "eng_version": "Error - no curio found!",
        "ru_version": "Ошибка: диковинка не найдена!",
        "category_id": 1
    },
    {
        "xml_id": "str_curio_no_negative_quirks_to_remove",
        "eng_version": "No negative quirks to remove.",
        "ru_version": "Негативных черт нет.",
        "category_id": 1
    },
    ...
]
```
2. Генеруем xlsx-файл фармату і захоўваем у дырэкторыю xlsx_files_temp:

|   | xml_id                                              | eng_version_for_tr                                  | category_id |
|---|-----------------------------------------------------|-----------------------------------------------------|-------------|
| 0 | str_curio_title_nothing                             | Error - no curio found!                             | 1           |
| 1 | str_curio_content_nothing                           | Error - no curio found!                             | 1           |
| 2 | str_curio_no_negative_quirks_to_remove              | No negative quirks to remove.                       | 1           |
| 3 | str_curio_title_bandits_trapped_chest               | Bandit's Trapped Chest                              | 1           |
| 4 | str_curio_content_bandits_trapped_chest             | Something doesn't look quite right with this one... | 1           |
| 5 | str_curio_tooltip_investigate_bandits_trapped_chest | Open the chest...                                   | 1           |

## 2. "Машынны" пераклад
Бяром xlsx-файл і ідзем на Google Перакладчык. Абіраем `Дакументы`. Перакладаем яго, спампоўваем і кладзем яго ў дырэкторыю xlsx_files.

|   | xml_id                                               |  eng_version_for_tr                               |  category_id |
|---|------------------------------------------------------|---------------------------------------------------|--------------|
| 0 |  str_curio_title_nothing                             |  Памылка - кур'ёз не знойдзены!                   | 1            |
| 1 |  str_curio_content_nothing                           |  Памылка - кур'ёз не знойдзены!                   | 1            |
| 2 |  str_curio_no_negative_quirks_to_remove              |  Няма негатыўных дзівацтваў, якія трэба выдаліць. | 1            |
| 3 |  str_curio_title_bandits_trapped_chest               |  Куфар бандыта ў пастцы                           | 1            |
| 4 |  str_curio_content_bandits_trapped_chest             |  З гэтым нешта не так...                          | 1            |
| 5 |  str_curio_tooltip_investigate_bandits_trapped_chest |  Адкрыйце куфар...                                | 1            |

## 3. Зброрка вынікаў у json-файл

Запускаем файл `fusion_data.py`. Каб скампанаваць вынікі папярэдніх крокаў у адзіны json-файл фармата: 
```JSON
[
    {
        "xml_id": "str_curio_knife_rack_effect",
        "eng_version": "The hero receives a nasty gash.",
        "ru_version": "Герой сильно порезался.",
        "category_id": 1,
        "bel_version": "Герой атрымлівае непрыемную рану."
    },
    {
        "xml_id": "str_curio_knife_rack_bandage_loot",
        "eng_version": "The bandage protects the hero's hands during the search.",
        "ru_version": "Повязка защищает руки героя во время осмотра.",
        "category_id": 1,
        "bel_version": "Павязка абараняе рукі героя падчас пошукаў."
    },
]
```

## 4. Закідваем файл ў базу дадзеных

- Дадаць катэгорыю у базу дадзеных.

```JSON
{
    "title": "heroes.string_table.xml",
    "date_updated": "2024-03-21T17:08:03",
    "id": 3
}
``` 

- Выкарстаць `push_data_to_bd.py`
```JSON
{
    'status_code': 200, 
    'detail': {'status': '200', 'msg': 'Successfully'}, 
    'headers': None
}
```