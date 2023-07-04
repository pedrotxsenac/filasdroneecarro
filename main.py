from Veiculo import Veiculo
from Carro import Carro
from Drone import Drone
from FilaCarros import FilaCarros
from FilaDrones import FilaDrones

fila_carros = FilaCarros()
fila_drones = FilaDrones()

while True:
    menu = input(""" ----------------

1 - Adicionar Carro na fila.
2 - Remover primeiro Carro da fila.
3 - Imprimir fila de Carros.
4 - Adicionar Drone na fila.
5 - Remover Drone da fila.
6 - Imprimir fila de Drones

DIGITE O NÚMERO DA FERRAMENTA QUE QUER UTILIZAR: """)

    if menu == "1":
        marca = input("digite a marca: ")
        modelo = input ("digite o modelo: ")
        portas = input("digite a quantidade de portas: ")

        carro = Carro(marca, modelo, portas)
        fila_carros.add(carro)
 
    if menu == "2":
        fila_carros.remover()

    if menu == "3":
        fila_carros.imprimir()

    if menu == "4":
        marca = input("digite a marca: ")
        modelo = input ("digite o modelo: ")
        qtdHelices = input("digite a quantidade de hélices: ")

        drone = Drone(marca, modelo, qtdHelices)
        fila_drones.add(drone)

    if menu == "5":
        fila_drones.remover()
    
    if menu == "6":
        fila_drones.imprimir()