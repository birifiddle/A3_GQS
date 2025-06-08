import math
from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def calcular_area(self) -> float:
        pass

class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self) -> float:
        return self.lado ** 2

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self) -> float:
        return self.largura * self.altura

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self) -> float:
        return math.pi * self.raio ** 2
