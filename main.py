from fastapi import FastAPI

app = FastAPI()

# Endpoint 1 — health check
@app.get("/health")
def health():
    return {"status": "ok"}

# Endpoint 2 — get all items
@app.get("/items")
def get_items():
    return [
        {"id": 1, "name": "Laptop", "price": 999},
        {"id": 2, "name": "Mouse", "price": 29},
        {"id": 3, "name": "Keyboard", "price": 79},
    ]

# Endpoint 3 — get one item by id
@app.get("/items/{item_id}")
def get_item(item_id: int):
    items = {
        1: {"id": 1, "name": "Laptop", "price": 999},
        2: {"id": 2, "name": "Mouse", "price": 29},
        3: {"id": 3, "name": "Keyboard", "price": 79},
    }
    if item_id not in items:
        return {"error": "item not found"}
    return items[item_id]




from pydantic import BaseModel

# define what a new item looks like
class Item(BaseModel):
    name: str
    price: float

# in-memory "database" for now
fake_db = {}
next_id = 4  # starting after our hardcoded items

@app.post("/items")
def create_item(item: Item):
    global next_id
    fake_db[next_id] = {"id": next_id, "name": item.name, "price": item.price}
    next_id += 1
    return fake_db[next_id - 1]


