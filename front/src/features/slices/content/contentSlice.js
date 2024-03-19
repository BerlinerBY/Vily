import { createSlice } from '@reduxjs/toolkit';

export const contentSlice = createSlice({
    name: 'contentSlicer',
    initialState: {
        items: [],
        selectedItemIndex: 0,
        selectedItem: [],
    },
    reducers: {
        setItems: (state, action) => {
            state.items = action.payload;
        },
        setItemToItems: (state, action) => {
            state.items[action.payload['index']] = action.payload['data'];
        },
        setItemIndex: (state, action) => {
            state.selectedItemIndex = action.payload;
        },
        setItem: (state, action) => {
            state.selectedItem = action.payload;
        },
        setDefaultItem: (state, action) => {
            state.selectedItem = [];
            state.selectedItemIndex = 0;
        },
        setPreviousItem: (state, action) => {
            if (action.payload - 1 >= 0) {
                state.selectedItemIndex = action.payload - 1;
                state.selectedItem = state.items[action.payload - 1];
            }
        },
        setNextItem: (state, action) => {
            if (action.payload + 1 <= state.items.length - 1) {
                state.selectedItemIndex = action.payload + 1;
                state.selectedItem = state.items[action.payload + 1];
            }
        },
    },
})

export const {setItems, setItemIndex, setItem, setDefaultItem, 
                setPreviousItem, setNextItem, setItemToItems} = contentSlice.actions

export default contentSlice.reducer