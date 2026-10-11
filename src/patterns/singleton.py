from observer import Sujeto


class GestorCasos(Sujeto):
    """Singleton: unica instancia del motor de gestion de casos."""
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            Sujeto.__init__(cls._instancia)
            cls._instancia.casos = []
        return cls._instancia

    def registrar_caso(self, expediente):
        self.casos.append(expediente)
        self.notificar(expediente)
