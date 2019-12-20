class Simulador:
    def __init__(self, vehiculos):
        self.vehiculos = vehiculos

    def iniciar_simulacion(self, dias):
        for v in self.vehiculos:
            print("\n")
            print("VEHICULO {}".format(v.placa))
            for dia on range(1, dias + 1):
                distancia = random.randint(0,100)
                print("----------------------")
                print("Dia {}".format(dia))
                print("----------------------")
                litros = random.randint(1,100)
                v.recorrer_distancia()
            v.obtener_reporte()
