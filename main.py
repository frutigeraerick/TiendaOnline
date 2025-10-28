from fastapi import FastAPI
from database import Base, engine
from models import Categoria, Producto

app = FastAPI(title="Tienda Online")

Base.metadata.create_all(bind=engine)

@app.get("/")
def inicio():
    return {"mensaje": "API Tienda Online lista"}
