from fastapi import APIRouter

user= APIRouter()

@user.get("/")
def root():
    return{"message":"Bienvenidos al gestor de la API"}