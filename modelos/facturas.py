from pydantic import BaseModel

class FacturaBase(BaseModel):
    fecha: str
    cliente_id: int

class FacturaCrear(FacturaBase):
    pass

class Factura(FacturaBase):
    id: int | None = None