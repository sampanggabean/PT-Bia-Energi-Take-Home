from db import engine, create_db_and_tables
from fastapi import FastAPI
from controller import book_router

async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(book_router)

@app.get("/")
def checkAlive():
    return {"status": "alive"}