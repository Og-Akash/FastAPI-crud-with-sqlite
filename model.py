from sqlalchemy import Column, Integer, String, Boolean
from db import base

class StoreDB(base):
    __tablename__ = "store"

    id = Column(Integer, primary_key=True, index=True)  # you need a primary key!
    item_name = Column(String)
    item_desc = Column(String)
    item_price = Column(Integer)
    discount = Column(Boolean)
