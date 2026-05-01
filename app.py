# main.py
from doctest import debug
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float


@app.get("/")
def read_root():
    return {"msg": "hello fastapi"}


@app.post("/items")
def create_item(item: Item):
    return {"msg": "created", "item": item}


def main() -> None:
    import uvicorn

    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)


if __name__ == "__main__":
    main()

