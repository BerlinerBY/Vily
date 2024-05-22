import './SearchPanel.css';
import close_image from './cross.png';
import arrow_image from './arrow.png';
import search_image from '../icons/search.png'
import { useEffect, useState } from 'react';

function SearchPanel({searchResultList, searchValue, transferDataToSearch,
            handleCloseSearchPanel, changeItemBySearch, xml_flag}) {
    const [value, setValue] = useState(searchValue);
    const [selectedItem, setSelectedItem] = useState(0);

    const handleChangeSearchValue = (event) => {
        setValue(event.target.value);
    };

    const handleSearch = () => {
        setSelectedItem(0);
        transferDataToSearch(xml_flag, value);
    };

    const handlePreviousSearchItem = () => {
        if (searchResultList.length === 1) {
            setSelectedItem(1);
            changeItemBySearch(searchResultList[0]);
        } else {
            if (selectedItem - 1 === -1) {
                setSelectedItem(searchResultList.length);
            } else if (selectedItem - 1 === 0) {
                setSelectedItem(searchResultList.length);
            } else {
                setSelectedItem(selectedItem - 1);
            }
        }
    };
    const handleNextSearchItem = () => {
        if (searchResultList.length === 1) {
            setSelectedItem(1);
            changeItemBySearch(searchResultList[0]);
        } else {
            if (selectedItem + 1 === searchResultList.length) {
                setSelectedItem(selectedItem + 1);
            } else if (selectedItem + 1 > searchResultList.length) {
                setSelectedItem(1);
            } else {
                setSelectedItem(selectedItem + 1);
            };
        }
    };

    useEffect(() => {
        if (selectedItem !== 0) {
            changeItemBySearch(searchResultList[selectedItem - 1]);
        } 
    }, [selectedItem]);

    return(
        <div className="Main-content-search-body">
            <div className='Main-content-search-body-textarea'>
                <textarea  
                    className='Main-content-search-body-textarea-entry'
                    value={value}
                    onChange={handleChangeSearchValue}/>
            </div>
            <div className='Main-content-search-body-buttons'>
                <div className='Main-content-search-body-buttons-previous'
                    role='button'
                    onClick={() => {handlePreviousSearchItem();}}>
                    <img src={arrow_image} alt=''/>
                </div>
                <div className='Main-content-search-body-buttons-next'
                    role='button'
                    onClick={() => {handleNextSearchItem();}}>
                    <img src={arrow_image} alt=''/>
                </div>
            </div>
            <div className='Main-content-search-body-search'
                role='button'
                onClick={handleSearch}>
                <img src={search_image} alt=''/>
            </div>
            <div className='Main-content-search-body-coincidence'>
                {selectedItem}/{searchResultList.length}
            </div>
            <div className="Main-content-search-body-close_button"
                role='button'
                onClick={() => {
                    handleCloseSearchPanel();
                }}>
                <img src={close_image} alt=''/>
            </div>
        </div>
    )
};

export default SearchPanel;