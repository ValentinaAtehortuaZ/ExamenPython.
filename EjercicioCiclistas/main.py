from Ciclista import Ciclista

ciclistas=int(input('Digite el numero de ciclistas que va a digitar: '))

name=""
age=0
country=""
time=0
i=0
for i in range(ciclistas):
    
    name=input('Digite el nombre del ciclista: ')
    age=int(input('Digite la age: '))
    country=input('Digite el country: ')
    time=int(input('Digite el time (en minutos) recorrido por el ciclista: '))

    ciclista=Ciclista(name, age, country, time)
    tiempoMenor=ciclista.calcularTiempoMenor()

print(tiempoMenor)
