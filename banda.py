from musicos import *
from random import choice

class Banda:

    def __init__(self):
        self.musicos = []
        self.instrumentos = [Guitarra(), Saxofon(), Triple(), Bajo(), Piano(), Bateria(), Trompeta(), Maracas(), Violin(), Flauta()]
        self.amigos = ["brayan", "kevin", "yursley", "justin", "lady", "sneider", "deiber", "yasbleidy", "yuyeimi", "brandon"]

    def crear_banda(self, cantidad_musicos):
        for i in range(cantidad_musicos):
            self.musicos.append(Musico(choice(self.amigos)))
            self.musicos[-1].asignar_instrumento(choice(self.instrumentos))
    
    def afinar_banda(self):
        for m in self.musicos:
            print(m.afinar_instrumento())
    
    def tocar_banda(self):
        for m in self.musicos:
            print(m.tocar_instrumento())
    
    def mostrar_banda(self):
        for m in self.musicos:
            print(m.nombre)
            print(m.instrumento.mostrar())

if __name__ == "__main__":
    b = Banda()
    b.crear_banda(3)
    b.mostrar_banda()
    print("afinamos la banda")
    b.afinar_banda()
    print("a tocar:")
    b.tocar_banda()

