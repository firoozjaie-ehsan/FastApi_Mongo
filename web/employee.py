from fastapi import APIRouter, Depends, Body,HTTPException
from pydantic import BaseModel
from config.database import db_motor_connection

router = APIRouter(prefix = "/employee")

class EmployeModel(BaseModel):
    name: str
    age: int
    team: list

@router.get("/items/{item_id}", response_model=EmployeModel)
async def read_item(item_name: str,collection:type=Depends(db_motor_connection)):
    item = await collection.find_one({"name": item_name})
    if item:
        return item
    raise HTTPException(status_code=404, detail="Employee not found")

@router.post("/add/")
async def create_item(item: EmployeModel= Body(...),collection:type=Depends(db_motor_connection)):
    result=await collection.insert_one(item.model_dump())
    if result is None:
        raise HTTPException(status_code=404, detail='employee not add.')
    return item