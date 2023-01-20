from fastapi import APIRouter
from schema.biblioteca_Schema import bibliotecaSchema
#from config.db import conn
#from model.biblioteca import bibliotecas


biblioteca= APIRouter()

@biblioteca.get("/")
def root():
    return{"message":"Bienvenidos al gestor de la API, para visualizar rutas dirigete a /docs"}

@biblioteca.post("/api/agregarLibro")
def crearLibro(data_Libro:bibliotecaSchema):
    nuevo_libro = data_Libro.dict()
    #conn.execute(bibliotecas.insert().values(nuevo_libro)) #->datalibro
    #print(data_Libro)
    #print(nuevo_libro)

@biblioteca.put("/api/actualizarEstado")
def actualizarLibro():
    pass