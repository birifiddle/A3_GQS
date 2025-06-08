import unittest
import math
from formas import Quadrado, Retangulo, Circulo
from calculadora import CalculadoraDeArea

class TestCalculadoraDeArea(unittest.TestCase):
    def test_quadrado(self):
        area = CalculadoraDeArea(Quadrado(4)).calcular()
        self.assertEqual(area, 16)

    def test_retangulo(self):
        area = CalculadoraDeArea(Retangulo(4, 5)).calcular()
        self.assertEqual(area, 20)

    def test_circulo(self):
        area = CalculadoraDeArea(Circulo(3)).calcular()
        self.assertAlmostEqual(area, math.pi * 9, places=5)

if __name__ == "__main__":
    unittest.main()
