class CalculadoraDeArea:
    def __init__(self, forma):
        self.forma = forma

    def calcular(self) -> float:
        return self.forma.calcular_area()
