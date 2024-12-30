num = int(input('Número: '))
print('''Escolha uma das bases para conversão: 
[ 1 ] para \033[34mbinário\033[m;
[ 2 ] para \033[30moctal\033[m;
[ 3 ] para \033[31mhexadecimal\033[m.''')


opt = int(input('Base escolhida: '))

if opt == 1:
    print('O número digitado foi {}. Em \033[34mbinário\033[m, ele equivale a {}.'.format(num, bin(num)[2:]))
elif opt == 2:
    print('O número digitado foi {}. Em \033[30moctal\033[m, ele equivale a{}.'.format(num, oct(num)[2:]))
elif opt == 3:
    print('O número digitado foi {}. Em \033[31mhexadecimal\033[m, ele equivale a {}.'.format(num, hex(num)[2:]))
else:
    print('Opção inválida.')