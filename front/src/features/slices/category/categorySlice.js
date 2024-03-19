import { createSlice } from '@reduxjs/toolkit';


export const categorySlice = createSlice({
    name: 'categorySlicer',
    initialState: {
        categories: [],
        selectedСategory: 0,
        selectedСategoryName: "",
    },
    reducers: {
        setCategories: (state, action) => {
            state.categories = action.payload;
        },
        setCategoryID: (state, action) => {
            state.selectedСategory = action.payload;
        },
        setCategoryName: (state, action) => {
            state.selectedСategoryName = action.payload;
        },
    }
})

export const {setCategories, setCategoryID, setCategoryName} = categorySlice.actions

export default categorySlice.reducer