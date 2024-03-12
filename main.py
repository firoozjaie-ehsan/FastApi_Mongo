from fastapi import FastAPI
from web import employee
app = FastAPI()
# https://medium.com/@miladev95/fastapi-crud-with-mongodb-d7a8fbb8c53e
app.include_router(employee.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app",
        host="localhost", port=8000, reload=True)