import uuid

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.meta_academica import (
    MetaAcademicaCrear,
    MetaAcademicaActualizar,
    MetaAcademicaRespuesta,
)
from app.services import meta_academica as servicio

router = APIRouter(
    prefix="/metas",
    tags=["Metas Academicas"],
)


@router.post(
    "/",
    response_model=MetaAcademicaRespuesta,
    status_code=status.HTTP_201_CREATED,
)
def crear_meta(
    datos: MetaAcademicaCrear,
    db: Session = Depends(get_db),
):
    return servicio.crear_meta(db, datos)


@router.get(
    "/",
    response_model=list[MetaAcademicaRespuesta],
)
def listar_metas(db: Session = Depends(get_db)):
    return servicio.listar_metas(db)


@router.get(
    "/{meta_id}",
    response_model=MetaAcademicaRespuesta,
)
def obtener_meta(
    meta_id: uuid.UUID,
    db: Session = Depends(get_db),
):
    meta = servicio.obtener_meta(db, meta_id)

    if meta is None:
        raise HTTPException(
            status_code=404,
            detail="Meta academica no encontrada",
        )

    return meta


@router.patch(
    "/{meta_id}",
    response_model=MetaAcademicaRespuesta,
)
def actualizar_meta(
    meta_id: uuid.UUID,
    datos: MetaAcademicaActualizar,
    db: Session = Depends(get_db),
):
    meta = servicio.actualizar_meta(db, meta_id, datos)

    if meta is None:
        raise HTTPException(
            status_code=404,
            detail="Meta academica no encontrada",
        )

    return meta


@router.delete(
    "/{meta_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def eliminar_meta(
    meta_id: uuid.UUID,
    db: Session = Depends(get_db),
):
    eliminado = servicio.eliminar_meta(db, meta_id)

    if not eliminado:
        raise HTTPException(
            status_code=404,
            detail="Meta academica no encontrada",
        )
