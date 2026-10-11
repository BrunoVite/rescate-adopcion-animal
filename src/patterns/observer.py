class Sujeto:
    """Observer: sujeto que mantiene la lista de observadores."""

    def __init__(self):
        self._observadores = []

    def suscribir(self, observador):
        self._observadores.append(observador)

    def notificar(self, caso):
        for o in self._observadores:
            o.actualizar(caso)


class Personal:
    """Observador concreto: voluntario o veterinario."""

    def __init__(self, nombre, rol):
        self.nombre, self.rol = nombre, rol

    def actualizar(self, caso):
        print(f"[{self.rol}] {self.nombre}: nuevo caso #{caso.id} - {caso.nombre}")
