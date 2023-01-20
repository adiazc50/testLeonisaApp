from fastapi import FastAPI
from route.route import bibliotec
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.cors import CORSMiddleware
#Inicio la APP
app = FastAPI()

#CORS para la APP
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#Asigno un administrador de rutas para la API
app.include_router(bibliotec)
