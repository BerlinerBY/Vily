
export function search(items, flag, searchValue) {
    let searchList = [];

    for (let i = 0; i < items.length; i++) {
        if (items[i][flag]) {
            if (items[i][flag].toLowerCase().indexOf(searchValue.toLowerCase()) !== -1) {
                searchList.push(i);
            }
        }
    };

    return searchList;
}