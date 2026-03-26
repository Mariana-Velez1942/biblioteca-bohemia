from database import conectar

class Usuario:
    def __init__(self, nombre, apellido, correo, contrasena):
        if nombre.strip() == "" or apellido.strip() == "":
            raise ValueError("Error: Nombre y apellido no pueden estar vacíos.")

        if "@" not in correo or "." not in correo:
            raise ValueError("Error: Correo electrónico inválido.")

        if len(contrasena) < 4:
            raise ValueError("Error: La contraseña debe tener al menos 4 caracteres.")

        self.nombre     = nombre.strip()
        self.apellido   = apellido.strip()
        self.correo     = correo.strip().lower()
        self.contrasena = contrasena

    def __str__(self):
        return (
            f"Nombre: {self.nombre} {self.apellido}\n"
            f"Correo: {self.correo}"
        )


class GestorUsuarios:

    # ------------------ CREATE ------------------
    def registrar(self, usuario):
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute(
            "SELECT * FROM usuarios WHERE correo = ?",
            (usuario.correo,)
        )
        existe = cursor.fetchone()

        if existe:
            print("Error: Ese correo ya está registrado.")
            conexion.close()
            return False

        cursor.execute(
            "INSERT INTO usuarios (nombre, apellido, correo, contrasena) VALUES (?, ?, ?, ?)",
            (usuario.nombre, usuario.apellido, usuario.correo, usuario.contrasena)
        )

        conexion.commit()
        conexion.close()
        return True

    # ------------------ (LOGIN) ------------------
    def iniciar_sesion(self, correo, contrasena):
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute(
            "SELECT * FROM usuarios WHERE correo = ? AND contrasena = ?",
            (correo.strip().lower(), contrasena.strip())
        )

        usuario = cursor.fetchone()
        conexion.close()
        return usuario

    # ------------------(LISTAR) ------------------
    def listar_usuarios(self):
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("SELECT id, nombre, apellido, correo FROM usuarios")
        usuarios = cursor.fetchall()
        conexion.close()

        if not usuarios:
            print("No hay usuarios registrados.")
            return []

        print("\nUSUARIOS REGISTRADOS:")
        print("-"*50)
        for u in usuarios:
            print(f"ID: {u[0]} | {u[1]} {u[2]} | {u[3]}")
        print("-"*50)

        return usuarios

    # ------------------ UPDATE ------------------
    def modificar_usuario(self, id_usuario, nombre, apellido, correo, contrasena):
        conexion = conectar()
        cursor = conexion.cursor()

        # Validación básica
        if nombre.strip() == "" or apellido.strip() == "":
            print("Error: Nombre y apellido no pueden estar vacíos.")
            return

        if "@" not in correo or "." not in correo:
            print("Error: Correo inválido.")
            return

        if len(contrasena) < 4:
            print("Error: Contraseña muy corta.")
            return

        cursor.execute("""
            UPDATE usuarios
            SET nombre=?, apellido=?, correo=?, contrasena=?
            WHERE id=?
        """, (nombre.strip(), apellido.strip(), correo.strip().lower(), contrasena, id_usuario))

        conexion.commit()
        conexion.close()

        print(f"Usuario ID {id_usuario} modificado correctamente.")

    # ------------------ DELETE ------------------
    def eliminar_usuario(self, id_usuario):
        conexion = conectar()
        cursor = conexion.cursor()

        # Ayuda a no eliminar admin
        if id_usuario == 1:
            print("No se puede eliminar el administrador.")
            return

        cursor.execute("DELETE FROM usuarios WHERE id=?", (id_usuario,))

        conexion.commit()
        conexion.close()

        print(f"Usuario ID {id_usuario} eliminado correctamente.")