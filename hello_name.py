from fastapi import FastAPI
from typing import Union

app=FastAPI()

@app.get("/")
def read_root():
    return {"Hello":"World"}

#@app.get("/items/{items_id}")
#def read_itemid(item_id:int, q: Union[str,None]=None):
#    return {"item_id":item_id, "q":q}

@app.get("/hello/{name}")
def read_item(name:str):
    return{"message":f"Hello, {name}!"}