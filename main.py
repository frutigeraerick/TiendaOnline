from fastapi import FastAPI
from database import Base, engine

import models

app = FastAPI(
    title="Tienda Online",
    description="API para gestionar una tienda online",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

@app.get("/")
def inicio():
    return {"mensaje": "Tienda online lista y conectada a la base de datos"}
