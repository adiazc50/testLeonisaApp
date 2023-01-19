from pydantic import BaseModel

class bibliotecaSchema(BaseModel):
    isbnId: str
    titulo: str
    autor: str
    editorial: str
    coleccion: str
    cantidad: int
    diponible: bool

