prc = float(input('Valor da casa: R$'))
slr = float(input('Salário do comprador: R$'))
yrs = float(input('Anos em que pagará: '))

mnts = yrs * 12
prst = prc / mnts
print('O valor da casa é de R${:.2f}. \nO pagamento será feito em {} meses. \nO salário do comprador é de R${:.2f}.'.format(prc, mnts, slr))

prnc = prst / slr * 100

if prst > slr * 0.3:
    print('A prestação mensal é de R${:.2f}. Isto equivale a {:.2f}% valor do salário do comprador. Ela ultrapassou trinta porcento do salário do comprador, logo, o empréstimo foi \033[1;31mNEGADO!\033[m'.format(prst, prnc))
else:
    print('A prestação mensal é de R${:.2f}. Isto equivale a {:.2f}% valor do salário do comprador. Ela não ultrapassou trinta porcento do salário do comprador, logo, o empréstimo foi \033[1;32mAPROVADO!\033[m'.format(prst, prnc))