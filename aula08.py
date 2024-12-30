""" import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('O número é {}. \nSua raiz quadrada é {}.'.format(num, raiz))

print('O número é {}. \nSua raiz quadrada é {}.'.format(num, math.ceil(raiz))) # se quiser arredondar o valor da raiz para cima

print('O número é {}. \nSua raiz quadrada é {:.2f}.'.format(num, raiz)) #raiz com duas casas decimais 

from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)   #quando importar dessa forma, não precisa usar math.sqrt pra puxar a função da library; função já é puxada automaticamente
print('O número é {:.1f}. \nSua raiz quadrada é {:.3f}.'.format(num, raiz))

print('O número é {:.1f}. \nSua raiz quadrada é {:.3f}.'.format(num, floor(raiz)))

import random
num = random.random() #generates a random number from 0 to 1; float number
print(num)
num2 = random.randint(1,10) #generates a random integer number from 1 to 10; both 1 and 10 can be chosen
print(num2)"""

import emoji
print(emoji.emojize('Hello, world! :earth_americas:', use_aliases=True))