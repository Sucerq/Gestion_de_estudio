import time
from datetime import date, time as Time

from app.models.interrupcion import Interrupcion


class Temporizador:
    def __init__(self, id_temporizador: int):
        self.id_temporizador = id_temporizador
        self.tiempo_transcurrido = 0
        self.estado = "detenido"
        self._inicio = None

    def iniciar(self) -> None:
        self.tiempo_transcurrido = 0
        self._inicio = time.time()
        self.estado = "corriendo"

    def pausar(self) -> None:
        if self.estado == "corriendo":
            self.tiempo_transcurrido += int(time.time() - self._inicio)
            self._inicio = None
            self.estado = "pausado"

    def reanudar(self) -> None:
        if self.estado == "pausado":
            self._inicio = time.time()
            self.estado = "corriendo"

    def finalizar(self) -> int:
        if self.estado == "corriendo":
            self.tiempo_transcurrido += int(time.time() - self._inicio)
        self._inicio = None
        self.estado = "finalizado"
        return self.tiempo_transcurrido


class SesionEstudio:
    def __init__(
        self,
        id_sesion: int,
        fecha: date,
        hora_inicio: Time,
        duracion_planificada: int,
        materia: str,
    ):
        self.id_sesion = id_sesion
        self.fecha = fecha
        self.hora_inicio = hora_inicio
        self.duracion_planificada = duracion_planificada
        self.materia = materia
        self.estado = "pendiente"
        self.temporizador = Temporizador(id_sesion)
        self.interrupciones: list[Interrupcion] = []

    def crear(self) -> None:
        if self.duracion_planificada <= 0:
            raise ValueError("La duración planificada debe ser mayor que cero")
        self.estado = "pendiente"

    def editar(self, **cambios) -> None:
        for campo, valor in cambios.items():
            if hasattr(self, campo):
                setattr(self, campo, valor)

    def eliminar(self) -> None:
        self.estado = "eliminada"
        self.interrupciones.clear()

    def finalizar(self) -> None:
        self.temporizador.finalizar()
        self.estado = "finalizada"

    def agregar_interrupcion(self, interrupcion: Interrupcion) -> None:
        interrupcion.registrar()
        self.interrupciones.append(interrupcion)
