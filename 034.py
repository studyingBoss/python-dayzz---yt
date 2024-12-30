slr = float(input('Digite o salário do funcionário: '))
print('O salário do funcinário é de R${:.2f}.'.format(slr))

if slr > 1250:
    inc = slr * 0.1
    print('O aumento de seu salário será de R${:.2f}. \nTotalizando um salário de R${:.2f}.'.format(inc, slr+inc))
else:
    inc = slr * 0.15
    print('O aumento de seu salário será de R${:.2f}. \nTotalizando um salário de R${:.2f}.'.format(inc, slr+inc))