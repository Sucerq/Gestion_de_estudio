import uuid
from sqlalchemy import Integer, String, CheckConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from app.database.base import Base


class MetaAcademica(Base):
    # Nombre de la tabla
    __tablename__ = "metas_academicas"

    __table_args__ = (
        # Validación para que el tiempo no vaya a recibir valores negativos
        CheckConstraint("tiempo_objetivo > 0", name="check_tiempo_objetivo"),
        # Validación para que en el estado solo puedan aparecer estás 3 palabras
        CheckConstraint(
            "estado IN ('pendiente', 'en_progreso', 'completada')", name="check_estado"
        ),
    )
    # Tablas y sus atributos
    id_meta: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )

    titulo: Mapped[str] = mapped_column(String(150), nullable=False)

    descripcion: Mapped[str | None] = mapped_column(String(500), nullable=True)

    tiempo_objetivo: Mapped[int] = mapped_column(Integer, nullable=False)

    tiempo_completado: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    estado: Mapped[str] = mapped_column(String(30), default="pendiente", nullable=False)

    def actualizar_estado(self):
        """Esta función sirve para poder cambiar el estado del estudio del candidato
        automaticamente con base al tiempo estudiado"""

        if self.tiempo_completado >= self.tiempo_objetivo:
            self.estado = "completada"

        elif self.tiempo_completado > 0:
            self.estado = "en_progreso"

        else:
            self.estado = "pendiente"

    def registrar_tiempo(self, minutos: int):
        """ "Esta funcion nos permite validar que el estudiante no vaya a registrar
        numeros negativos
        """

        if minutos <= 0:
            raise ValueError("Los minutos deben ser mayores que cero")

        self.tiempo_completado += minutos

        self.actualizar_estado()
