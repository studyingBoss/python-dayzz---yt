name = input('Digite o nome: ').strip()

print('O nome digitado foi {}. \nEste nome com todas as letras maiúsculas é {}. \nApenas em letras minúsculas: {}.'.format(name, name.upper(), name.lower()))

print('O nome digitado possui {} letras.'.format(len(name) - name.count(' ')))

dividido = name.split()
len(dividido[0]) 

print('O primeiro nome possui {} letras.'.format(len(dividido[0])))

name.find(' ') # dá a posição do primeiro espaço, então, é o tamanho do primeiro nome
               # Ana Maria: posição do primeiro espaço é a posição 3, que é o tamanho de 'Ana'

print('O primeiro nome tem {} letras.'.format(name.find(' '))) 