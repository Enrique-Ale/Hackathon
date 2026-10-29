from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, Text, DateTime
from sqlalchemy.orm import declarative_base, relationship
import datetime

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    telefono = Column(String, nullable=True)
    es_trabajador = Column(Boolean, default=False)
    es_cliente = Column(Boolean, default=True)
    creado_en = Column(DateTime, default=datetime.datetime.utcnow)

    perfil_trabajador = relationship("PerfilTrabajador", back_populates="usuario", uselist=False)

class Oficio(Base):
    __tablename__ = "oficios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, nullable=False)
    descripcion = Column(Text, nullable=True)

class PerfilTrabajador(Base):
    __tablename__ = "perfiles_trabajadores"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), unique=True)
    oficio_principal = Column(String, nullable=False)
    zona_cobertura = Column(String, nullable=False)
    disponibilidad = Column(Boolean, default=True)
    rango_precio_min = Column(Float, nullable=True)
    rango_precio_max = Column(Float, nullable=True)
    reputacion = Column(Float, default=5.0)
    descripcion = Column(Text, nullable=True)

    usuario = relationship("Usuario", back_populates="perfil_trabajador")

class SolicitudServicio(Base):
    __tablename__ = "solicitudes_servicio"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("usuarios.id"))
    oficio_requerido = Column(String, nullable=False)
    descripcion = Column(Text, nullable=False)
    estado = Column(String, default="Borrador") # Borrador, Publicado, Asignado, En curso, Terminado, Calificado
    ubicacion = Column(String, nullable=True)
    creado_en = Column(DateTime, default=datetime.datetime.utcnow)
