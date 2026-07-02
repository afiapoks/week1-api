from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

load_dotenv()

# ── Database setup ──────────────────────────────────────────
DATABASE_URL = "sqlite:///./database.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# ── Database model (this becomes a table) ───────────────────
class ItemDB(Base):
    __tablename__ = "items"
    id       = Column(Integer, primary_key=True, index=True)
    name     = Column(String, nullable=False)
    price    = Column(Float, nullable=False)

# Create the table if it doesn't exist
Base.metadata.create_all(bind=engine)

# ── FastAPI app ──────────────────────────────────────────────
app = FastAPI(title=os.getenv("APP_NAME", "My API"))

# ── Pydantic schema (what the user sends in requests) ───────
class ItemInput(BaseModel):
    name: str
    price: float

# ── Endpoints ───────────────────────────────────────────────
@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/items")
def get_items():
    db = SessionLocal()
    items = db.query(ItemDB).all()
    db.close()
    return items


@app.get("/items/{item_id}")
def get_item(item_id: int):
    db = SessionLocal()
    item = db.query(ItemDB).filter(ItemDB.id == item_id).first()
    db.close()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.post("/items", status_code=201)
def create_item(item: ItemInput):
    db = SessionLocal()
    new_item = ItemDB(name=item.name, price=item.price)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    db.close()
    return new_item


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    db = SessionLocal()
    item = db.query(ItemDB).filter(ItemDB.id == item_id).first()
    if not item:
        db.close()
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(item)
    db.commit()
    db.close()