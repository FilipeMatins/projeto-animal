class Animal:
    nome=''
    coracao=bool
    racional=bool
    instinto=bool
    tamanho=''
    sexo=str

    animais = list


    def __init__(self, nome,coracao):
        self.nome = nome
        self.coracao = coracao

class Humano(Animal):
    idioma=''

    def __init__(self,nome,tamanho,idioma,sexo):
       
       self.nome = nome
       self.idioma=idioma
       self.coracao=True
       self.racional=True
       self.instinto=True
       self.tamanho=tamanho
       self.sexo=sexo     

    # def imprimir_humano(self):

    #     print(self.nome)
    #     print(self.idioma)
    #     print(self.tamanho)
    #     print(self.sexo)

class Cachorro(Animal):
    raca=''

    def __init__(self,nome,tamanho, raca, sexo):
        self.nome=nome
        self.tamanho = tamanho
        self.raca = raca
        self.coracao=True
        self.racional=False
        self.instinto=True
        self.sexo=sexo

    # def imprimir_cachorro(self):

    #     print(self.nome)
    #     print(self.tamanho)
    #     print(self.raca)
    #     print(self.sexo)


class Cavalo(Animal):
    raca=''

    def __init__(self,nome,tamanho, raca, sexo):
        self.nome=nome
        self.tamanho = tamanho
        self.raca = raca
        self.coracao=True
        self.racional=False
        self.instinto=True
        self.sexo=sexo

    def info(self):
        return{'nome': self.nome
               }
    # def imprimir_cavalo(self):

    #     print(self.nome)
    #     print(self.tamanho)
    #     print(self.raca)
        # print(self.sexo)


# cao = Cachorro('safira',10,'pinscher','femea')
# homem = Humano('Filipe','português', 1.70, 'Masculino')
# cavalo = Cavalo('Morramedi',2.30,'Pamtaneiro','Macho')
# cao.imprimir_cachorro()
# print('-----------')
# # homem.imprimir_humano()