from formas import Quadrado, Retangulo, Circulo
from calculadora import CalculadoraDeArea

formas = [
    Quadrado(4),
    Retangulo(4, 5),
    Circulo(3)
]

for forma in formas:
    calc = CalculadoraDeArea(forma)
    print(f"Área: {calc.calcular():.2f}")
