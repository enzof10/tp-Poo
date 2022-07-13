class Orden:
    contadorOrdenes = 0

    def __init__(self):
        self._idOrden = ++Orden.contadorOrdenes
        self._computadoras = []

    def getIdOrden(self):
        return self._idOrden

    def aregarComputadoras(self, computadora):
        self._computadoras.append(computadora)

    def mostrarOrden(self):
        computadorasOrden = ""
        for computadora in self._computadoras:
            computadorasOrden += f"\n{computadora}"

        print(f"Orden {self._idOrden}, Computadoras: {computadorasOrden} ")

    def __str__(self):
        return self.mostrarOrden()

    def __repr__(self):
        return self.mostrarOrden()

    def __eq__(self, other):
        return self._idOrden == other._idOrden

    def __hash__(self):
        return hash(self._idOrden)

    def __lt__(self, other):
        return self._idOrden < other._idOrden

    def __gt__(self, other):
        return self._idOrden > other._idOrden

    def __le__(self, other):
        return self._idOrden <= other._idOrden

    def __ge__(self, other):
        return self._idOrden >= other._idOrden

    def __ne__(self, other):
        return self._idOrden != other._idOrden

    def __add__(self, other):
        return self._idOrden + other._idOrden