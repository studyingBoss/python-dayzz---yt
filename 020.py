""" from random import shuffle

n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1, n2, n3, n4]
shuffle(lista)
print('Os quatro alunos a apresentar são {}, {}, {} e {}. \nA ordem de apresentação será {}.'.format(n1, n2, n3, n4, lista)) """

import random

n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1, n2, n3, n4]
random.shuffle(lista)

print('Os quatro alunos a apresentar são {}, {}, {} e {}. \nA ordem de apresentação será {}.'.format(n1, n2, n3, n4, lista))