import { useEffect, useState } from 'react';
import './Main.css'
import { useDispatch, connect } from 'react-redux';
import { getItemsRequest } from '../../features/ApiRequests/MainRequests';
import MainItem from './MainItem/MainItem';
import SearchPanel from './SearchPanel/SearchPanel';
import no_image from './icons/no.png';
import yes_image from './icons/yes.png';
import search_image from './icons/search.png';
import { setItemIndex, setItem } from '../../features/slices/content/contentSlice';
import { setPreviousItem, setNextItem } from '../../features/slices/content/contentSlice';
import MWSearch from './MWSearch/MWSearch';
import { search } from './MWSearch/Search';

function Main({selectedCategoryFromStore, itemsFromStore, selectedItemIndexFromStore}) {
    const items = itemsFromStore;
    const selectedCategory = selectedCategoryFromStore;
    const dispatch = useDispatch();
    const [itemButtonID, setItemButtonID] = useState(-1);
    const index = selectedItemIndexFromStore;
    const [showSearchPanel, setShowSearchPanel] = useState(true);
    const [showMWSearch, setShowMWSearch] = useState(false);
    const [searchResultList, setSearchResultList] = useState([]);
    const [searchValue, setSearchValue] = useState([]);
    const [xml_flag, setXml_flag] = useState('');

    const changeBackground = (itemIndex) => {
        if (itemButtonID !== -1) {
            document.getElementById('item_button_' + itemButtonID).style.backgroundColor='';
        }
        document.getElementById('item_button_' + itemIndex).style.backgroundColor="#232323";
        setItemButtonID(itemIndex);
    };

    const goToItem = (index) => {
        document.getElementById('item_button_' + index).scrollIntoView({ behavior: "smooth", block: "center"});
    };

    const handlePreviousItem = () => {
        if (index - 1 >= 0) {
            dispatch(setPreviousItem(index));
            // document.getElementById('item_button_' + (index - 1)).scrollIntoView({ behavior: "smooth", block: "center"});
            goToItem(index - 1);
            changeBackground(index - 1);
        }
    };
    const handleNextItem = () => {
        if (index + 1 <= items.length - 1) {
            dispatch(setNextItem(index));
            // document.getElementById('item_button_' + (index + 1)).scrollIntoView({ behavior: "smooth", block: "center"});
            goToItem(index + 1);
            changeBackground(index + 1);
        }
    };

    const changeItem = (itemIndex) => {
        dispatch(setItem(items[itemIndex]));
        dispatch(setItemIndex(itemIndex));
    };

    const changeItemBySearch = (itemIndex) => {
        changeItem(itemIndex);
        goToItem(itemIndex);
        changeBackground(itemIndex);
    };
    const transferDataToSearch = (flag, value) => {
        // get data from MWSearch and transfet it to SearchPanel
        // enable SearchPanel
        setXml_flag(flag)
        var list = search(items, flag, value);

        if (list.length !== 0) {
            setSearchResultList(list);
            setSearchValue(value)
            setShowSearchPanel(true);
        } else {
            alert("Coincidences doesn't exist");
        }
    };


    const handleClickItem = (itemIndex) => {
        changeBackground(itemIndex);
        changeItem(itemIndex);
    };
    const handleClickSearch = () => {
        setShowMWSearch(true);
        setShowSearchPanel(false);
    };
    const handleCloseSearchPanel = () => {
        setShowSearchPanel(false);
    };
    const handleCloseMWSearch = () => {
        setShowMWSearch(false);
    }

    const convertData = (data) => {
        let new_data = data.split("T")[0].split("-");
        return new_data.reverse().join("/");
    };

    window.addEventListener('keydown', function (event) {
        if (event.key === "ArrowDown") {
            handleNextItem();
        } else if (event.key === "ArrowUp") {
            handlePreviousItem();
        }
      }, {once: true});

    useEffect(() => {
        setItemButtonID(-1);
        setShowSearchPanel(false);
        getItemsRequest(selectedCategory, dispatch);
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [selectedCategory]);

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
                            handlePreviousItem={handlePreviousItem}
                            handleNextItem={handleNextItem}
                            />
                    </div>
                    <div className='Main-content'>
                        {items.length ? 
                            (items.length > 0 && (
                                <>
                                    <div className='Main-content-count'>
                                        <MWSearch transferDataToSearch={transferDataToSearch}
                                                  handleCloseMWSearch={handleCloseMWSearch}
                                                  showMWSearch={showMWSearch}
                                                  items={items}/>
                                        <div>Element count: {items.length}</div>
                                        <div className='Main-content-count-search_button'
                                            role='button'
                                            onClick={() => {
                                                handleClickSearch();
                                            }}>
                                            <img src={search_image} alt=''/>
                                        </div>
                                    </div>
                                    {showSearchPanel ? 
                                            <div className='Main-content-search'>
                                                <SearchPanel
                                                    handleCloseSearchPanel={handleCloseSearchPanel}
                                                    transferDataToSearch={transferDataToSearch}
                                                    changeItemBySearch={changeItemBySearch}
                                                    searchResultList={searchResultList}
                                                    searchValue={searchValue}
                                                    xml_flag={xml_flag}/>
                                            </div>
                                            :
                                            <></>}
                                    <div className={showSearchPanel ? 
                                                        "Main-content-items Panel-enable" 
                                                        : 
                                                        "Main-content-items Panel-disable"}>
                                        {items.map((item, index) => (
                                            <div key={item.id} className='Content-item-body'
                                                role='button'
                                                id={'item_button_' + index}
                                                onClick={() => {
                                                    handleClickItem(index);
                                                }}>
                                                <div className='item-body-image'>
                                                    {item.readiness ? 
                                                        <img src={yes_image} alt=''/> 
                                                        : 
                                                        <img src={no_image} alt=''/>}
                                                </div>
                                                <div className='item-body-text'>
                                                    <div className='item-body-text-eng_version'>{item.eng_version}</div>
                                                    <div className='item-body-text-change_date'>{convertData(item.date_updated)}</div>
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
        selectedItemIndexFromStore: state.contentReducer.selectedItemIndex,
    };
};

export default connect(displayStateToProps)(Main);

