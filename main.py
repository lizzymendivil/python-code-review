from vehiculo import Vehiculo
from simulador import Simulador

motor1 = Motor('78pm4450a', 1000)
motor2 = Motor('9uppkm098', 2000)
motor3 = Motor('9uppkm098', 3000)

auto1 = Vehiculo('3797IYH', 'Suzuki', 'Azul Cielo', '2014', 'Automovil', 'gasolina')
auto1.poner_motor(motor1)

auto2 = Vehiculo()
auto2.poner_motor(motor2)

auto3 = Vehiculo('5996PKY', 'Nissan', 'Verde', '2018', 'Automovil', 'gasolina')
auto3.poner_motor()

lista_vehiculos = [auto1, auto2, auto3]

simulador = Simulador()
simulador.iniciar_simulacion()
