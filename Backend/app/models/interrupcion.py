from datetime import datetime


class Interrupcion:
    def __init__(self, id_interrupcion: int, motivo: str, duracion_aprox: int, fecha_hora: datetime | None = None):
        self.id_interrupcion = id_interrupcion
        self.motivo = motivo
        self.duracion_aprox = duracion_aprox
        self.fecha_hora = fecha_hora or datetime.now()

    def registrar(self) -> None:
        if self.duracion_aprox < 0:
            raise ValueError("La duración no puede ser negativa")
        self.fecha_hora = datetime.now()
