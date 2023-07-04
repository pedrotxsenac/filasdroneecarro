from Carro import Carro

class FilaCarros:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self.tamanho = 0

    def add(self, carro):
        no = carro
        if self.primeiro == None:
            self.primeiro = no
            self.ultimo = no
        else:
            self.ultimo.proximo = no
            self.ultimo = no
        self.tamanho += 1
        self.imprimir()


    def remover(self):
        if self.primeiro == None:
            print("Lista Vazia")
        elif self.primeiro.proximo == None:
            self.primeiro = None
            self.ultimo = None
            self.tamanho = 0
        else:
            self.primeiro = self.primeiro.proximo
            self.tamanho -= 1
        self.imprimir()



    def imprimir(self):
        texto = ""
        if self.primeiro == None:
            texto = "Lista Vazia"
        else:
            aux = self.primeiro
            while( aux ):
                texto += "Marca: " + str(aux.marca) + " - Modelo: " + str(aux.modelo) + " - Portas:" + str(aux.getPortas()) + "\n" 
                aux = aux.proximo
        print("-----------")
        print( texto )
        print("Total de elementos: ", str(self.tamanho) )