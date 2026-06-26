from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List, TYPE_CHECKING

if TYPE_CHECKING:
    from app.modelos.facturas import Factura

class ClienteBase(SQLModel):
    nombre: str
    email: str
    descripcion: str

class Cliente(ClienteBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    facturas: List["Factura"] = Relationship(back_populates="cliente")

class ClienteCrear(ClienteBase):
    pass

class ClienteEditar(SQLModel):
    nombre: Optional[str] = None
    email: Optional[str] = None
    descripcion: Optional[str] = None

class ClienteLeer(ClienteBase):
    id: int