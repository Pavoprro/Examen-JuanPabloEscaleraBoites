from clases.areas import Areas

if __name__ == "__main__":
    calc = Areas()
    calc.leer_numero()
    print("triangulo", calc.area_triangulo())
    print("rectangulo", calc.area_rectangulo())

    calc.leer_radio()
    print("circulo", calc.area_circulo())
