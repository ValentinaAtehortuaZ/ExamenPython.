
class Ciclista:    
    def __init__(self,name,age,country,time):
        self.name=name
        self.age=age
        self.country=country
        self.time=time

    def calcularTiempoMayor(self):
        mayor=0
        if(mayor<self.time):
            mayor=self.time

            datosCiclista={
              self.name,
              self.age,
              self.country,
              self.time
            }

            return datosCiclista
        return 'el timpo debe ser mayor a 0'

    def mostrarTiempo(self,datosCiclista):
        print(datosCiclista)
