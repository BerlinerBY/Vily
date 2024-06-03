import './MainItem.css';
import { connect, useDispatch } from 'react-redux';
import arrow_icon from './icons/arrow.png';
import copy_icon from './icons/copy.png';
import clear_icon from './icons/clear.png';
import save_icon from './icons/save.png';
import { useEffect, useState } from 'react';
import { updateItemRequest } from '../../../features/ApiRequests/MainRequests';

function MainItem({handlePreviousItem, handleNextItem,
                    selectedItemFromStore, selectedItemIndexFromStore,
                    selectedCategoryFromStore}) {
    const item = selectedItemFromStore;
    const index = selectedItemIndexFromStore;
    const category = selectedCategoryFromStore;
    const [belValue, setBelValue] = useState();
    const dispatch = useDispatch();

    useEffect(() => {
        setBelValue(item.bel_version);
    }, [item.bel_version])

    const submitButton = () => {
        updateItemRequest(index, item.id, belValue, dispatch);
    };

    const handleChange = (event) => {
        setBelValue(event.target.value);
    };
    const handleClear = () => {
        setBelValue("");
    };
    const handleCopy = () => {
        navigator.clipboard.writeText(belValue);
    };

    const convertData = (data) => {
        let new_data = data.split("T")[0].split("-");
        return new_data.reverse().join(".");
    };

    const chooseItem = () => {
        if (item.length === 0) {
            return (
                <div className='Main-Item-Welcome'>
                    <h2>Choose Item</h2>
                </div>
            )
        } else {
            return (
                <div className='Main-Item-Container'>
                    <div className='Main-Item-SourceStrings'>
                        <div className='Main-Item-SourceStrings-entry'>
                            <div className='Main-Item-SourceStrings-Header'>
                                <div className='Main-Item-SourceStrings-Header-header'>
                                    <div className='Main-Item-SourceStrings-Header-header-title'>
                                        Source Strings
                                    </div>
                                    <div className='Main-Item-SourceStrings-Header-header-change_date'>
                                        {convertData(item.date_updated)}
                                    </div>
                                    <div className='Main-Item-SourceStrings-Header-header-change_time'>
                                        {item.date_updated.split("T")[1]}
                                    </div>
                                </div>
                                <div className='Main-Item-SourceStrings-Header-Status'>
                                    {item.readiness ? 
                                        <div className='Main-Item-SourceStrings-Header-Status-done'>Done</div> 
                                        : 
                                        <div className='Main-Item-SourceStrings-Header-Status-raw'>Raw</div>}
                                </div>
                                <div className='Main-Item-SourceStrings-Header-buttons'>
                                    <div className='Main-Item-SourceStrings-Header-buttons-previous'
                                        role='button'
                                        onClick={handlePreviousItem}>
                                        <img src={arrow_icon} alt='previous' className='Main-Item-SourceStrings-Header-buttons-previous-arrow'/>
                                    </div>
                                    <div className='Main-Item-SourceStrings-Header-buttons-next'
                                        role='button'
                                        onClick={handleNextItem}>
                                        <img src={arrow_icon} alt='next' className='Main-Item-SourceStrings-Header-buttons-next-arrow'/>
                                    </div>
                                </div>
                            </div>
                            <div className='Main-Item-SourceStrings-Strings'>
                                <div className='Main-Item-SourceStrings-Strings-Versions'>
                                    <div className='Main-Item-SourceStrings-Strings-Versions-version'>
                                        {item.first_version}
                                    </div>
                                    {item.second_version ?
                                        <div className='Main-Item-SourceStrings-Strings-Versions-version'>
                                            {item.second_version}
                                        </div>
                                        :
                                        <></>
                                    }
                                </div>
                            </div>
                        </div>
                    </div>
                    <hr />
                    <div className='Main-Item-TargetField'>
                        <div className='Main-Item-TargetField-entry'>
                            <div className='Main-Item-TargetField-entry-text'>
                                <textarea 
                                    className='Main-Item-TargetField-entry-textarea'
                                    value={belValue} 
                                    onChange={handleChange}
                                />
                            </div>
                            <div className='Main-Item-TargetField-entry-buttons'>
                                <div className='Main-Item-TargetField-entry-buttons-copy' 
                                    role='button'
                                    onClick={handleCopy}>
                                    <img alt='' src={copy_icon}/>
                                </div>
                                <div className='Main-Item-TargetField-entry-buttons-clear'
                                    role='button'
                                    onClick={handleClear}>
                                    <img alt='' src={clear_icon}/>
                                </div>
                                <div className='Main-Item-TargetField-entry-buttons-save' 
                                    role='button'
                                    onClick={submitButton}
                                    >
                                    <img alt='' src={save_icon}/>
                                    SAVE
                                </div>
                            </div>
                        </div>
                    </div>
                    <hr />
                    <div className='Main-Item-Context'>
                        <div className='Main-Item-Context-Entry'>
                            <div className='Main-Item-Context-Entry-context'>
                                Context
                            </div>
                            <div className='Main-Item-Context-Entry-fields'>
                                <div>file_name: {category}</div>
                                <div>item_id: {item.item_id}</div>
                            </div>
                            <div className='Main-Item-Context-Entry-textarea'>
                                {item.context ?
                                    <textarea 
                                        className='Main-Item-Context-Entry-textarea-area'
                                        value={item.context}/>
                                    :
                                    <></>
                                }
                            </div>
                        </div>
                    </div>
                </div>
            )
        }
    };

    return (
        <>
            {chooseItem()}  
        </>
    )
};

function displayStateToProps(state) {
    return {
        selectedItemFromStore: state.contentReducer.selectedItem,
        selectedItemIndexFromStore: state.contentReducer.selectedItemIndex,
        selectedCategoryFromStore: state.categoryReducer.selectedСategoryName,
    }
};

export default connect(displayStateToProps)(MainItem);