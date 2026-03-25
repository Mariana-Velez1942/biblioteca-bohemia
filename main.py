from database import creacion_tabla, crear_tabla_usuarios
from libro import Libro
from biblioteca import Biblioteca
from usuarios import Usuario, GestorUsuarios

def pantalla_inicial():
    print("\n" + "="*50)
    print("BIBLIOTECA BOHEMIA")
    print("="*50)
    print("  1. Acceso Administrador")
    print("  2. Acceso Usuario")
    print("  0. Salir")
    print("="*50)


def menu_admin():
    print("\n" + "="*50)
    print("PANEL ADMINISTRADOR")
    print("="*50)
    print("  1. Agregar libro")
    print("  2. Listar todos los libros")
    print("  3. Buscar / Filtrar libros")
    print("  4. Modificar libro")
    print("  5. Eliminar libro")
    print("  6. Gestionar usuarios")  # 👈 NUEVO
    print("  0. Cerrar sesión")
    print("="*50)


def menu_usuario():
    print("\n" + "="*50)
    print("PANEL USUARIO")
    print("="*50)
    print("  1. Listar todos los libros")
    print("  2. Buscar / Filtrar libros")
    print("  0. Cerrar sesión")
    print("="*50)


def menu_usuarios():  # 👈 NUEVO
    print("\n" + "="*50)
    print("GESTIÓN DE USUARIOS")
    print("="*50)
    print("  1. Listar usuarios")
    print("  2. Modificar usuario")
    print("  3. Eliminar usuario")
    print("  0. Volver")
    print("="*50)


def submenu_busqueda():
    print("\n" + "-"*40)
    print("BUSCAR / FILTRAR LIBROS")
    print("-"*40)
    print("  1. Buscar por título")
    print("  2. Buscar por autor")
    print("  3. Filtrar por sección")
    print("  0. Volver")
    print("-"*40)


def menu_acceso_usuario():
    print("\n" + "="*50)
    print("ACCESO USUARIO")
    print("="*50)
    print("  1. Iniciar sesión")
    print("  2. Crear cuenta nueva")
    print("  0. Volver")
    print("="*50)


def flujo_busqueda(bib):
    while True:
        submenu_busqueda()
        op = input("\n👉 Elige una opción: ")

        if op == "1":
            titulo = input("Ingresa el título a buscar: ")
            bib.buscar_por_titulo(titulo)

        elif op == "2":
            autor = input("Ingresa el autor a buscar: ")
            bib.buscar_por_autor(autor)

        elif op == "3":
            seccion = input("Ingresa la sección a filtrar: ")
            bib.filtrar_por_seccion(seccion)

        elif op == "0":
            break

        else:
            print("Opción inválida.")


def agregar(bib):
    print("\n--- ➕ AGREGAR LIBRO ---")
    titulo  = input("Título   : ")
    autor   = input("Autor    : ")
    seccion = input("Sección  : ")

    while True:
        try:
            cantidad = int(input("Cantidad : "))
            if cantidad < 0:
                print("La cantidad no puede ser negativa.")
            else:
                break
        except ValueError:
            print("Ingresa un número entero válido.")

    while True:
        try:
            precio = float(input("Precio   : "))
            if precio < 0:
                print("El precio no puede ser negativo.")
            else:
                break
        except ValueError:
            print("Ingresa un número válido.")

    try:
        libro = Libro(titulo, autor, seccion, cantidad, precio)
        bib.agregar_libro(libro)
    except ValueError as e:
        print(e)


def modificar(bib):
    print("---MODIFICAR LIBRO ---")
    bib.listar_libros()

    try:
        id_libro = int(input("\nIngresa el ID del libro a modificar: "))
    except ValueError:
        print("ID inválido.")
        return

    titulo  = input("Nuevo título   : ")
    autor   = input("Nuevo autor    : ")
    seccion = input("Nueva sección  : ")

    while True:
        try:
            cantidad = int(input("Nueva cantidad : "))
            if cantidad < 0:
                print("La cantidad no puede ser negativa.")
            else:
                break
        except ValueError:
            print("Ingresa un número entero válido.")

    while True:
        try:
            precio = float(input("Nuevo precio   : "))
            if precio < 0:
                print("El precio no puede ser negativo.")
            else:
                break
        except ValueError:
            print("Ingresa un número válido.")

    bib.modificar_libro(id_libro, titulo, autor, seccion, cantidad, precio)


def eliminar(bib):
    print("--- ELIMINAR LIBRO ---")
    bib.listar_libros()

    try:
        id_libro = int(input("\nIngresa el ID del libro a eliminar: "))
        confirmacion = input(f"¿Seguro que deseas eliminar el libro ID {id_libro}? (s/n): ")
        if confirmacion.lower() == "s":
            bib.eliminar_libro(id_libro)
        else:
            print("Eliminación cancelada.")
    except ValueError:
        print("ID inválido.")


