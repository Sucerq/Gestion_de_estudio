from fastapi import FastAPI
from app.routes.meta_academica import router as metas_router

# Crear la aplicación FastAPI
app = FastAPI(
    title="Software de Gestión de Tiempos de Estudio",
    description="API para gestionar sesiones de estudio",
    version="1.0.0",
)

app.include_router(metas_router)


# Endpoint de inicio
@app.get("/")
def inicio():
    return {"mensaje": "Bienvenido al sistema de gestión de estudio"}


# Endpoint para verificar el servidor
@app.get("/salud")
def verificar_salud():
    return {"estado": "Servidor funcionando correctamente"}
