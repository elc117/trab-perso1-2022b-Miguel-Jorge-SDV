#VIDEO 2
#VIDEO 3

from random import randint

class Pessoa:
    anoAtual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def getAnoNascimento(self):
        print(self.anoAtual - self.idade)

    @classmethod
    def porAnoNascimeto(cls, nome, anoNascimento):
        idade = cls.anoAtual - anoNascimento
        return cls(nome, idade)

    @staticmethod
    def geraId():
        rand = randint(10000, 19999)
        return rand

p1 = Pessoa('Luiz', 32)
print(p1)
print(p1.nome, p1.idade)
p1.getAnoNascimento()
print(Pessoa.geraId())
print(p1.geraId())