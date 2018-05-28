from Grafo import Grafo

grafo = Grafo()

start = True

while(start):
    option = input("Opcoes: \n Nova vertice (v) \n Nova Aresta (a) \n Existe Aresta entre dois vertices (e) \n Sair (s) \n")
    if(option == 's'):
        start = False
    elif(option == 'v'):
        iden = input('Digite o identificador: ')
        grafo.novo_Vertice(iden)
    elif(option == 'a'):
        iden1 = input('Digite o identificador de origem: ')
        iden2 = input('Digite o identificador de destino: ')
        peso = int(input('Digite o peso: '))
        grafo.nova_Aresta(iden1, iden2, peso)
        grafo.imprime_Grafo(iden1, iden2)