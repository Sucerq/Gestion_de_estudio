import uuid

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.meta_academica import MetaAcademica
from app.schemas.meta_academica import (
    MetaAcademicaCrear,
    MetaAcademicaActualizar,
)


def crear_meta(db: Session, datos: MetaAcademicaCrear):
    nueva_meta = MetaAcademica(
        titulo=datos.titulo,
        descripcion=datos.descripcion,
        tiempo_objetivo=datos.tiempo_objetivo,
        tiempo_completado=0,
        estado="pendiente",
    )

    db.add(nueva_meta)
    db.commit()
    db.refresh(nueva_meta)

    return nueva_meta


def listar_metas(db: Session):
    consulta = select(MetaAcademica)
    resultado = db.scalars(consulta)

    return resultado.all()


def obtener_meta(db: Session, meta_id: uuid.UUID):
    return db.get(MetaAcademica, meta_id)


def actualizar_meta(
    db: Session,
    meta_id: uuid.UUID,
    datos: MetaAcademicaActualizar,
):
    meta = obtener_meta(db, meta_id)

    if meta is None:
        return None

    cambios = datos.model_dump(exclude_unset=True)

    for campo, valor in cambios.items():
        setattr(meta, campo, valor)

    meta.actualizar_estado()

    db.commit()
    db.refresh(meta)

    return meta


def eliminar_meta(db: Session, meta_id: uuid.UUID):
    meta = obtener_meta(db, meta_id)

    if meta is None:
        return False

    db.delete(meta)
    db.commit()

    return True
