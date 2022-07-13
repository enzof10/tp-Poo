class Monitor:
    contadorMonitores = 0

    def __init__(self, marca, tamano, resolucion):
        Monitor.contadorMonitores += 1
        self._idMonitor = Monitor.contadorMonitores
        self._marca = marca
        self._tamano = tamano
        self._resolucion = resolucion

    def getIdMonitor(self):
        return self._idMonitor

    def getMarca(self):
        return self._marca

    def setMarca(self, marca):
        self._marca = marca

    def getTamano(self):
        return self._tamano

    def setTamano(self, tamano):
        self._tamano = tamano

    def getResolucion(self):
        return self._resolucion

    def setResolucion(self, resolucion):
        self._resolucion = resolucion

    def toString(self):
        return f"idMonitor: {self._idMonitor}, Marca: {self._marca}, Tamaño: {self._tamano}"

    def __str__(self):
        return self.toString()

    