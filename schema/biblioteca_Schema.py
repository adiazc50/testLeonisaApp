from pydantic import BaseModel
from typing import Optional

#Establesco el modelo para la base de datos
class bibliotecaSchema(BaseModel):
    isbnId:Optional[str]
    titulo: str
    autor: str
    editorial: str
    coleccion: str
    cantidad: int
    diponible: int

