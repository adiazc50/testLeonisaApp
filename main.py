from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from route.route import user

app = FastAPI()

app.include_router(user)

#Creamos el modelo del libro
"""""
class Libro(BaseModel):
    isbnId: str
    titulo: str
    autor: str
    editorial: str
    coleccion: str
    cantidad: int
    diponible: bool

@app.get("/buscarLibro")
def buscarLibro():
    return{"message"}

@app.post("/agregarlibro")
def insertarLibro(libro:Libro):
    return{"menssage": f"libro {libro.isbnId} insertado"}
    """