def login_admin(gestor):
    print("--- ACCESO ADMINISTRADOR ---")
    correo     = input("Correo     : ")
    contrasena = input("Contraseña : ")

    usuario = gestor.iniciar_sesion(correo, contrasena)

    if usuario and usuario[1] == "Admin":
        print(f"Bienvenido/a, {usuario[1]} {usuario[2]}!")
        return True
    else:
        print("Credenciales incorrectas o no tienes permisos de administrador.")
        return False


def login_usuario(gestor):
    print("--- INICIAR SESIÓN ---")
    correo     = input("Correo     : ")
    contrasena = input("Contraseña : ")

    usuario = gestor.iniciar_sesion(correo, contrasena)

    if usuario and usuario[1] != "Admin":
        print(f"Bienvenido/a, {usuario[1]} {usuario[2]}!")
        return usuario
    else:
        print("Correo o contraseña incorrectos.")
        return None


def registro_usuario(gestor):
    print("--- CREAR CUENTA ---")
    nombre     = input("Nombre     : ")
    apellido   = input("Apellido   : ")
    correo     = input("Correo     : ")
    contrasena = input("Contraseña : ")

    try:
        usuario = Usuario(nombre, apellido, correo, contrasena)
        exito = gestor.registrar(usuario)

        if exito:
            print(f"¡Cuenta creada exitosamente!")
            print(f"Bienvenido/a, {usuario.nombre} {usuario.apellido}!")
            return usuario
        else:
            return None

    except ValueError as e:
        print(e)
        return None


def main():
    creacion_tabla()
    crear_tabla_usuarios()

    bib    = Biblioteca()
    gestor = GestorUsuarios()

    while True:
        pantalla_inicial()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            if login_admin(gestor):
                while True:
                    menu_admin()
                    op = input("Elige una opción: ")

                    if op == "1":
                        agregar(bib)
                    elif op == "2":
                        bib.listar_libros()
                    elif op == "3":
                        flujo_busqueda(bib)
                    elif op == "4":
                        modificar(bib)
                    elif op == "5":
                        eliminar(bib)

                    # 👇 NUEVO BLOQUE USUARIOS
                    elif op == "6":
                        while True:
                            menu_usuarios()
                            opu = input("Elige una opción: ")

                            if opu == "1":
                                gestor.listar_usuarios()

                            elif opu == "2":
                                gestor.listar_usuarios()
                                try:
                                    idu = int(input("ID del usuario: "))
                                    nombre = input("Nuevo nombre: ")
                                    apellido = input("Nuevo apellido: ")
                                    correo = input("Nuevo correo: ")
                                    contrasena = input("Nueva contraseña: ")
                                    gestor.modificar_usuario(idu, nombre, apellido, correo, contrasena)
                                except ValueError:
                                    print("ID inválido.")

                            elif opu == "3":
                                gestor.listar_usuarios()
                                try:
                                    idu = int(input("ID del usuario a eliminar: "))
                                    gestor.eliminar_usuario(idu)
                                except ValueError:
                                    print("ID inválido.")

                            elif opu == "0":
                                break

                            else:
                                print("Opción inválida.")

                    elif op == "0":
                        print("Sesión de administrador cerrada.")
                        break
                    else:
                        print("Opción inválida.")

        elif opcion == "2":
            while True:
                menu_acceso_usuario()
                op = input("Elige una opción: ")

                if op == "1":
                    usuario = login_usuario(gestor)
                    if usuario:
                        while True:
                            menu_usuario()
                            opu = input("Elige una opción: ")

                            if opu == "1":
                                bib.listar_libros()
                            elif opu == "2":
                                flujo_busqueda(bib)
                            elif opu == "0":
                                print("Sesión cerrada. ¡Hasta luego!")
                                break
                            else:
                                print("Opción inválida.")
                        break

                elif op == "2":
                    usuario = registro_usuario(gestor)
                    if usuario:
                        while True:
                            menu_usuario()
                            opu = input("Elige una opción: ")

                            if opu == "1":
                                bib.listar_libros()
                            elif opu == "2":
                                flujo_busqueda(bib)
                            elif opu == "0":
                                print("Sesión cerrada. ¡Hasta luego!")
                                break
                            else:
                                print("Opción inválida.")
                        break

                elif op == "0":
                    break

                else:
                    print("Opción inválida.")

        elif opcion == "0":
            print("¡Hasta luego! Gracias por usar Biblioteca Bohemia.")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()