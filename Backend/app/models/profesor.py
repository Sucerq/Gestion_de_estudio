from app.models.usuario import Usuario
from app.models.sesion_estudio import SesionEstudio
from app.models.estudiante import Estudiante


class Profesor(Usuario):
    def __init__(self, id_usuario: int, nombre: str, correo: str, contrasena: str, departamento: str):
        super().__init__(id_usuario, nombre, correo, contrasena, rol="profesor")
        self.departamento = departamento
        self.sesiones_asignadas: list[SesionEstudio] = []

    def crear_sesion(self, s: SesionEstudio) -> None:
        s.crear()
        self.sesiones_asignadas.append(s)

    def asignar_sesion(self, s: SesionEstudio, e: Estudiante) -> None:
        if s not in self.sesiones_asignadas:
            self.sesiones_asignadas.append(s)
        if s not in e.sesiones:
            e.sesiones.append(s)
