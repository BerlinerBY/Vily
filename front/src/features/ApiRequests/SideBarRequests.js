import { setCategories } from "../slices/category/categorySlice";

export function getCategoryRequest(dispatch) {
    const requestOptions = {
        method: 'GET',
        headers: {
            'Accept': 'application/json',
        },
    };

    fetch("http://127.0.0.1:8000/api/categories", requestOptions)
        .then(response => {
            return response.json();
        })
        .then(data => dispatch(setCategories(data)))
        .catch(error => {
            console.error(error);
        });
}