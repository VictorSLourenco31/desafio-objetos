# Definição da classe
from contextlib import nullcontext


class Hero:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        ataque = 0
        if self.tipo == 'Guerreiro':
            ataque = 'Espada'
            print(f'O {self.tipo} atacou usando {ataque}')
        elif self.tipo == 'Monge':
            ataque = 'Artes Marciais'
            print(f'O {self.tipo} atacou usando {ataque}')
        elif self.tipo == 'Ninja':
            ataque = 'Shuriken'
            print(f'O {self.tipo} atacou usando {ataque}')
        elif self.tipo == 'Mago':
            ataque = 'Magia'
            print(f'O {self.tipo} atacou usando {ataque}')


# Declaração de um objeto
heroi_1 = Hero(nome="Fred", idade=17, tipo='Guerreiro')
heroi_2 = Hero(nome="Derf", idade=20, tipo='Mago')
heroi_3 = Hero(nome="Frederick", idade=14, tipo='Monge')
heroi_4 = Hero(nome="Fredson", idade=41, tipo='Ninja')

heroi_1.atacar()
heroi_2.atacar()
heroi_3.atacar()
heroi_4.atacar()