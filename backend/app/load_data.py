import json
from sqlalchemy.orm import Session
from . import models, database

def load_fixtures(db: Session):
    # Cargar archivo de datos
    with open("data/fixtures.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    # Insertar Oficios
    for oficio_data in data["oficios"]:
        if not db.query(models.Oficio).filter(models.Oficio.nombre == oficio_data["nombre"]).first():
            db.add(models.Oficio(**oficio_data))

    # Insertar Usuarios y sus perfiles
    for usuario_data in data["usuarios"]:
        usuario = db.query(models.Usuario).filter(models.Usuario.email == usuario_data["email"]).first()
        if not usuario:
            usuario = models.Usuario(**usuario_data)
            db.add(usuario)
            db.commit()
            db.refresh(usuario)

        # Vincular perfil si existe en fixtures
        for perfil_data in data["perfiles"]:
            if perfil_data["email_referencia"] == usuario.email:
                if not db.query(models.PerfilTrabajador).filter(models.PerfilTrabajador.usuario_id == usuario.id).first():
                    perfil = models.PerfilTrabajador(
                        usuario_id=usuario.id,
                        oficio_principal=perfil_data["oficio_principal"],
                        zona_cobertura=perfil_data["zona_cobertura"],
                        disponibilidad=perfil_data["disponibilidad"],
                        rango_precio_min=perfil_data["rango_precio_min"],
                        rango_precio_max=perfil_data["rango_precio_max"],
                        reputacion=perfil_data["reputacion"],
                        descripcion=perfil_data["descripcion"]
                    )
                    db.add(perfil)

    db.commit()

if __name__ == "__main__":
    # Script ejecutable para poblar la DB
    db = next(database.get_db())
    load_fixtures(db)
    print("Datos de demostración cargados correctamente.")
