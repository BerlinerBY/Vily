import { useEffect, useState } from 'react';
import './Main.css'
import { useDispatch, connect } from 'react-redux';
import { getItemsRequest } from '../../features/ApiRequests/MainRequests';
import MainItem from './MainItem/MainItem';
import no_image from './no.png';
import yes_image from './yes.png';
import { setItemIndex, setItem } from '../../features/slices/content/contentSlice';

function Main({selectedCategoryFromStore, itemsFromStore}) {
    const items = itemsFromStore;
    const selectedCategory = selectedCategoryFromStore;
    const dispatch = useDispatch();
    const [itemButtonID, setItemButtonID] = useState(-1);

    const changeBackground = (itemIndex) => {
        // don't forget set !important for :hover and :active
        if (itemButtonID !== -1) {
            document.getElementById('item_button_' + itemButtonID).style.backgroundColor='';
        }
        document.getElementById('item_button_' + itemIndex).style.backgroundColor="#232323";
        setItemButtonID(itemIndex);        
    };

    const changeItem = (item, itemIndex) => {
        dispatch(setItem(item));
        dispatch(setItemIndex(itemIndex));
    };

    const handleClick = (item, itemIndex) => {
        changeBackground(itemIndex);
        changeItem(item, itemIndex);
    };

    const convertData = (data) => {
        let new_data = data.split("T")[0].split("-");
        return new_data.reverse().join("/");
    };

    const formatTitle = (title) => {
        if (title.length < 41) {
            return title;
        } else {
            return (title.substr(0, 41) + '...');
        }
    };

    useEffect(() => {
        getItemsRequest(selectedCategory, dispatch);
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [selectedCategory])

    const chooseContent = () => {
        if (selectedCategory === 0) {
            return (
                <div className='Main-Welcome'>
                    <h1>Welcome</h1>
                    <h3>Select the file you want</h3>
                </div>
            )
        } else {
            return (
                <div className='Main-container'>
                    <div className='Main-item'>
                        <MainItem 
                            changeBackground={changeBackground}
                            itemsLength={items.length}/>
                    </div>
                    <div className='Main-content'>
                        {items.length ? 
                            (items.length > 0 && (
                                <>
                                    <div className='Main-content-count'>Element count: {items.length}</div>
                                    <div className='Main-content-items'>
                                        {items.map((item, index) => (
                                            <div key={item.id} className='Content-item-body'
                                                role='button'
                                                id={'item_button_' + index}
                                                onClick={() => {
                                                    handleClick(item, index);
                                                }}>
                                                <div className='item-body-image'>
                                                    {item.readiness ? 
                                                        <img src={yes_image} alt=''/> 
                                                        : 
                                                        <img src={no_image} alt=''/>}
                                                </div>
                                                <div className='item-body-text'>
                                                    <div className='eng_version'>{formatTitle(item.eng_version)}</div>
                                                    <div className='change_date'>{convertData(item.date_updated)}</div>
                                                </div>
                                            </div>
                                        ))}
                                    </div>
                                </>
                            ))
                            : 
                            <div className='Main-content-count'>There isn't any item</div>}
                    </div>
                </div>
            )
        }
    }

    return (
        <>
            <div className='MainBlock'>
                {chooseContent()}
            </div>
        </>
    )
};


function displayStateToProps(state) {
    return {
        selectedCategoryFromStore: state.categoryReducer.selectedСategory,
        itemsFromStore: state.contentReducer.items,
    };
};

export default connect(displayStateToProps)(Main);

