import { setItem, setItemToItems, setItems } from "../slices/content/contentSlice";

export function getItemsRequest(categoryID, dispatch) {
    const requestOptions = {
        method: 'GET',
        headers: {
            'Accept': 'application/json',
        },
    };

    fetch('http://127.0.0.1:8000/api/category/' + categoryID, requestOptions)
        .then(response => {
            return response.json();
        })
        .then(data => {
            dispatch(setItems(data));
        })
        .catch(error => {
            console.error(error);
        })
};

export function updateItemRequest(index, itemID, bel_version, dispatch) {
    const requestOptions = {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(
            {
                readiness: true,
                bel_version: bel_version
            }
        )
    };
    fetch("http://127.0.0.1:8000/api/items/update/" + itemID, requestOptions)
        .then(response => response.json())
        .then(data => {
            dispatch(setItem(data));
            dispatch(setItemToItems({'index': index, 'data': data}));
        })
        .catch(error => error)
};