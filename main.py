from fastapi import FastAPI
from pydantic import BaseModel
import mysql.connector

app = FastAPI()

# Definir el modelo para la API
class Equipo(BaseModel):
    nombre: str
    descripcion: str
    fecha_adquisicion: str
    estado: str
    serial_number: str
    ubicacion: str

# Función para conectar a la base de datos
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="tu_usuario",
        password="tu_contraseña",
        database="inventario_equipos"
    )

# Crear un equipo
@app.post("/equipos/")
def crear_equipo(equipo: Equipo):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO equipos (nombre, descripcion, fecha_adquisicion, estado, serial_number, ubicacion) VALUES (%s, %s, %s, %s, %s, %s)",
        (equipo.nombre, equipo.descripcion, equipo.fecha_adquisicion, equipo.estado, equipo.serial_number, equipo.ubicacion)
    )
    db.commit()
    cursor.close()
    db.close()
    return {"mensaje": "Equipo creado exitosamente"}

# Obtener todos los equipos
@app.get("/equipos/")
def obtener_equipos():
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM equipos")
    equipos = cursor.fetchall()
    cursor.close()
    db.close()
    return equipos

# Obtener equipo por ID
@app.get("/equipos/{equipo_id}")
def obtener_equipo(equipo_id: int):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM equipos WHERE id = %s", (equipo_id,))
    equipo = cursor.fetchone()
    cursor.close()
    db.close()
    if equipo:
        return equipo
    return {"mensaje": "Equipo no encontrado"}
