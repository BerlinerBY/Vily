import './MWSearch.css';
import { useEffect, useState } from 'react';
// import { search } from './Search';

function MWSearch({showMWSearch, handleCloseMWSearch, items, transferDataToSearch}) {
    const showHideClassName = showMWSearch ? "modal display-block" : "modal display-none";
    const [searchValue, setSearchValue] = useState("");
    const [source, setSource] = useState("all categories");
    const [stringType, setStringType] = useState("xml_id");


    const onOptionChahgeSource = (e) => {
        setSource(e.target.value);
    };
    const onOptionChangeLvl1 = (e) => {
        setStringType(e.target.value);
    };

    const handleChangeSearchValue = (event) => {
        setSearchValue(event.target.value);
    };

    const handleClose = () => {
        setSource("all categories");
        setStringType("xml_id");
        setSearchValue("");
        handleCloseMWSearch();
    };
    const handleSearch = () => {
        if (searchValue !== "") {        
            var xml_flag;

            if (source === "all categories") {
                // request to back-end
                alert("Sorry, I don't work now");
            } else if (source === "current category") {
                if (stringType === "xml_id") {
                    xml_flag = "xml_id";
                } else if (stringType === "1-st language") {
                    xml_flag = "eng_version";
                } else if (stringType === "2-nd language") {
                    xml_flag = "ru_version";
                } else if (stringType === "belarus") {
                    xml_flag = "bel_versio";
                }
            }
            transferDataToSearch(xml_flag, searchValue);
            handleClose();
        }
    };

 
    useEffect(() => {
        const closeOnEscapePressed = (e) => {
            if (e.key === "Escape") {
                handleClose();
            }
        };
        document.addEventListener('keydown', closeOnEscapePressed);
        return () => {
            document.addEventListener('keydown', closeOnEscapePressed);
        };
    }, [])

    return (
        <div className={showHideClassName} 
                onClick={() => {
                    // close modal when clicked outside
                    handleClose();
                }}>
            <div className="modal-main"
                onClick={e => {
                    // do not close modal if anything inside modal content is clicked
                    e.stopPropagation();
                }}>
                <div className='modal-header'>
                    Search
                </div>
                <hr></hr>
                <div className='modal-body'>
                    <fieldset>
                        <legend>Source:</legend>
                        
                        <div>
                            <input 
                                type="radio" 
                                name="source" 
                                value="all categories" 
                                id="all categories" 
                                checked={source === "all categories"}
                                onChange={onOptionChahgeSource}/>
                            <label htmlFor="all categories">all categories</label>
                        </div>

                        <div>
                            <input 
                                type="radio" 
                                name="source" 
                                value="current category" 
                                id="current category" 
                                checked={source === "current category"}
                                onChange={onOptionChahgeSource}/>
                            <label htmlFor="current category">current category</label>
                        </div>
                    </fieldset>
                    {source === "current category" ? 
                        <fieldset>
                            <legend>String type:</legend>

                            <div>
                                <input 
                                    type="radio" 
                                    name="stringType" 
                                    value="xml_id" 
                                    id="xml_id" 
                                    checked={stringType === "xml_id"}
                                    onChange={onOptionChangeLvl1}/>
                                <label htmlFor="xml_id">xml_id</label>
                            </div>

                            <div>
                                <input 
                                    type="radio" 
                                    name="stringType" 
                                    value="1-st language" 
                                    id="1-st language" 
                                    checked={stringType === "1-st language"}
                                    onChange={onOptionChangeLvl1}/>
                                <label htmlFor="1-st language">1-st language</label>
                            </div>

                            <div>
                                <input 
                                    type="radio" 
                                    name="stringType" 
                                    value="2-nd language" 
                                    id="2-nd language" 
                                    checked={stringType === "2-nd language"}
                                    onChange={onOptionChangeLvl1}/>
                                <label htmlFor="2-nd language">2-nd language</label>
                            </div>

                            <div>
                                <input 
                                    type="radio" 
                                    name="stringType" 
                                    value="belarus" 
                                    id="belarus" 
                                    checked={stringType === "belarus"}
                                    onChange={onOptionChangeLvl1}/>
                                <label htmlFor="belarus">belarus</label>
                            </div>
                        </fieldset>
                        :
                        <></>}
                </div>
                <div className='model-input'>
                    <textarea 
                        className='model-input-textarea'
                        value={searchValue}
                        onChange={handleChangeSearchValue}/>
                </div>
                <div className='modal-footer'>
                    <button className='modal-footer-button search' type="button" onClick={() => {handleSearch();}}>
                        Search
                    </button>
                    <button className='modal-footer-button close' type="button" onClick={() => {handleClose();}}>
                        Close
                    </button>
                </div>
            </div>
      </div>
    )
};

export default MWSearch;