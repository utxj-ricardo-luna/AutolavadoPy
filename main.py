from fastapi import FastAPI
from typing import List, Optional
from uuid import UUID, uuid4
from model import Genero,Role,Usuario
app = FastAPI()

db: List[Usuario] = [
    Usuario(
        id=uuid4(),
        primerNombre="Raul",
        apellidos="Rufino Pazos",
        genero=Genero.masculino,
        roles=[Role.user]
    ),
    Usuario(
        id=uuid4(),
        primerNombre="Edwin",
        apellidos="Cabrera Tecorralco",
        genero=Genero.masculino,
        roles=[Role.user]
    ),
    Usuario(
        id=uuid4(),
        primerNombre="Francisco",
        apellidos="Galindo Rosales",
        genero=Genero.femenino,
        roles=[Role.user]
    ),
    Usuario(
        id=uuid4(),
        primerNombre="Angel",
        apellidos="Artiaga Carrillo",
        genero=Genero.otro,
        roles=[Role.user]
    ),
]

@app.get("/")
async def root():
    return{"messaje":"hola pequeñ@s de 8A DSM"}

@app.get("/api/v1/users")
async def get_users():
    return db
