class PalabrasComunes:
    def __init__(self, lista1, lista2):
        self.lista1 = lista1
        self.lista2 = lista2

    def obtener_comunes(self):
        # Usamos conjuntos para eliminar duplicados y encontrar intersección
        comunes = set(self.lista1) & set(self.lista2)
        return list(comunes)