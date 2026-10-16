from abc import ABC


class Usuario(ABC):

    def __init__(self, id_usuario: int, nombre: str, correo: str, contrasena: str, rol: str):
        self._id_usuario = id_usuario
        self._nombre = nombre
        self._correo = correo
        self._contrasena = contrasena
        self._rol = rol
        self._sesion_activa = False

    @property
    def id_usuario(self) -> int:
        return self._id_usuario

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def correo(self) -> str:
        return self._correo

    @property
    def rol(self) -> str:
        return self._rol

    def registrarse(self) -> None:
        if not self._nombre or not self._correo or not self._contrasena:
            raise ValueError("Nombre, correo y contraseña son obligatorios")
        print(f"Usuario {self._nombre} registrado como {self._rol}")

    def iniciar_sesion(self) -> bool:
        self._sesion_activa = True
        return self._sesion_activa

    def cerrar_sesion(self) -> None:
        self._sesion_activa = False
