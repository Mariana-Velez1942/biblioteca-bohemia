

from database import conectar   # Importacion de la función de conexión
from libro import Libro         # Importacion de la clase Libro


class Biblioteca:
    
    # Clase principal que gestiona todos los libros.
    # Contiene los métodos para agregar, consultar,
    # modificar, eliminar y listar libros.
    
    # AGREGAR
   
    def agregar_libro(self, libro):
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
        INSERT INTO libros (titulo, autor, seccion, cantidad, precio)
        VALUES (?, ?, ?, ?, ?)
    """, (libro.titulo, libro.autor, libro.seccion, libro.cantidad, libro.precio))

        conexion.commit()
        conexion.close()
        print(f"'{libro.titulo}' agregado correctamente.")
    
    # LISTAR TODOS
    
    def listar_libros(self):
        """
        Muestra todos los libros almacenados en la base de datos.
        Retorna la lista de libros encontrados.
        """
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM libros")
        libros = cursor.fetchall()  # Trae todos los resultados
        conexion.close()

        if len(libros) == 0:
            print("No hay libros registrados aún.")
            return []

        print("\n" + "="*50)
        print("CATÁLOGO BIBLIOTECA BOHEMIA")
        print("="*50)

        for libro in libros:
            print(f"ID: {libro[0]}")
            print(f"Título: {libro[1]}")
            print(f"Autor: {libro[2]}")
            print(f"Sección: {libro[3]}")
            print(f"Cantidad: {libro[4]}")
            print(f"Precio: ${libro[5]:,.2f}")
            print("-"*50)

        return libros

    
    # BUSCAR POR TÍTULO

    def buscar_por_titulo(self, titulo):
        """
        Busca libros que contengan el título dado.
        Parámetro: titulo (str)
        Retorna: lista de libros encontrados
        """
        conexion = conectar()
        cursor = conexion.cursor()

        # El % permite buscar aunque sea parte del título
        cursor.execute("""
            SELECT * FROM libros WHERE titulo LIKE ?
        """, (f"%{titulo}%",))

        libros = cursor.fetchall()
        conexion.close()

        if len(libros) == 0:
            print(f"No se encontraron libros con título '{titulo}'.")
            return []

        print(f"Se encontraron {len(libros)} libro(s):\n")
        for libro in libros:
            print(f"ID: {libro[0]} | {libro[1]} |  {libro[2]} |  {libro[3]}")

        return libros

    
    # BUSCAR POR AUTOR

    def buscar_por_autor(self, autor):
        """
        Busca libros por nombre de autor.
        Parámetro: autor (str)
        Retorna: lista de libros encontrados
        """
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
            SELECT * FROM libros WHERE autor LIKE ?
        """, (f"%{autor}%",))

        libros = cursor.fetchall()
        conexion.close()

        if len(libros) == 0:
            print(f"No se encontraron libros del autor '{autor}'.")
            return []

        print(f"Se encontraron {len(libros)} libro(s):\n")
        for libro in libros:
            print(f"ID: {libro[0]} | {libro[1]} |  {libro[2]} |  {libro[3]}")

        return libros

    
    # FILTRAR POR SECCIÓN
   

    def filtrar_por_seccion(self, seccion):
        """
        Filtra todos los libros de una sección específica.
        Parámetro: seccion (str)
        Retorna: lista de libros de esa sección
        """
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
            SELECT * FROM libros WHERE seccion LIKE ?
        """, (f"%{seccion}%",))

        libros = cursor.fetchall()
        conexion.close()

        if len(libros) == 0:
            print(f"No hay libros en la sección '{seccion}'.")
            return []

        print(f"Libros en sección '{seccion}':\n")
        for libro in libros:
            print(f"ID: {libro[0]} |  {libro[1]} |  {libro[2]}")

        return libros

    
    # MODIFICAR
   

    def modificar_libro(self, id_libro, titulo, autor, seccion, cantidad, precio):
        """
        Modifica los datos de un libro existente por su ID.
        Parámetros: id_libro y los nuevos datos del libro
        """
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
            UPDATE libros
            SET titulo=?, autor=?, seccion=?, cantidad=?, precio=?
            WHERE id=?
        """, (titulo, autor, seccion, cantidad, precio, id_libro))

        conexion.commit()
        conexion.close()
        print(f"Libro ID {id_libro} modificado correctamente.")

    
    # ELIMINAR
    

    def eliminar_libro(self, id_libro):
        """
        Elimina un libro de la base de datos por su ID.
        Parámetro: id_libro (int)
        """
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("DELETE FROM libros WHERE id=?", (id_libro,))

        conexion.commit()
        conexion.close()
        print(f"Libro ID {id_libro} eliminado correctamente.")