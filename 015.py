dist = int(input('Quilômetros percorridos: '))
dias = int(input('Dias alugado: '))

aluguel = 60*dias + 0.15*dist

print('A quantidade de quilômetros percorridos foi {}. \nO automóvel foi alugado por {} dias. \nConsiderando a distância e o tempo de aluguel, o valor a pagar será R${:.2f}.'.format(dist, dias, aluguel))
