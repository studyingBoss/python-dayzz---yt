from time import sleep
n = int(input('Número: '))

print('O número digitado é {}. \nAnalisando sua paridade...'.format(n))
sleep(3)

if n%2 == 0:
    print('O número analisado é par.')
else:
    print('O número analisado é ímpar.')