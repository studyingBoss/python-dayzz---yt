# cada aresta tem que ser menor que a soma das outras duas para formar um triângulo

print('-='*30, '\nAnalisador de Triângulos')
print('-='*30)

r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É possível formar um triângulo com esses segmentos de reta!')
else:
    print('Não é possível formar um triângulo.')
