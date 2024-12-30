""" import random
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1, n2, n3, n4]

chosen = random.choice(lista)
print('Os alunos possíveis são {}, {}, {} ou {}. \nO escolhido para limpar o quadro é {}.'.format(n1, n2, n3, n4, chosen))
 """

from random import choice
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1, n2, n3, n4]
chosen = choice(lista)
print('Os alunos possíveis são {}, {}, {} e {}. \nO aluno escolhido foi {}.'.format(n1, n2, n3, n4, chosen))
