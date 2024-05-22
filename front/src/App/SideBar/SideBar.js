import { useEffect, useState } from 'react';
import './SideBar.css';
import { useDispatch, connect } from 'react-redux';
import { getCategoryRequest } from "../../features/ApiRequests/SideBarRequests";
import xml_icon from './xml.png'
import { setCategoryID, setCategoryName } from '../../features/slices/category/categorySlice';
import { setDefaultItem } from '../../features/slices/content/contentSlice';

function SideBar({categoryFromStore}) {
    const categories = categoryFromStore;
    const dispatch = useDispatch();
    const [categoryButtonID, setCategoryButtonID] = useState(0);

    const handleClick = (categoryID, title) => {
        // don't forget set !important for :hover and :active
        if (categoryButtonID !== 0) {
            document.getElementById('category_button_' + categoryButtonID).style.backgroundColor='';
        }
        dispatch(setCategoryID(categoryID));
        dispatch(setCategoryName(title));
        dispatch(setDefaultItem());
        document.getElementById('category_button_' + categoryID).style.backgroundColor="#232323";
        setCategoryButtonID(categoryID);
    };

    const convertData = (data) => {
        let new_data = data.split("T")[0].split("-");
        return new_data.reverse().join("/");
    };

    useEffect(() => {
        getCategoryRequest(dispatch);
    // eslint-disable-next-line
    }, []);

    return (
        <>
            <div className="CategoryBlock">
                {categories.length > 0 && (
                    <div>
                        {categories.map(category => (
                            <div key={category.id} className="SideBar-category">
                                <div className='SideBar-category-button' 
                                    role='button'
                                    id={'category_button_' + category.id}
                                    onClick={() => {
                                        handleClick(category.id, category.title);
                                    }}>
                                    <div className="Icon-button">
                                        <img src={xml_icon} className="SideBar-icon" alt="icon" />
                                    </div>
                                    <div className='Name-button'>
                                        <div className='Name-button-title'>{category.title}</div>
                                        <div className='Name-button-change_date'>{convertData(category.date_updated)}</div>
                                    </div>
                                </div>
                            </div>
                        ))}
                    </div>        
                )}
            </div>
        </>
    )
}

function displayStateToProps(state) {
    return {
        categoryFromStore: state.categoryReducer.categories,
    };
}


export default connect(displayStateToProps)(SideBar);        