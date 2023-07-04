class Veiculo:
    
	def __init__(self, marca, modelo):
		self.marca = marca
		self.modelo = modelo

	def __str__(self) -> str:
		texto = "Marca: " + self.marca 
		texto += "\nModelo: " + self.modelo
		return texto
	
	def imprimirInformacoes(self):
		print( self )