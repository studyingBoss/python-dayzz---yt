'''
style:  0 - normal
        1 - negrito
        4 - underline
        7 - passar cor do fundo pra letra e a recíproca

text:   30 - letra cinza
        31 - vermelha
        32 - verde
        33 - amarela
        34 - azul
        35 - violeta
        36 - verde marinho
        37 - branco

back:   40 - fundo cinza
        41 - fundo vermelho
        42 - verde
        43 - amarelo
        44 - azul
        45 - violeta
        46 - verde marinho
        47 - branco


\033[0;30;41m

\033[4;33;44m

\033[1;35;43m

\033[30;42m

\033[7;30m 

print('\033[7;37;mHello, world!\033[m')

a = 3
b = 5
print('Os valores são \033[32;44m{}\033[m e \033[31;44m{}\033[m.'.format(a, b))


name = 'João'
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', name, '\033[m'))
'''

name = 'João'
cores = {'limpa':'\033[m', 
        'azul':'\033[34m', 
        'amarelo':'\033[33m', 
        'pretoebranco':'\033[7;37m'}

print('Olá! Muito prazer em te conhecer, {}{}{}!'.format(cores['pretoebranco'], name, cores['limpa']))