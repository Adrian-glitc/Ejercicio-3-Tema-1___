from Palabras_Comunes import PalabrasComunes
# Ejemplo de uso
if __name__ == "__main__":
    lista1 = ["manzana", "pera", "uva", "manzana", "naranja"]
    lista2 = ["pera", "naranja", "kiwi", "uva", "uva"]

    palabras = PalabrasComunes(lista1, lista2)
    resultado = palabras.obtener_comunes()

    print("Palabras comunes:", resultado)