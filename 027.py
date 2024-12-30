name = input('Nome: ').strip()
dividido = name.split()
print('O nome digitado é {}. \nO primeiro nome é {}. \nO último nome é {}.'.format(name, dividido[0], dividido[len(dividido)-1]))
