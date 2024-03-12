from mongoengine import connect
from motor.motor_asyncio import AsyncIOMotorClient

def db_mongoengine_connection():
    con=connect("Test", host="localhost", port=27017)
    return con

def db_motor_connection():
    # MongoDB connection URL
    MONGO_URL = "mongodb://localhost:27017"
    client = AsyncIOMotorClient(MONGO_URL)
    db = client.get_database("Test")
    collection = db.get_collection("employee")
    return collection
