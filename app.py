from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from uuid import UUID

app = FastAPI()

class Item(BaseModel):
    name: str = Field(..., min_length=3)
    description: str = Field(..., min_length=10, max_length=100)
    price: float
    discount: bool | None = None  # Optional field

ITEMS = []

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/items")
def get_items():
    return ITEMS

@app.post("/item")
def add_item(item: Item):
    ITEMS.append(item)
    return {"message": "Item added successfully", "item": item}


@app.put("/item/{item_id}")
def update_item(item_id:UUID,item:Item):
    for i, existing_item in enumerate(ITEMS):
        if existing_item.id == item_id:
            ITEMS[i] = item
            return {"message": "Item updated successfully", "item": item}
    raise HTTPException(status_code=404, detail=f" item with {item_id} not found")

@app.delete("/item/{item_id}")
def delete_item(item_id:UUID):
    for i, existing_item in enumerate(ITEMS):
       if existing_item.id == item_id:
            ITEMS.pop(i)
            return {"message": "Item Deleted successfully"}
    raise HTTPException(status_code=404, detail=f" item with {item_id} not found")
