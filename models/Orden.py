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
