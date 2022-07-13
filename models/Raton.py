from .DispositivosEntrada import DispositivosEntrada

class Raton(DispositivosEntrada):
    contadorRatones = 0

    def __init__(self, tipoEntrada, marca, dpi):
        super().__init__(tipoEntrada, marca)
        Raton.contadorRatones += 1
        self._idRaton = Raton.contadorRatones
        self._dpi = dpi

    def getIdRaton(self):
        return self._idRaton

    def getDpi(self):
        return self._dpi

    def setDpi(self, dpi):
        self._dpi = dpi
    
    def __str__(self):
        return f"idRaton: {self._idRaton}, Tipo de entrada: {self._tipoEntrada}, Marca: {self._marca}"

    def conectar(self):
        print("Conectando raton por" + self._tipoEntrada)

    def desconectar(self):
        print("Desconectando raton por" + self._tipoEntrada)

    def comunicarseConLaPc(self):
        print("mover y clickar...")