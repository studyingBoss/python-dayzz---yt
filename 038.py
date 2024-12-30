n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))

if n1 > n2:
    print('O primeiro valor é {}. O segundo valor é {}. \nO primeiro valor é maior.'.format(n1, n2))
elif n2 > n1:
    print('O primeiro valor é {}. O segundo valor é {}. \nO segundo valor é maior.'.format(n1, n2))
else:
    print('O primeiro valor é {}. O segundo valor é {}. \nOs dois números são iguais.'.format(n1, n2))