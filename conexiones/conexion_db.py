import os
import mysql.connector

os.system('cls')###limpiar la pantalla de consola y el cls es el comando
def conectar_db():### mandamos a llamar la funcion para conectar la bd
    return mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="farmacia_bienestar"
)

