from factory import ExpedienteFactory
from singleton import GestorCasos


class CasoView:
    """MVC - Vista."""

    def mostrar(self, caso):
        print(f"Caso {caso.id}: {caso.nombre} -> {caso.estado} | {caso.obtener_protocolo()}")


class CasoController:
    """MVC - Controlador: coordina fabrica, gestor (modelo) y vista."""

    def __init__(self):
        self.gestor = GestorCasos()
        self.vista = CasoView()

    def crear_caso(self, especie, id, nombre):
        expediente = ExpedienteFactory.crear(especie, id, nombre)
        self.gestor.registrar_caso(expediente)
        self.vista.mostrar(expediente)
        return expediente
