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
        print(f"{self.nome}Foi Comer Capim")
class Gato():
    def __init__(self,nome,cor):
        super().__init__(nome,cor)
    def miar(self):
        print(f"O{self.nome}Foi Miar")


class ingresso():
    def __init__(self,valor):
        super().__init__(valor=valor)
    def imprimeValor(self):
        print(f"O valor do ingresso e  {self.valor} ")
class Vip ():
    def __init__(self, valor):
      super().__init__(valor)
      self.valor*=1.5
    def imprimeValorVip(self):
      print(f"O valor do ingresso e  Vip{self.valor} ")

class Forma():
    def __init__(self):
        self.area=0
        self.perimetro=0

class Retangulo():
    def __init__(self):
        super().__init__()
    def calculaArea(self,base,altura):
        self.area=base*altura
        print(f"A área do Retangulo é {self.area}")
    def calculaperimetro(self,base,altura):
        self.perimetro=(base+altura)*2
        print(f"o PERIMETRO DO RETANGULO É {self.perimetro}")


