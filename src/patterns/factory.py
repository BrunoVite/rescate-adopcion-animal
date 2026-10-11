from abc import ABC, abstractmethod


class Expediente(ABC):
    def __init__(self, id, nombre):
        self.id, self.nombre, self.estado = id, nombre, "Rescatado"

    def cambiar_estado(self, estado):
        self.estado = estado

    @abstractmethod
    def obtener_protocolo(self): ...


class ExpedientePerro(Expediente):
    def obtener_protocolo(self):
        return "Vacunacion + desparasitacion canina"


class ExpedienteGato(Expediente):
    def obtener_protocolo(self):
        return "Vacunacion + esterilizacion felina"


class ExpedienteFauna(Expediente):
    def obtener_protocolo(self):
        return "Cuarentena + aviso a autoridad ambiental"


class ExpedienteFactory:
    """Factory Method: crea el expediente segun la especie."""
    TIPOS = {"perro": ExpedientePerro, "gato": ExpedienteGato, "fauna": ExpedienteFauna}

    @classmethod
    def crear(cls, especie, id, nombre):
        return cls.TIPOS[especie.lower()](id, nombre)
