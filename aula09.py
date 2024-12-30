""" frase = 'Curso em Vídeo Python'

len(frase) # dá quantidade de caracteres da string; neste caso, len(frase) recebe o número 21
frase.count('o') #conta quantidade de 'o' minúsculo na string; recebe valor 3; tem que botar entre aspas, sem aspas pensaria que é uma variável
frase.count('o', 0, 13) #conta quantidade de 'o' minúsculos na string, do caractér 0 até o 12
frase.find('deo') # diz onde 'deo' começou, no caso, retorna posição 11
frase.find('Android') # não existe a string, então retorna valor -1, significa que string 'Android' não existe na string 'Curso em Vídeo Python'

'Curso' in frase # retorna True se 'Curso' existir na string 'Curso em Vídeo Python'; False otherwise

frase.replace('Python','Android') # substitui string 'Python' pela string 'Android', tornando a string 'Curso em Vídeo Python', mas não substitui diretamente na string - variável frase continua recebendo exatamente a mesma coisa

frase.upper() # transforma string em toda maiúscula
frase.lower() #transforma string em toda minúscula
frase.capitalize() # transforma string toda em minúscula, e então transforma a primeira letra de toda string em maiúscula

frase.title() # transforma toda primeira letra de cada palavra em maiúscula

frase = '   Aprenda Python  ' # espaços no começo e no fim, coisa de gente super leiga em computadores
frase.strip() #remove espaços antes de 'Aprenda' e depois de 'Python', mas não interefere com o espaço no meio das duas palavras; notar que caractér A era o 3a caractér na string, e por causa do strip, torna-se o caractér 0a

frase.rstrip() # remove somente espaços à direita da string, no caso de '   Aprenda Python  ', remove os dois espaços depois de 'n', tornando a string em '   Aprenda Python', string vai agora de 0 a 16, com len de 17 caracteres

frase.lstrip() #remove espaços no extremo esquerdo

frase = 'Curso em Vídeo Python'
frase.split() # cria divisões na string frase: 'Curso' 'em' 'Vídeo' 'Python', vários bloquinhos, onde cada bloquinho recomeça a contar do caractér zero; por ex., na string frase normal, 'e' de 'em' é o caractér 6, mas em frase.split(), 'e' de 'em' é o caractér zero. Também, 'Curso' 'em' 'Vídeo' 'Python'. Também, forma uma lista ['Curso', 'em', 'Vídeo', 'Python'] onde a palavra zero é 'Curso', 'em' é a palavra um, além de que em cada uma dessas palavras, você número a posição de cada letra 

'-'.join(frase) # gera string 'Curso-em-Vídeo-Python'; coloca a string '-' onde tem espaço na string frase 

frase = 'Curso em Vídeo Python'
print(frase)
print(frase[3:13]) # printa da letra na posição 3 (s) até a letra na posição 12 (e)
print(frase[:13]) # posição zero até posição 12
print(frase[13:]) # posição 13 até final
print(frase[1:15]) # posição 1 até posição 14 o print
print(frase[1:15:2]) # posição 1 até posição 14, pulando de 2 em 2
print(frase[::2]) # não tem início nem final, então é string inteira; pulando de 2 em 2

print(frase.count('o')) # como em Python tudo é objeto, dá pra botar ponto no fim de frase e dale o count

print(frase.upper().count('O')) # frase.upper() torna string frase tudo em maiúsculo, e depois o count('O') vai contar os 'O' maiúsculos, sendo que todos os 'o' viraram 'O' por causa de frase.upper()

print(len(frase)) # tamanho da string
frase = '    Curso em Vídeo Python  '
print(len(frase)) # espaços em branco também são contados para o tamanho da string, considerando os espaços nas extremidades
print(len(frase.strip())) # mostra o length de frase strippada

frase = 'Curso em Vídeo Python'
print(frase.replace('Python', 'Android')) # 1a parâmetro será trocado pelo 2a parâmetro

frase = 'Curso em Vídeo Python'
frase[0] = J 
# não funciona, pois string em Python é imutável, apenas usando frase.replace; não muda efetivamente a string, é só um módulo 

frase = 'Curso em Vídeo Python'
frase = frase.replace('Python', 'Android') # faz o replace e depois faz frase receber essa alteração, daí alterou a string porque mudou a string na variável frase 

print('Curso' in frase)

frase = 'Curso em Vídeo Python'
print(frase.find('Curso')) # printa 0 porque é posição onde string 'Curso' começa
# se desse find em 'curso', ele printaria -1 porque 'curso' não existe, apenas 'Curso', letra maiúscula em C


frase = 'Curso em Vídeo Python'
print(frase.split())
"""
frase2 = 'Curso em Vídeo Python'
dividido = frase2.split()
print(dividido[0]) # printa 'Curso', pois ela é o elemento zero da lista dividido
print(dividido[2][3]) # vai olhar elemento 2 em dividido, que é 'Vídeo' e printar elemento 3 dele, que é 'e'