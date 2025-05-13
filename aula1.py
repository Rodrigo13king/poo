'''class pessoa():
    def __init__(self, peso, nome, idade):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.comendo = False
        self.falando = False
        self.dormindo = False

    def comer(self, comida):
        if self.comendo == True:
            print(f"{self.nome} Ja esta comendo")
        elif self.nome == True:
            print(f"{self.falando}NAO PODE COMER PQ ESTA FALANDO")
        else:
            print(f"{self.nome} foi comer {comida}")
            self.comendo = True
'''

class Animal():
    def __init__(self, nome, cor):
        self.nome=nome
        self.cor=cor

    def comer(self):
        print(f"{self.nome}Foi Comer")
class Gato(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)
    def miar(self):
        print(f"O{self.nome}foi Miando")