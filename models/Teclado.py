from models.DispositivosEntrada import DispositivosEntrada

class Teclado(DispositivosEntrada):
    contadorTeclados = 0

    def __init__(self, tipoEntrada, marca, tipoTeclado):
        super().__init__(tipoEntrada, marca)
        Teclado.contadorTeclados += 1
        self._idTeclado = Teclado.contadorTeclados
        self._tipoTeclado = tipoTeclado

    def getIdTeclado(self):
        return self._idTeclado
    
    def getTipoTeclado(self):
        return self._tipoTeclado

    def setTipoTeclado(self, tipoTeclado):
        self._tipoTeclado = tipoTeclado

    def __str__(self):
        return f"idTeclado: {self._idTeclado}, Tipo de entrada: {self._tipoEntrada}, Marca: {self._marca}"
    
    def conectar(self):
        print("Conectando teclado por" + self._tipoEntrada)
    
    def desconectar(self):
        print("Desconectando teclado por" + self._tipoEntrada)

    def comunicarseConLaPc(self):
        print("escribir...")