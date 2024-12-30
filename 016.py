"""from math import trunc
num = float(input('Digite um número: '))
integer = trunc(num)
print('O número digitado é {}. \nSua porção inteira é {}.'.format(num, integer))

import math
num = float(input('Digite um número: '))
integer = math.trunc(num)
print('O número digitado é {}. \nSua porção inteira é {}. \nEsta, com apenas duas casas após a vírgula, é {:.2f}.'.format(num, integer, num))"""

num = float(input('Digite um número: '))
print('O número digitado é {}. \nSua parte inteira é {}.'.format(num, int(num))) #função int() dará a parte inteira do número; não precisaria importar library