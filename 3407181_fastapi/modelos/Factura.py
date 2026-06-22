from pydantic import BaseModel

class Factura(BaseModel):
    id: int
    fecha: str
    cliente_id: int
