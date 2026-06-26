from fastapi import FastAPI
from modelos.clientes import Cliente, ClienteCrear
from modelos.facturas import Factura, FacturaCrear
from modelos.transacciones import Transaccion, TransaccionCrear

app = FastAPI()

# --- LISTAS EN MEMORIA ---
lista_clientes: list[Cliente] = []
lista_facturas: list[Factura] = []
lista_transacciones: list[Transaccion] = []

@app.get("/clientes", response_model=list[Cliente])
def listar_clientes():
    return lista_clientes

# Usamos ClienteCrear para recibir datos sin ID, pero respondemos con Cliente
@app.post("/clientes", response_model=Cliente)
def crear_clientes(datos_cliente: ClienteCrear):
    cliente_val = Cliente.model_validate(datos_cliente.model_dump())
    lista_clientes.append(cliente_val)
    return cliente_val

@app.put("/clientes/{id}", response_model=Cliente)
def editar_clientes(id: int, datos_cliente: ClienteCrear):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == id:
            cliente_val = Cliente.model_validate(datos_cliente.model_dump())
            cliente_val.id = id # Mantenemos el ID original
            lista_clientes[i] = cliente_val
            return cliente_val
    return {"mensaje": "Cliente no encontrado"}

@app.delete("/clientes/{id}")
def eliminar_clientes(id: int):
    for p, cliente in enumerate(lista_clientes):
        if cliente.id == id:
            lista_clientes.pop(p)
            return {"mensaje": "Cliente eliminado"}
    return {"mensaje": "Cliente no encontrado"}

@app.get("/clientes/{id}", response_model=Cliente)
def lista_Solo_Cliente(id: int):
    for cliente in lista_clientes:
        if cliente.id == id:
            return cliente
    return {"mensaje": "Cliente no encontrado"}


@app.get("/facturas", response_model=list[Factura])
def listar_facturas():
    return lista_facturas

@app.post("/facturas", response_model=Factura)
def crear_factura(datos_factura: FacturaCrear):
    factura_val = Factura.model_validate(datos_factura.model_dump())
    lista_facturas.append(factura_val)
    return factura_val

@app.post("/facturas/{cliente_id}", response_model=Factura)
def crear_factura_cliente(cliente_id: int, datos_factura: FacturaCrear):
    for cliente in lista_clientes:
        if cliente.id == cliente_id:
            factura_val = Factura.model_validate(datos_factura.model_dump())
            lista_facturas.append(factura_val)
            return factura_val
    return {"mensaje": "Cliente no existe"}

@app.put("/facturas/{id}", response_model=Factura)
def editar_factura(id: int, datos_factura: FacturaCrear):
    for i, obj_factura in enumerate(lista_facturas):
        if obj_factura.id == id:
            factura_val = Factura.model_validate(datos_factura.model_dump())
            factura_val.id = id
            lista_facturas[i] = factura_val
            return factura_val
    return {"mensaje": "Factura no encontrada"}

@app.delete("/facturas/{id}")
def eliminar_factura(id: int):
    for p, factura in enumerate(lista_facturas):
        if factura.id == id:
            lista_facturas.pop(p)
            return {"mensaje": "factura eliminada"}
    return {"mensaje": "Factura no encontrada"}

@app.get("/transacciones", response_model=list[Transaccion])
def listar_transacciones():
    return lista_transacciones

@app.post("/transacciones", response_model=Transaccion)
def crear_transaccion(datos_transaccion: TransaccionCrear):
    transaccion_val = Transaccion.model_validate(datos_transaccion.model_dump())
    lista_transacciones.append(transaccion_val)
    return transaccion_val

@app.post("/transacciones/{factura_id}", response_model=Transaccion)
def crear_transaccion_factura(factura_id: int, datos_transaccion: TransaccionCrear):
    for factura in lista_facturas:
        if factura.id == factura_id:
            transaccion_val = Transaccion.model_validate(datos_transaccion.model_dump())
            lista_transacciones.append(transaccion_val)
            return transaccion_val
    return {"mensaje": "Factura no existe"}

@app.put("/transacciones/{id}", response_model=Transaccion)
def editar_transaccion(id: int, datos_transaccion: TransaccionCrear):
    for i, obj_transaccion in enumerate(lista_transacciones):
        if obj_transaccion.id == id:
            transaccion_val = Transaccion.model_validate(datos_transaccion.model_dump())
            transaccion_val.id = id
            lista_transacciones[i] = transaccion_val
            return transaccion_val
    return {"mensaje": "Transaccion no encontrada"}

@app.delete("/transacciones/{id}")
def eliminar_transaccion(id: int):
    for p, transaccion in enumerate(lista_transacciones):
        if transaccion.id == id:
            lista_transacciones.pop(p)
            return {"mensaje": "transaccion eliminada"}
    return {"mensaje": "Transaccion no encontrada"}