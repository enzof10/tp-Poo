from models.Monitor import Monitor
from models.Raton import Raton
from models.Teclado import Teclado


class Computadora:
    contadorComputadora = 0
    monitor = Monitor
    raton = Raton
    teclado = Teclado

    def __init__(self, nombre, monitor, raton, teclado):
        Computadora.contadorComputadora += 1
        self._idComputadora = Computadora.contadorComputadora
        self._nombre = nombre
        self._monitor = monitor
        self._raton = raton
        self._teclado = teclado

    def toString(self):
        return f"Computadora {self._idComputadora}: {self._nombre} \n {self._monitor}\n {self._raton} \n {self._teclado}"

    def __str__(self):
        return self.toString()
