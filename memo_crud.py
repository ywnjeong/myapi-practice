from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app=FastAPI()

memo_db=[]

class Memo(BaseModel):
    title: str
    content: str

@app.post("/memos/",response_model=Memo)
def create_memo(memo:Memo):
    memo_db.append(memo)
    return memo

@app.get("/memos/",response_model=List[Memo])
def read_memos():
    return memo_db

@app.get("/memos/{memo_id}",response_model=Memo)
def read_memo(memo_id:int):
    return memo_db[memo_id]

@app.put("/memos/{memo_id}", response_model=Memo)
def update_memo(memo_id:int, updated_memo:Memo):
    memo_db[memo_id]=updated_memo
    return updated_memo

@app.delete("/memos/{memo_id}",response_model=Memo)
def delete_memo(memo_id:int):
    deleted_memo=memo_db.pop(memo_id)
    return deleted_memo