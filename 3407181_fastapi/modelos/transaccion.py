from pydantic import BaseModel

class transaccion(BaseModel):
    id:int
    contidad:int
    vr_unitarios:float
    descripcion:str
    factura_id:int 