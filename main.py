from models.Raton import Raton
from models.Teclado import Teclado
from models.Monitor import Monitor
from models.Computadora import Computadora
from models.Orden import Orden


raton = Raton("usb", "philco", 3200)
raton2 = Raton("usb", "tavel", 7200)
raton2.comunicarse()

teclado = Teclado("usb", "lenovo", "qwerty")
teclado2 = Teclado("usb2", "lenovo2", "qwerty2")


monitor = Monitor("HP", 14)
monitor2 = Monitor("Dell", 27)
print(raton)
print(teclado)
print(monitor)

computadora1 = Computadora("HP", monitor, "raton", teclado)
computadora2 = Computadora("Dell", monitor2, raton2, teclado2)

print(computadora1)
print(computadora2)

orden = Orden()
orden.aregarComputadoras(computadora1)
orden.aregarComputadoras(computadora2)
orden.mostrarOrden()

orden2 = Orden()
orden2.aregarComputadoras(computadora2)
orden2.aregarComputadoras(computadora2)
orden2.aregarComputadoras(computadora1)
orden2.mostrarOrden()
