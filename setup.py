
import subprocess   # Para ejecutar comandos del sistema
import sys          # Para acceder al intérprete de Python
import os           # Para verificar si existen archivos


def verificar_python():
    """
    Verifica que la versión de Python sea 3.6 o superior.
    """
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 6):
        print("Error: Se requiere Python 3.6 o superior.")
        sys.exit(1)
    print(f"Python {version.major}.{version.minor} detectado.")


def verificar_sqlite():
    try:
        import sqlite3
        print(f"SQLite3 disponible — versión {sqlite3.sqlite_version}")
    except ImportError:
        print("Error: SQLite3 no está disponible.")
        sys.exit(1)


def verificar_archivos():
    """
    Verifica que todos los archivos del proyecto existan.
    """
    archivos = ["main.py", "database.py", "libro.py", "biblioteca.py", "seed.py"]
    todos_ok = True

    for archivo in archivos:
        if os.path.exists(archivo):
            print(f"{archivo} encontrado.")
        else:
            print(f"Error: {archivo} NO encontrado.")
            todos_ok = False

    return todos_ok


def inicializar_base_de_datos():
    if os.path.exists("biblioteca.db"):
        print("Base de datos ya existe — omitiendo seed.")
    else:
        print("Inicializando base de datos con 30 libros...")
        subprocess.run([sys.executable, "seed.py"])


def main():
    """
    Ejecuta todos los pasos de instalación en orden.
    """
    print("\n" + "="*50)
    print(" SETUP — BIBLIOTECA BOHEMIA")
    print("="*50)

    print("Paso 1: Verificando Python...")
    verificar_python()

    print("Paso 2: Verificando SQLite...")
    verificar_sqlite()

    print("Paso 3: Verificando archivos del proyecto...")
    if not verificar_archivos():
        print("Error:Faltan archivos. Verifica tu carpeta del proyecto.")
        sys.exit(1)

    print("Paso 4: Inicializando base de datos...")
    inicializar_base_de_datos()

    print("\n" + "="*50)
    print("TODO LISTO — Ejecutar: python main.py")
    print("="*50 + "\n")


if __name__ == "__main__":
    main()