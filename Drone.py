from Veiculo import Veiculo


class Drone( Veiculo ):
    def __init__(self, marca, modelo, qtdHelices):
        super().__init__(marca, modelo)
        self._quantidadeHelices = qtdHelices
        self.proximo = None

    def __str__(self) -> str:
        texto = super().__str__() + "\n Quantidade de hélices: " + self._quantidadeHelices
        return texto
    
    def imprimir(self):
        print(self)