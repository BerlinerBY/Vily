# Алгарытм перакладу
## 1. Збор данных

1. Адкрываем файл `parse_xml_to_xlsx_and_json.py`. І мяняем у ім палі _category_id_ і _name_. 

2. Запускаем файл `parse_xml_to_xlsx_and_json.py` 

    ```
    python parse_xml_to_xlsx_and_json.py
    ```

3. Генеруем json-файл фармату і захоўваем у дырэкторыю json_temp:

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

1. Адкрываем файл `fusion_data.py` і мяняем у ім поле _name_.

2. Запускаем файл `fusion_data.py`
    ```
    python fusion_data.py
    ```
    Каб скампанаваць вынікі папярэдніх крокаў у адзіны json-файл фармата: 
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

## 4. Закідваем файл ў базу данных

- Дадаць катэгорыю у базу данных.

    ```JSON
    {
        "title": "heroes.string_table.xml",
        "date_updated": "2024-03-21T17:08:03",
        "id": 3
    }
    ``` 
- Адкрыць файл `push_data_to_db.py` і памяняць _name_.
- Запусціць `push_data_to_db.py`
    ```
    python push_data_to_db.py
    ```

    ```JSON
    {
        'status_code': 200, 
        'detail': {'status': '200', 'msg': 'Successfully'}, 
        'headers': None
    }
    ```

## 5. Спампоўваем данныя з БД і запісваем іх у новыя xml-файлы

1. Запускаем файл `write_output_xml.py`


## P.S. 
### На ўсякі выпадак раю зрабіць просценькую праверку паміж старымі і новымі файламі

Для гэтага трэба скарыстацца `find_diff.py`

Мне гэта спатрэбілася, бо я пачынаў рабіць пераклад з не сцімаўскай версіі гульні. У выніку атрымаў такі вывад (_пісаўся скрыпт хутка, таму доўга апроцоўвае вялікія файлы_):

```
(env) user@user: (path)$ python find_diff.py
Old xml-files --- 16
New xml-files --- 16
iOS.string_table.xml : old - 121, new - 121
121---121
old --- []
new --- []
-----------
backertrinkets.string_table.xml : old - 293, new - 293
293---293
old --- []
new --- []
-----------
miscellaneous.string_table.xml : old - 4045, new - 4047
4045---4047
old --- []
new --- ['buff_rule_tooltip_attacking_monster_type', 'buff_rule_tooltip_monster_type_count_min']
-----------
workshop.string_table.xml : old - 2, new - 2
2---2
old --- []
new --- []
-----------
dialogue.string_table.xml : old - 6302, new - 6302
6302---6302
old --- []
new --- []
-----------
curios.string_table.xml : old - 433, new - 433
433---433
old --- []
new --- []
-----------
apple_inapps.string_table.xml : old - 17, new - 17
17---17
old --- []
new --- []
-----------
steamdeck.string_table.xml : old - 147, new - 147
147---147
old --- []
new --- []
-----------
journal.string_table.xml : old - 46, new - 46
46---46
old --- []
new --- []
-----------
heroes.string_table.xml : old - 577, new - 577
577---577
old --- []
new --- []
-----------
arena_base.string_table.xml : old - 65, new - 65
65---65
old --- []
new --- []
-----------
switch.string_table.xml : old - 218, new - 218
218---218
old --- []
new --- []
-----------
PSN.string_table.xml : old - 509, new - 509
509---509
old --- []
new --- []
-----------
party_names.string_table.xml : old - 411, new - 411
411---411
old --- []
new --- []
-----------
xb1.string_table.xml : old - 194, new - 194
194---194
old --- []
new --- []
-----------
names.string_table.xml : old - 562, new - 562
562---562
old --- []
new --- []
-----------

```