from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Usuario Schemas
class UsuarioCreate(BaseModel):
    nombre: str
    email: str
    telefono: Optional[str] = None
    es_trabajador: bool = False
    es_cliente: bool = True

class UsuarioOut(BaseModel):
    id: int
    nombre: str
    email: str
    telefono: Optional[str]
    es_trabajador: bool
    es_cliente: bool
    creado_en: datetime

    class Config:
        from_attributes = True

# Perfil Trabajador Schemas
class PerfilTrabajadorCreate(BaseModel):
    usuario_id: int
    oficio_principal: str
    zona_cobertura: str
    disponibilidad: bool = True
    rango_precio_min: Optional[float] = None
    rango_precio_max: Optional[float] = None
    descripcion: Optional[str] = None

class PerfilTrabajadorOut(BaseModel):
    id: int
    usuario_id: int
    oficio_principal: str
    zona_cobertura: str
    disponibilidad: bool
    rango_precio_min: Optional[float]
    rango_precio_max: Optional[float]
    reputacion: float
    descripcion: Optional[str]

    class Config:
        from_attributes = True

# Solicitud Servicio Schemas
class SolicitudServicioCreate(BaseModel):
    cliente_id: int
    oficio_requerido: str
    descripcion: str
    ubicacion: Optional[str] = None

class SolicitudServicioOut(BaseModel):
    id: int
    cliente_id: int
    oficio_requerido: str
    descripcion: str
    estado: str
    ubicacion: Optional[str]
    creado_en: datetime

    class Config:
        from_attributes = True
