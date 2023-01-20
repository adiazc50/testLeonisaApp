from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from schema.biblioteca_Schema import bibliotecaSchema
from config.db import engine
from model.biblioteca import biblioteca
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.cors import CORSMiddleware

bibliotec= APIRouter()


#Raiz donde se indica la direccion con todas las rutas de la API
@bibliotec.get("/")
def root():
    return{"message":"Bienvenidos al gestor de la API, para visualizar rutas dirigete a /docs"}
#Traemos todos los libros de la base de datos
@bibliotec.get("/api/libros",response_model=List[bibliotecaSchema])
def mostrarLibros():
    with engine.connect() as conn:
        resultado = conn.execute(biblioteca.select()).fetchall()
        return resultado
#Consulta a un libro en especifico
@bibliotec.get("/api/consultarLibro/{isbnId}", response_model=bibliotecaSchema)
def obtenerLibro(isbnId: str):
    with engine.connect() as conn:
        resultado= conn.execute(biblioteca.select().where(biblioteca.c.isbnId== isbnId)).first()
        return resultado

#Crear un nuevo libro
@bibliotec.post("/api/crearLibros", status_code=HTTP_201_CREATED)
def crearLibros(data_libro: bibliotecaSchema):
    with engine.connect() as conn:
        nuevoLibro= data_libro.dict()
        conn.execute(biblioteca.insert().values(nuevoLibro))
        return Response(status_code=HTTP_201_CREATED)
#Modificacion de un libro
@bibliotec.put("/api/actualizarEstado/{isbnId}",response_model=bibliotecaSchema)
def actualizarLibro(data_update:bibliotecaSchema,isbnId: str):
    with engine.connect() as conn:
        conn.execute(biblioteca.update().values(titulo=data_update.titulo,autor=data_update.autor,
        editorial=data_update.editorial,coleccion=data_update.coleccion,cantidad=data_update.cantidad,diponible=data_update.diponible).where(biblioteca.c.isbnId == isbnId))
 
        resultado = conn.execute(biblioteca.select().where(biblioteca.c.isbnId == isbnId)).first()
        return resultado

#Borrar un libro
@bibliotec.delete("/api/libro/{isbnId}",status_code=HTTP_204_NO_CONTENT)
def borrarLibro(isbnId:str):
    with engine.connect() as conn:
        conn.execute(biblioteca.delete().where(biblioteca.c.isbnId == isbnId))
        return Response(status_code=HTTP_204_NO_CONTENT)



