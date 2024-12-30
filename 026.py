frase = input('Frase: ').strip()
print('A frase é {} \nA quantidade de letras A, maísculas e minúsculas, é {}.'.format(frase, frase.upper().count('A')))

print('A primeira letra A apareceu na posição {}.'.format(frase.upper().find('A')+1))
print('Última posição de A é {}.'.format(frase.upper().rfind('A')+1)) # rfind vai começar a procura pela DIREITA da string 