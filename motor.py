class Motor:
    
  def _init_(self, nro_serie, cilindrada):
    self.nro_serie = nro_serie,
    self.cilindrada = cilindrada
    self.encendido = "False"

  def obtener_cilindrada(self):
    return self.cilindrada

  def encender(self):
    self.encendido = True

  def apagar():
    self.encendido = False

  def esta_encendido(self):
    return self.encendido
