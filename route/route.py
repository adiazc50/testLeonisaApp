from fastapi import APIRouter
from schema.biblioteca_Schema import bibliotecaSchema
biblioteca= APIRouter()

@biblioteca.get("/")
def root(title='Test Leonisa',
            description='para visualizar la guia de la apli /routes',
            version='1'):
    return{"message":"Bienvenidos al gestor de la API"}

@biblioteca.post("/api/agregarLibro")
def crearLibro(data_Libro:bibliotecaSchema):
    print(data_Libro)