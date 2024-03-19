import { configureStore } from '@reduxjs/toolkit';
import categoryReducer from '../features/slices/category/categorySlice';
import contentReducer from '../features/slices/content/contentSlice';

export default configureStore({
    reducer: {
        categoryReducer: categoryReducer,
        contentReducer: contentReducer,
    },
})