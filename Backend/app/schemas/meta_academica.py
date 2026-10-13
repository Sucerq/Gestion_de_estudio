import uuid

from pydantic import BaseModel, ConfigDict, Field


class MetaAcademicaCrear(BaseModel):
    titulo: str = Field(min_length=1, max_length=150)
    descripcion: str | None = Field(default=None, max_length=500)
    tiempo_objetivo: int = Field(gt=0)


class MetaAcademicaActualizar(BaseModel):
    titulo: str | None = Field(default=None, min_length=1, max_length=150)

    descripcion: str | None = Field(default=None, max_length=500)

    tiempo_objetivo: int | None = Field(default=None, gt=0)

    class MetaAcademicaRespuesta(BaseModel):
        model_config = ConfigDict(from_attributes=True)

        id_meta: uuid.UUID
        titulo: str
        descripcion: str | None
        tiempo_objetivo: int
        tiempo_completado: int
        estado: str
