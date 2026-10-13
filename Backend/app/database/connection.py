from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

# Crear conexión con Neon
engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True)


# Crear sesiones de base de datos
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


# Obtener una sesión para los endpoints
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# Comprobar la conexión con Neon
def probar_conexion():
    with engine.connect() as conexion:
        resultado = conexion.execute(text("SELECT 1"))
        return resultado.scalar()
