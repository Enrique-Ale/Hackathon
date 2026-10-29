from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

from . import models, schemas, database

# Inicializar base de datos
database.init_db()

app = FastAPI(
    title="Chamba Solidaria MX API",
    description="API para conectar servicios, oficios, capacitaciones y economía solidaria.",
    version="0.1.0"
)

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {
        "message": "Bienvenido a la API de Chamba Solidaria MX",
        "status": "online",
        "version": "0.1.0"
    }

# --- USUARIOS ---

@app.post("/usuarios/", response_model=schemas.UsuarioOut, status_code=status.HTTP_201_CREATED)
def crear_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(database.get_db)):
    db_usuario = db.query(models.Usuario).filter(models.Usuario.email == usuario.email).first()
    if db_usuario:
        raise HTTPException(status_code=400, detail="El email ya está registrado")

    nuevo_usuario = models.Usuario(**usuario.model_dump())
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

@app.get("/usuarios/", response_model=List[schemas.UsuarioOut])
def listar_usuarios(db: Session = Depends(database.get_db)):
    return db.query(models.Usuario).all()

# --- PERFILES TRABAJADORES ---

@app.post("/perfiles-trabajadores/", response_model=schemas.PerfilTrabajadorOut, status_code=status.HTTP_201_CREATED)
def crear_perfil_trabajador(perfil: schemas.PerfilTrabajadorCreate, db: Session = Depends(database.get_db)):
    # Verificar si el usuario existe
    db_usuario = db.query(models.Usuario).filter(models.Usuario.id == perfil.usuario_id).first()
    if not db_usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    # Verificar si ya tiene perfil
    if db_usuario.perfil_trabajador:
        raise HTTPException(status_code=400, detail="El usuario ya tiene un perfil de trabajador")

    # Marcar al usuario como trabajador
    db_usuario.es_trabajador = True

    nuevo_perfil = models.PerfilTrabajador(**perfil.model_dump())
    db.add(nuevo_perfil)
    db.commit()
    db.refresh(nuevo_perfil)
    return nuevo_perfil

@app.get("/trabajadores/", response_model=List[schemas.PerfilTrabajadorOut])
def listar_trabajadores(oficio: str = None, db: Session = Depends(database.get_db)):
    query = db.query(models.PerfilTrabajador)
    if oficio:
        query = query.filter(models.PerfilTrabajador.oficio_principal.ilike(f"%{oficio}%"))
    return query.all()

# --- SOLICITUDES ---

@app.post("/solicitudes/", response_model=schemas.SolicitudServicioOut, status_code=status.HTTP_201_CREATED)
def crear_solicitud(solicitud: schemas.SolicitudServicioCreate, db: Session = Depends(database.get_db)):
    # Verificar si el cliente existe
    db_usuario = db.query(models.Usuario).filter(models.Usuario.id == solicitud.cliente_id).first()
    if not db_usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    nueva_solicitud = models.SolicitudServicio(**solicitud.model_dump())
    db.add(nueva_solicitud)
    db.commit()
    db.refresh(nueva_solicitud)
    return nueva_solicitud

@app.get("/solicitudes/", response_model=List[schemas.SolicitudServicioOut])
def listar_solicitudes(db: Session = Depends(database.get_db)):
    return db.query(models.SolicitudServicio).all()
