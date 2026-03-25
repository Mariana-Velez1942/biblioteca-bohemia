
class Libro:

    def __init__(self, titulo, autor, seccion, cantidad, precio):
    
        # --- Validaciones ---

        if cantidad < 0:
            raise ValueError("Error: La cantidad no puede ser negativa.")

        if precio < 0:
            raise ValueError("Error: El precio no puede ser negativo.")

        if titulo.strip() == "" or autor.strip() == "":
            raise ValueError("Error: El título y autor no pueden estar vacíos.")

        # --- Variables del libro ---
        self.titulo   = titulo.strip()
        self.autor    = autor.strip()
        self.seccion  = seccion.strip()
        self.cantidad = cantidad
        self.precio   = precio

    def __str__(self):
        return (
            f"Título: {self.titulo}"
            f"Autor: {self.autor}"
            f"Sección: {self.seccion}"
            f"Cantidad: {self.cantidad}"
            f"Precio: ${self.precio:,.2f}"
        )