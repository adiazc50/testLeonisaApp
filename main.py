from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from route.route import biblioteca

app = FastAPI()



app.include_router(biblioteca)

#Creamos el modelo del libro
"""""


@app.get("/buscarLibro")
def buscarLibro():
    return{"message"}

@app.post("/agregarlibro")
def insertarLibro(libro:Libro):
    return{"menssage": f"libro {libro.isbnId} insertado"}
    """