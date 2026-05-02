# main.py
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pathlib import Path
from pydantic import BaseModel

app = FastAPI()
TEMPLATE_PATH = Path(__file__).parent / "templates" / "index.html"


class Item(BaseModel):
    name: str
    price: float


@app.get("/", response_class=HTMLResponse)
def read_root():
    html = TEMPLATE_PATH.read_text(encoding="utf-8")
    return HTMLResponse(content=html)


@app.post("/items")
def create_item(item: Item):
    return {"msg": "created", "item": item}


def main() -> None:
    import uvicorn

    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)


if __name__ == "__main__":
    main()
