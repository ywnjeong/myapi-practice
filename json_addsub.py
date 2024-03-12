from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

item_db=[]

class Item(BaseModel):
    title: int
    num: int

@app.put("/itemupdate/",response_model=dict)
def update(item:Item):
    result1=item.title+item.num
    result2=item.title-item.num
    return {"addition":result1, "subtraction":result2}