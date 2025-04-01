class PalabrasComunes:
    def __init__(self, lista1, lista2):
        self.lista1 = lista1
        self.lista2 = lista2

    def obtener_comunes(self):
        # Usamos conjuntos para eliminar duplicados y encontrar intersección
        comunes = set(self.lista1) & set(self.lista2)
        return list(comunes)

# Ejemplo de uso
if __name__ == "__main__":
    lista1 = ["manzana", "pera", "uva", "manzana", "naranja"]
    lista2 = ["pera", "naranja", "kiwi", "uva", "uva"]

    palabras = PalabrasComunes(lista1, lista2)
    resultado = palabras.obtener_comunes()

    print("Palabras comunes:", resultado)