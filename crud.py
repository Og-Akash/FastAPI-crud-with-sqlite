from fastapi import FastAPI, Depends, HTTPException
from db import session_local, engine, base
from sqlalchemy.orm import Session
from model import StoreDB
from pydantic import BaseModel, Field
from typing import List, Optional

app = FastAPI()

base.metadata.create_all(bind=engine)

class StoreResponse(BaseModel):
    id:int
    item_name: str = Field(..., min_length=3)
    item_desc: str = Field(..., min_length=10, max_length=100)
    item_price: float
    discount: bool

    class Config:
        from_attributes = True

def get_db():
    try:
        db = session_local()
        return db
    finally:
        db.close()

@app.post("/item", response_model=StoreResponse)
def add_item(item: StoreResponse, db: Session = Depends(get_db)):
    db_item = StoreDB(
        id=item.id,
        item_name=item.item_name,
        item_desc=item.item_desc,
        item_price=item.item_price,
        discount=item.discount
    )
    db.add(db_item)
    db.commit() 
    db.refresh(db_item)
    return db_item

# reading the records from the db
@app.get("/items", response_model=List[StoreResponse])
def read_items(skip:int = 0, limit:int=10):
    db = get_db()
    items = db.query(StoreDB).offset(skip).limit(limit).all()
    if items is None:
        raise HTTPException(status_code=404,detail="No Item recored")
    return items

# reading the records from the db by id
@app.get("/items/{item_id}", response_model=StoreResponse)
def get_item_by_id(item_id:int,db:Session=Depends(get_db)):
    item = db.query(StoreDB).filter(StoreDB.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404,detail="No Item Found")
    return item

# update record in db

# @app.put("/update/{item_id}", response_model=StoreResponse)
# def update_item(item_id:int,item:StoreResponse,db:Session=Depends(get_db)):
#     matchedItem = db.query(StoreDB).filter(StoreDB.id == item_id).first()

#     if matchedItem is None:
#         raise HTTPException(status_code=404, detail="Item not found")
    
#     matchedItem.id = item.id if item.id is not None else matchedItem.id
#     matchedItem.item_name = item.item_name if item.item_name is not None else matchedItem.item_name
#     matchedItem.item_desc = item.item_desc if item.item_desc is not None else matchedItem.item_desc
#     matchedItem.item_price = item.item_price if item.item_price is not None else matchedItem.item_price
#     matchedItem.discount = item.discount if item.discount is not None else matchedItem.discount

#     db.commit()
#     db.refresh(matchedItem)
#     return matchedItem

#? Optimal Code
@app.put("/update/{item_id}", response_model=StoreResponse)
def update_item(item_id: int, item: StoreResponse, db: Session = Depends(get_db)):
    matched_item = db.query(StoreDB).filter(StoreDB.id == item_id).first()

    if matched_item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    update_data = item.dict(exclude_unset=True)

    for key, value in update_data.items():
        setattr(matched_item, key, value)

    db.commit()
    db.refresh(matched_item)
    return matched_item

# Delete the item from DB
@app.delete("/delete/{item_id}")
def update_item(item_id: int, db: Session = Depends(get_db)):
    matched_item = db.query(StoreDB).filter(StoreDB.id == item_id).first()

    if matched_item is None:
        raise HTTPException(status_code=404, detail="Item not found") 
    db.delete(matched_item)
    db.commit()
    return {"message": "Item with {item_id} is Deleted"}
