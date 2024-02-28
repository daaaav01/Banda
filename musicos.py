from instrumento import *

class Musico:
    def __init__(self,nombre):
        self.nombre = nombre
        self.instrumento = None
    
    def asignar_instrumento(self,instrumento):
        self.instrumento = instrumento
    
    def afinar_instrumento(self):
        self.instrumento.afinar()

    def tocar_instrumento(self):
        self.instrumento.tocar()
