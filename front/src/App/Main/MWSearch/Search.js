
export function search(items, flag, searchValue) {
    let searchList = [];

    for (let i = 0; i < items.length; i++) {
        if (items[i][flag].toLowerCase().indexOf(searchValue.toLowerCase()) !== -1) {
            searchList.push(i);
        }
    };

    return searchList;
}


// id(pin): 12379
// eng_version(pin): "Always Show Circus Tutorials"
// readiness(pin): false
// date_updated(pin): "2024-05-16T19:07:23"
// bel_version(pin): "Заўсёды паказваць падручнікі па цырку"
// xml_id(pin): "menu_options_element_always_show_circus_tutorials"
// ru_version(pin): "Всегда показывать обучение в цирке"
// data_created(pin): "2024-05-16T19:07:23"
// category_id(pin): 8