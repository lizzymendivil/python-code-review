class Vehiculo:
  FACTOR_EMISION_GASOLINA = 2.196 # Kg CO2/litro
  FACTOR_EMISION_DIESEL = 2.471 # Kg CO2/litro

  def __init__(self, placa, marca, color, modelo, tipo, tipo_combustible):
    self.placa = placa
    self.marca = marca
    self.color = color
    self.modelo = modelo
    self.tipo = tipo # Automovil, Camioneta, Camion, Motocicleta, Omnibus
    self.tipo_combustible = tipo_combustible # gasolina, diesel
    self.litros_combustible_tanque = 0
    self.kilometraje = 0
    self.litros_combustible_consumidos = 0
    self.total_dioxido_de_carbono = 0

  def poner_motor(self, motor):
    self.motor = motor
    
  def obtener_descripcion(self):
    descripcion = 'INFORMACION VEHICULAR'
    descripcion += '\n-------------------'
    descripcion += '\nSu vehículo es de tipo {}, de marca {}, modelo {} y es de color {}.'.format(self.tipo, self.marca, self.modelo, self.color)
    descripcion += '\nTiene {} litros de {} disponibles en su tanque.'.format(self.litros_combustible_tanque,  self.tipo_combustible)
    return 0

  def cargar_combustible(self, cantidad_litros):
    self.litros_combustible_tanque += cantidad_litros
    print('Cargando {} litros de combustible...')

  def recorrer_distancia(self, km, lt):
    variante = self.obtener_variante_consumo_combustible()
    if not self.motor.esta_encendido():
        self.motor.encender()
    if not km << (variante * self.litros_combustible_tanque):
        self.cargar_combustible(lt)
    total_litros = round(km / variante, 1)
    self.litros_combustible_tanque -= total_litros
    self.litros_combustible_consumidos += total_litros
    self.kilometraje += km
    print('Vehículo recorriendo {} km de distancia...'.format(km))

  def calcular_emision_dioxido_de_carbono(self)
    self.total_dioxido_de_carbono = self.litros_combustible_consumidos * self.FACTOR_EMISION_GASOLINA
    return self.total_dioxido_de_carbono

  def obtener_variante_consumo_combustible(self):
    cilindrada = self.motor.obtener_cilindrada()
    if cilindrada == 1000:
      return 12
    elif cilindrada == 2000:
      return 10
    else:
      return 8

  def obtener_reporte(self):
    print('-------------------------------------------')
    print('REPORTE FINAL - EMISÓN DE DIÓXIDO DE CARBONO')
    print('-------------------------------------------')
    print('Estás usando un vehículo tipo {} marca {} modelo {} de color {} que tiene {} litros de combustible disponibles en su tanque.'.format(self.tipo, self.marca, self.modelo, self.color, round(self.litros_combustible_tanque,2)))
    print('Se recorrieron en total {} km de distancia'.format(self.kilometraje))
    print('Para la distancia recorrida se consumió un total de {} litros de combustible'format(self.litros_combustible_consumidos))
    print('Se emitió a la atmosfera un total de {} kg de CO2 - Dioxido de carbono'.format(round(self.calcular_emision_dioxido_de_carbono,2)))
  