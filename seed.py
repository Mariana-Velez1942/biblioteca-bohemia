
from database import creacion_tabla, crear_tabla_usuarios, conectar
from libro import Libro
from biblioteca import Biblioteca
from usuarios import Usuario, GestorUsuarios


def cargar_libros():
   
    libros_iniciales = [
        # --- SECCIÓN: Clásicos ---
        {"titulo": "Cien años de soledad",              "autor": "Gabriel García Márquez", "seccion": "Clásicos",        "cantidad": 5,  "precio": 35000},
        {"titulo": "El amor en los tiempos del cólera", "autor": "Gabriel García Márquez", "seccion": "Clásicos",        "cantidad": 3,  "precio": 32000},
        {"titulo": "Don Quijote de la Mancha",          "autor": "Miguel de Cervantes",    "seccion": "Clásicos",        "cantidad": 4,  "precio": 40000},
        {"titulo": "Crimen y castigo",                  "autor": "Fiódor Dostoyevski",     "seccion": "Clásicos",        "cantidad": 3,  "precio": 30000},
        {"titulo": "Ana Karenina",                      "autor": "León Tolstói",           "seccion": "Clásicos",        "cantidad": 2,  "precio": 38000},

        # --- SECCIÓN: Ciencia Ficción ---
        {"titulo": "Dune",                              "autor": "Frank Herbert",          "seccion": "Ciencia Ficción", "cantidad": 6,  "precio": 42000},
        {"titulo": "1984",                              "autor": "George Orwell",          "seccion": "Ciencia Ficción", "cantidad": 7,  "precio": 28000},
        {"titulo": "Un mundo feliz",                    "autor": "Aldous Huxley",          "seccion": "Ciencia Ficción", "cantidad": 4,  "precio": 27000},
        {"titulo": "Fundación",                         "autor": "Isaac Asimov",           "seccion": "Ciencia Ficción", "cantidad": 5,  "precio": 33000},
        {"titulo": "El marciano",                       "autor": "Andy Weir",              "seccion": "Ciencia Ficción", "cantidad": 3,  "precio": 36000},

        # --- SECCIÓN: Fantasía ---
        {"titulo": "El Hobbit",                         "autor": "J.R.R. Tolkien",         "seccion": "Fantasía",        "cantidad": 8,  "precio": 39000},
        {"titulo": "El nombre del viento",              "autor": "Patrick Rothfuss",       "seccion": "Fantasía",        "cantidad": 5,  "precio": 41000},
        {"titulo": "El imperio final",                  "autor": "Brandon Sanderson",      "seccion": "Fantasía",        "cantidad": 4,  "precio": 38000},
        {"titulo": "Eragon",                            "autor": "Christopher Paolini",    "seccion": "Fantasía",        "cantidad": 6,  "precio": 29000},
        {"titulo": "Las brumas del reino",              "autor": "Brandon Sanderson",      "seccion": "Fantasía",        "cantidad": 3,  "precio": 37000},

        # --- SECCIÓN: Historia ---
        {"titulo": "Sapiens",                           "autor": "Yuval Noah Harari",      "seccion": "Historia",        "cantidad": 9,  "precio": 45000},
        {"titulo": "El origen de las especies",         "autor": "Charles Darwin",         "seccion": "Historia",        "cantidad": 3,  "precio": 31000},
        {"titulo": "Historia del tiempo",               "autor": "Stephen Hawking",        "seccion": "Historia",        "cantidad": 4,  "precio": 34000},
        {"titulo": "Armas, gérmenes y acero",           "autor": "Jared Diamond",          "seccion": "Historia",        "cantidad": 2,  "precio": 43000},
        {"titulo": "El mundo de ayer",                  "autor": "Stefan Zweig",           "seccion": "Historia",        "cantidad": 3,  "precio": 30000},

        # --- SECCIÓN: Autoayuda ---
        {"titulo": "Hábitos atómicos",                  "autor": "James Clear",            "seccion": "Autoayuda",       "cantidad": 10, "precio": 48000},
        {"titulo": "El poder del ahora",                "autor": "Eckhart Tolle",          "seccion": "Autoayuda",       "cantidad": 7,  "precio": 35000},
        {"titulo": "Los 7 hábitos",                     "autor": "Stephen Covey",          "seccion": "Autoayuda",       "cantidad": 5,  "precio": 37000},
        {"titulo": "Piense y hágase rico",              "autor": "Napoleon Hill",          "seccion": "Autoayuda",       "cantidad": 6,  "precio": 32000},
        {"titulo": "La inteligencia emocional",         "autor": "Daniel Goleman",         "seccion": "Autoayuda",       "cantidad": 4,  "precio": 36000},

        # --- SECCIÓN: Programación ---
        {"titulo": "Python para todos",                 "autor": "Charles Severance",      "seccion": "Programación",    "cantidad": 8,  "precio": 52000},
        {"titulo": "Aprende Python",                    "autor": "Eric Matthes",           "seccion": "Programación",    "cantidad": 6,  "precio": 55000},
        {"titulo": "Clean Code",                        "autor": "Robert C. Martin",       "seccion": "Programación",    "cantidad": 5,  "precio": 58000},
        {"titulo": "El programador pragmático",         "autor": "David Thomas",           "seccion": "Programación",    "cantidad": 4,  "precio": 54000},
        {"titulo": "Algoritmos en Python",              "autor": "George T. Heineman",     "seccion": "Programación",    "cantidad": 3,  "precio": 50000},
    ]

    # Inicializacion de ambas tablas
    creacion_tabla()
    crear_tabla_usuarios()

    bib    = Biblioteca()
    gestor = GestorUsuarios()

    print("Cargando libros iniciales...")

    # Recorrer la lista e insertar cada libro
    for datos in libros_iniciales:
        try:
            libro = Libro(
                titulo    = datos["titulo"],
                autor     = datos["autor"],
                seccion   = datos["seccion"],
                cantidad  = datos["cantidad"],
                precio    = datos["precio"]
            )
            bib.agregar_libro(libro)
        except ValueError as e:
            print(f"Error con '{datos['titulo']}': {e}")

    print("¡30 libros cargados exitosamente en Biblioteca Bohemia!")

    # --- Crear usuario admin por defecto ---
    print("Creando usuario admin...")

    try:
        admin = Usuario(
            nombre     = "Admin",
            apellido   = "Bohemia",
            correo     = "admin@bohemia.com",
            contrasena = "1234"
        )
        gestor.registrar(admin)
        print("Usuario admin creado correctamente.")
        print("Correo: admin@bohemia.com")
        print("Contraseña: 1234")
    except ValueError as e:
        print(f"Error creando admin: {e}")

    print("¡Base de datos lista para usar!")


if __name__ == "__main__":
    cargar_libros()