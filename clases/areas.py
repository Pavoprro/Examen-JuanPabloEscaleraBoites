class Areas():
    def leer_numero(self):
        self.base= float(input("Ingresa la base de la figura "))
        self.altura = float(input("Ingrese la altura de la figura "))

    def area_triangulo(self):
        return ((self.base*self.altura)/2)

    def area_rectangulo(self):
        return (self.base*self.altura)
