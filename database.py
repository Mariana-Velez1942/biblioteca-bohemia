# En esta seccion se genera la creacion de la base de datos de la biblioteca

# 1. Importamos sqlite

import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
bd = os.path.join(BASE_DIR, "biblioteca.db")

# Abrimos la conexion de la database y retornamos el objeto de la conexion 
def conectar():
    conexion = sqlite3.connect(bd)
    return conexion

# Se genera la creacion de la tabla libros en caso de no existir
def creacion_tabla():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS libros (
            id       INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo   TEXT    NOT NULL,
            autor    TEXT    NOT NULL,
            seccion  TEXT    NOT NULL,
            cantidad INTEGER NOT NULL DEFAULT 0,
            precio   REAL    NOT NULL DEFAULT 0.0
        )
    """)
    
    conexion.commit() #Aqui guard0 los cambios
    conexion.close()  # Cerramos los cambios que se realicen dentro de la database

def crear_tabla_usuarios():
    """
    Crea la tabla 'usuarios' si no existe.
    Campos: id, nombre, apellido, correo, contraseña
    """
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre     TEXT    NOT NULL,
            apellido   TEXT    NOT NULL,
            correo     TEXT    NOT NULL UNIQUE,
            contrasena TEXT    NOT NULL
        )
    """)

    conexion.commit()
    conexion.close()