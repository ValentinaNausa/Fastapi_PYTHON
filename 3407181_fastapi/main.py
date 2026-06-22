from fastapi import FastAPI
from pydantic import BaseModel

from modelos.Factura import Factura
from modelos.transaccion import transaccion

app = FastAPI()


# Crear clase llamado MODELO
class Cliente(BaseModel):
    id: int
    nombre: str
    edad: int
    descripcion: str |None|None 


lista_clientes: list[Cliente] = []


# endpoint
@app.get("/clientes", response_model=list[Cliente])
def listar_clientes():
    return lista_clientes


# endpoint
@app.post("/clientes", response_model=Cliente)
def crear_clientes(datos_cliente: Cliente):
    cliente_val = Cliente.model_validate(datos_cliente.model_dump())
    lista_clientes.append(cliente_val)
    return cliente_val


# endpoint
@app.put("/clientes/{id}", response_model=Cliente)
def editar_clientes(id: int, datos_cliente: Cliente):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == id:
            cliente_val = Cliente.model_validate(datos_cliente.model_dump())
            lista_clientes[i] = cliente_val

    return cliente_val

# endpoint
@app.delete("/clientes/{id}")
def eliminar_clientes(id: int):
    for p, cliente in enumerate(lista_clientes):
        if cliente.id == id:
            lista_clientes.pop(p)
            return {"mensaje": "Cliente eliminado"}


@app.get("/clientes/{id}", response_model=Cliente)
def lista_Solo_Cliente(id:int):
    for cliente in lista_clientes:
        if cliente.id == id:
            return cliente
        
lista_transacciones: list[transaccion] = []

@app.get("/transacciones", response_model=list[transaccion])
def listar_transacciones():
    return lista_transacciones


@app.post("/transacciones", response_model=transaccion)
def crear_transaccion(datos_transaccion: transaccion):
    transaccion_val = transaccion.model_validate(datos_transaccion.model_dump())
    lista_transacciones.append(transaccion_val)
    return transaccion_val

@app.post("/transacciones/{factura_id}")
def crear_transaccion_factura( factura_id: int,datos_transaccion: transaccion):
    for factura in lista_facturas:
        if factura.id == factura_id:
            transaccion_val = transaccion.model_validate(
                datos_transaccion.model_dump()
            )
            lista_transacciones.append(transaccion_val)
            return transaccion_val
    return {"mensaje": "Factura no existe"}


@app.put("/transacciones/{id}", response_model=transaccion)
def editar_transaccion(id: int, datos_transaccion: transaccion):
    for i, obj_transaccion in enumerate(lista_transacciones):
        if obj_transaccion.id == id:
            transaccion_val = transaccion.model_validate(datos_transaccion.model_dump())
            lista_transacciones[i] = transaccion_val

    return transaccion_val

@app.delete("/transacciones/{id}")
def eliminar_transaccion(id: int):
    for p, transaccion in enumerate(lista_transacciones):
        if transaccion.id == id:
            lista_transacciones.pop(p)
            return {"mensaje": "transaccion eliminada"}


lista_facturas: list[Factura] = []
     
@app.get("/facturas", response_model=list[Factura])
def listar_facturas():
    return lista_facturas


@app.post("/facturas", response_model=Factura)
def crear_factura(datos_factura: Factura):
    factura_val = Factura.model_validate(datos_factura.model_dump())
    lista_facturas.append(factura_val)
    return factura_val


@app.post("/facturas/{cliente_id}")
def crear_factura_cliente(cliente_id: int, datos_factura: Factura):

    for cliente in lista_clientes:

        if cliente.id == cliente_id:

            factura_val = Factura.model_validate(
                datos_factura.model_dump()
            )

            lista_facturas.append(factura_val)

            return factura_val

    return {"mensaje": "Cliente no existe"}

@app.put("/facturas/{id}", response_model=Factura)
def editar_factura(id: int, datos_factura: Factura):
    for i, obj_factura in enumerate(lista_facturas):
        if obj_factura.id == id:
            factura_val = Factura.model_validate(datos_factura.model_dump())
            lista_facturas[i] = factura_val

    return factura_val

@app.delete("/facturas/{id}")
def eliminar_factura(id: int):
    for p, factura in enumerate(lista_facturas):
        if factura.id == id:
            lista_facturas.pop(p)
            return {"mensaje": "factura eliminada"} 
        
@app.post("/transacciones/{factura_id}/{cliente_id}")
def crear_transaccion_cliente_factura(
    factura_id: int,
    cliente_id: int,
    datos_transaccion: transaccion
):

    cliente_encontrado = False
    factura_encontrada = False

    for cliente in lista_clientes:
        if cliente.id == cliente_id:
            cliente_encontrado = True

    for factura in lista_facturas:
        if factura.id == factura_id:
            factura_encontrada = True

    if not cliente_encontrado:
        return {"mensaje": "Cliente no existe"}

    if not factura_encontrada:
        return {"mensaje": "Factura no existe"}

    transaccion_val = transaccion.model_validate(
        datos_transaccion.model_dump()
    )

    lista_transacciones.append(transaccion_val)

    return transaccion_val