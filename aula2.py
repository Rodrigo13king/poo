from aula1 import pessoa

aluno01= pessoa(peso=78,nome="Rodrigo",idade=30)
aluno02= pessoa(peso=90,nome="Rodri",idade=32)
print(aluno01.comer("Cachorro quente"))

print(aluno01.falando("com george"))


class pessoa():
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




