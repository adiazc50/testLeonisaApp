from pydantic import BaseModel
from typing import Optional

class bibliotecaSchema(BaseModel):
    isbnId:Optional[str]
    titulo: str
    autor: str
    editorial: str
    coleccion: str
    cantidad: int
    diponible: int

