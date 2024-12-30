import random
from time import sleep
n = input('Número: ')
resposta = random.randint(0,5)

print('-=-' * 30)
print('Pensando no número...')
print('-=-' * 30)
sleep(2) # espera 2 segundos

if (n == resposta):
    print('Valor correto!')
else:
    print('Chute errado!')

print('O valor randomizado era {}.'.format(resposta))