from Veiculo import Veiculo

class Carro(Veiculo):
    
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.__portas = portas
        self.proximo = None

    def __str__(self) -> str:
        texto = super().__str__() + "\n Portas: " + self.__portas
        return texto
    
    def getPortas(self):
        return self.__portas

    def imprimir(self):
        print(self)


