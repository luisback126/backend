import mysql.connector

db = mysql.connector.connect(
    host="localhost",  # o la dirección de tu servidor
    user="tu_usuario",
    password="tu_contraseña",
    database="inventario_equipos"
)

cursor = db.cursor()

cursor.execute("SELECT * FROM equipos")
for row in cursor.fetchall():
    print(row)

cursor.close()
db.close()
