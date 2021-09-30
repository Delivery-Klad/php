from parser import parse
from fastapi import FastAPI
from database import create_tables, select_all

app = FastAPI()


@app.post("/parse")
async def create_database_tables():
    try:
        return parse()
    except Exception as e:
        print(e)


@app.get("/get_all")
def test():
    try:
        return select_all()
    except Exception as e:
        print(e)


@app.on_event("startup")
def startup():
    create_tables()
