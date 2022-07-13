class DispositivosEntrada:

    def __init__(self, tipoEntrada, marca):
        self._tipoEntrada = tipoEntrada
        self._marca = marca

    def getTipoEntrada(self):
        return self._tipoEntrada

    def setTipoEntrada(self, tipoEntrada):
        self._tipoEntrada = tipoEntrada

    def getMarca(self):
        return self._marca

    def setMarca(self, marca):
        self._marca = marca

    def comunicarseConLaPc(self):
        pass    

    