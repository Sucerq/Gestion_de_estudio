from app.models.usuario import Usuario
from app.models.meta_academica import MetaAcademica
from app.models.sesion_estudio import SesionEstudio
from app.models.interrupcion import Interrupcion


class Estudiante(Usuario):
    def __init__(self, id_usuario: int, nombre: str, correo: str, contrasena: str, programa_academico: str):
        super().__init__(id_usuario, nombre, correo, contrasena, rol="estudiante")
        self.programa_academico = programa_academico
        self.metas: list[MetaAcademica] = []
        self.sesiones: list[SesionEstudio] = []
        self._sesion_actual: SesionEstudio | None = None

    def definir_meta(self, m: MetaAcademica) -> None:
        self.metas.append(m)

    def iniciar_temporizador(self, s: SesionEstudio) -> None:
        if s not in self.sesiones:
            self.sesiones.append(s)
        s.temporizador.iniciar()
        s.estado = "en_curso"
        self._sesion_actual = s

    def registrar_interrupcion(self, i: Interrupcion) -> None:
        if self._sesion_actual is None:
            raise ValueError("No hay una sesión de estudio en curso")
        self._sesion_actual.agregar_interrupcion(i)

    def consultar_progreso(self) -> dict:
        finalizadas = [s for s in self.sesiones if s.estado == "finalizada"]
        minutos = sum(s.temporizador.tiempo_transcurrido for s in finalizadas) // 60
        return {
            "estudiante": self.nombre,
            "sesiones_finalizadas": len(finalizadas),
            "minutos_estudiados": minutos,
            "metas_cumplidas": sum(m.estado == "completada" for m in self.metas),
            "total_metas": len(self.metas),
        }
