from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
import schemas, crud
from database import SessionLocal

router = APIRouter(
    prefix="/categorias",
    tags=["Categorías"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.CategoriaRead, status_code=status.HTTP_201_CREATED)
def crear_categoria(categoria: schemas.CategoriaCreate, db: Session = Depends(get_db)):
    return crud.crear_categoria(db, categoria)

@router.get("/", response_model=list[schemas.CategoriaRead])
def obtener_categorias_activas(db: Session = Depends(get_db)):
    return crud.obtener_categorias_activas(db)

@router.get("/{categoria_id}", response_model=schemas.CategoriaReadConProductos)
def obtener_categoria_con_productos(categoria_id: int, db: Session = Depends(get_db)):
    return crud.obtener_categoria_con_productos(db, categoria_id)

@router.put("/{categoria_id}", response_model=schemas.CategoriaRead)
def actualizar_categoria(categoria_id: int, datos: schemas.CategoriaUpdate, db: Session = Depends(get_db)):
    return crud.actualizar_categoria(db, categoria_id, datos)

@router.delete("/{categoria_id}")
def desactivar_categoria(categoria_id: int, db: Session = Depends(get_db)):
    return crud.desactivar_categoria(db, categoria_id)
