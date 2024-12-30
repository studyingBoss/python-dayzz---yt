""" num = int(input('Número: '))

n = str(num)
print('Analisando o número {}.'.format(num))
print('Unidade: {}; \nDezena: {}; \nCentena: {}; \nMilhar: {}.'.format(n[3], n[2], n[1], n[0]))
 """
# solução acima tem problema, só funciona se colocares quatro dígitos no número

num = int(input('Número: '))
u = num // 1 % 10 # unidade é o resto da divisão de num por 10
d = num // 10 % 10 # num // 10 pegará os 3 primeiros dígitos; o resto da divisão por 10 dará o rightmost dígito 
c = num // 100 % 10 
m = num // 1000
print('Analisando o número {}.'.format(num))
print('Unidade: {}; \nDezena: {}; \nCentena: {}; \nMilhar: {}.'.format(u, d, c, m))