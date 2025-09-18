import math

class Areas():
    def leer_numero(self):
        self.base= float(input("Ingresa la base de la figura "))
        self.altura = float(input("Ingrese la altura de la figura "))

    def leer_radio(self):
        self.radio= float(input("Ingrese el radio del circulo "))

    def area_triangulo(self):
        return ((self.base*self.altura)/2)

    def area_rectangulo(self):
        return (self.base*self.altura)
    
    def area_circulo(self):
        return (math.pi * (self.radio ** 2))
