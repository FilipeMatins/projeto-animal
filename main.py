from classe import * 
from views import *
from crud import *

lista_de_cao = []
lista_de_humano = []
lista_de_cavalo = []

def criar_cao():
    nome = input("Nome do Cão: ")
    tamanho = input("Tamanho do cão em centimentros: ")
    raca = input("Raça do cão: ")
    sexo = input('digite o sexo do cachorro:')
    cao = Cachorro(nome,tamanho,raca,sexo)
    lista_de_cao.append(cao)

def criar_humano():
    nome = input("Nome do humano: ")
    tamanho = input("Tamanho do humano: ")
    idioma = input("Idioma que o humano fala: ")
    sexo = input('digite o genero: ')
    homem = Humano(nome,tamanho,idioma,sexo)
    lista_de_humano.append(homem)

def criar_cavalo():
    nome = input("Nome do Cavalo: ")
    tamanho = input("Tamanho do cavalo: ")
    raca = input("Raça do Cavalo: ")
    sexo = input('digite o sexo: ')
    cavalo = Cachorro(nome,tamanho,raca,sexo)
    lista_de_cavalo.append(cavalo)


def listar_humano(lista):
    for objeto in lista:
        print(objeto.info())

menu = menu_principal()
menu2 = menu_listar()
while True:
    print(menu)        
    op = input("Escolha uma opção: ")
    if op == '1': 
        criar_humano()
    elif op == '2':
        criar_cao()
    elif op == '3':
        criar_cavalo()
    elif op == '4':
        print(menu2)
        op = input("Escolha uma opção: ")
        if op == '1':
            print(listar_humano)
    else:
        print("Opção Inválida")