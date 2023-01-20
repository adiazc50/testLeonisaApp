from fastapi import APIRouter
from schema.biblioteca_Schema import bibliotecaSchema
from config.db import conn
from model.biblioteca import biblioteca
from typing import List

biblioteca= APIRouter()

@biblioteca.get("/")
def root():
    return{"message":"Bienvenidos al gestor de la API, para visualizar rutas dirigete a /docs"}


@biblioteca.post("/api/crearLibros")
def crearLibros(data_libro: bibliotecaSchema):
    nuevoLibro= data_libro.dict()
    print(nuevoLibro)
    print(data_libro)
    #conn.execute(bibliotecas.insert().values())

@biblioteca.put("/api/actualizarEstado")
def actualizarLibro():
    pass






"""""
@biblioteca.get("api/ObtenerLibros", response_model=List[bibliotecaSchema])
def obtenerLibros():
    #with engine.connect() as conn:
        #resultado= conn.execute(bibliotecas.select().fetchall())
        #return resultado


@biblioteca.get("api/libro/{isbnId_Id}", response_model=bibliotecaSchema)
def buscarLibro(isbnId_Id: str):
    #with engine.connect() as conn:
        #resultado= conn.execute(bibliotecas.select().where(bibliotecas.c.isbnId==isbnId_Id)).first()
        #return resultado

@biblioteca.post("/api/agregarLibro")
def crearLibro(data_Libro:bibliotecaSchema):
    print(data_Libro)
    #with engine.connect() as conn:
        #nuevo_libro = data_Libro.dict()
        #conn.execute(bibliotecas.insert().values(nuevo_libro)) #->datalibro
    
        #print(nuevo_libro)
    


"""