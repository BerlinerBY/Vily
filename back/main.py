from typing import Union
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from model.database import DBSession
from model import models
from schemas import CategoryInput, ItemPutInput, ItemCreateInput, UploadItems
from sqlalchemy.orm.exc import UnmappedInstanceError
from typing import List

app = FastAPI()

origins = [
    'http://localhost:3000', 
    'https://localhost:3000'
    'http://localhost'
    'https://localhost']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/api/categories")
async def read_categories():
    db = DBSession()
    try:
        categories = db.query(models.CategoryFile).all()
    finally:
        db.close()

    return categories

@app.post("/api/category")
async def create_category(category: CategoryInput):
    db = DBSession()
    try:
        if len(category.title) == 0:
            raise HTTPException(
                status_code=400, detail={
                    "status": "Error 400 - Bad Request",
                    "msg": "Empty title" 
                }
            )
        new_category = models.CategoryFile(title=category.title)
        db.add(new_category)
        db.commit()
        db.refresh(new_category)
    finally:
        db.close()

    return new_category

@app.put("/api/category/update/{category_id}")
async def update_category(category_id: int, update_category: CategoryInput):
    if len(update_category.title) == 0:
        raise HTTPException(
            status_code=400, detail={
                "status": "Error 400 - Bad Request",
                "msg": "Empty title" 
            }
        )
    db = DBSession()
    try:
        category = db.query(models.CategoryFile).filter(models.CategoryFile.id == category_id).first()
        category.title = update_category.title
        db.commit()
        db.refresh(category)
    finally:
        db.close()
    
    return category


@app.delete("/api/category/delete/{category_id}")
async def delete_category(category_id):
    db = DBSession()
    try:
        category = db.query(models.CategoryFile).filter(models.CategoryFile.id == category_id).first()
        db.delete(category)
        db.commit()
    except UnmappedInstanceError:
        raise  HTTPException(status_code=400, detail={
            "status": "Error 400 - Bad Request",
            "msg": f"Category with 'id': '{category_id}' doesn't exist."
        })
    finally:
        db.close()

    return {
        "status": "200",
        "msg": "Category deleted successfully"
    }

### API of items

@app.get("/api/items")
async def read_items():
    db = DBSession()
    try:
        items = db.query(models.Item).all()
    finally:
        db.close()

    return items


@app.get("/api/items/{item_id}")
async def read_item(item_id: int):
    db = DBSession()
    try:
        item = db.query(models.Item).filter(models.Item.id == item_id).first()
    finally:
        db.close()
    
    return item


@app.get("/api/category/{category_id}")
async def read_items_by_category(category_id: int):
    db = DBSession()
    try:
        items = db.query(models.Item).filter(models.Item.category_id == category_id).all()
    finally:
        db.close()
    
    return items

@app.post("/api/item")
async def create_item(item: ItemCreateInput):
    db = DBSession()
    try:
        if len(item.xml_id) == 0 and len(item.eng_version) == 0 and len(item.ru_version) == 0:
            raise HTTPException(
                status_code=400, detail={
                    "status": "Error 400 - Bad Request",
                    "msg": "Empty fields" 
                }
            )
        if item.bel_version:
            new_item = models.Item(
                xml_id=item.xml_id,
                bel_version=item.bel_version,
                eng_version=item.eng_version,
                ru_version=item.ru_version,
                category_id=item.category_id,
            )
        else:
            new_item = models.Item(
                xml_id=item.xml_id,
                eng_version=item.eng_version,
                ru_version=item.ru_version,
                category_id=item.category_id,
            )

        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    finally:
        db.close()

    return new_item

### Upload items
@app.post("/api/items/upload")
async def upload_items(requset: List[ItemCreateInput]):
    db = DBSession()
    try:
        arr = []
        for item in requset:
            if len(item.xml_id) == 0 and len(item.eng_version) == 0 and len(item.ru_version) == 0:
                raise HTTPException(
                    status_code=400, detail={
                        "status": "Error 400 - Bad Request",
                        "msg": f"Empty fields. {item.xml_id}" 
                    }
                )
            if item.bel_version:
                new_item = models.Item(
                    xml_id=item.xml_id,
                    bel_version=item.bel_version,
                    eng_version=item.eng_version,
                    ru_version=item.ru_version,
                    category_id=item.category_id,
                )
            else:
                new_item = models.Item(
                    xml_id=item.xml_id,
                    eng_version=item.eng_version,
                    ru_version=item.ru_version,
                    category_id=item.category_id,
                )
    
            db.add(new_item)
            db.commit()
            db.refresh(new_item)
            arr.append(item)
    finally:
        db.close()

    return HTTPException(
        status_code=200, detail={
            "status": "200",
            "msg": "Successfully"
        }
    )

@app.put("/api/items/update/{item_id}")
async def update_item(item_id: int, update_item: ItemPutInput):
    if len(update_item.bel_version) == 0:
        raise HTTPException(
            status_code=400, detail={
                "status": "Error 400 - Bad Request",
                "msg": "Empty field" 
            }
        )
    db = DBSession()
    try:
        item = db.query(models.Item).filter(models.Item.id == item_id).first()
        item.bel_version = update_item.bel_version
        item.readiness = update_item.readiness
        db.commit()
        db.refresh(item)
    finally:
        db.close()
    
    return item



@app.delete("/api/items/delete/{item_id}")
async def delete_item(item_id):
    db = DBSession()
    try:
        item = db.query(models.Item).filter(models.Item.id == item_id).first()
        db.delete(item)
        db.commit()
    except UnmappedInstanceError:
        raise  HTTPException(status_code=400, detail={
            "status": "Error 400 - Bad Request",
            "msg": f"Item with 'id': '{item_id}' doesn't exist."
        })
    finally:
        db.close()

    return {
        "status": "200",
        "msg": "Item deleted successfully"
    }


@app.delete("/api/items/delete/all/{category_id}")
async def delete_items(category_id):
    db = DBSession()
    try:
        value = models.Item.__table__.delete().where(models.Item.category_id == category_id)
        db.execute(value)
        db.commit()
    except UnmappedInstanceError:
        raise  HTTPException(status_code=400, detail={
            "status": "Error 400 - Bad Request",
            "msg": f"Item with 'id': "
        })
    finally:
        db.close()

    return {
        "status": "200",
        "msg": "Items deleted successfully"
    }