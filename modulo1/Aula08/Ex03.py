from random import randint
def rolar_ataque(n1):
    dado1 = randint(1, n1)
    return dado1
def rolar_dano(n2):
    dado2 = randint(1, n2)
    return dado2
n1 = int(input('Digite a quantidade de lados do dado de ataque: '))
n2 = int(input('Digite a quantidade de lados do dado de dano: '))
dado_ataque = rolar_ataque(n1)
dado_dano = rolar_dano(n2)
print(f'Resultado do dado para ataque: {dado_ataque}')
print(f'Resultado do dado para dano: {dado_dano}')