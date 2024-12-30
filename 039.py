from datetime import date

brth = int(input('Ano de nascimento: '))
age = date.today().year - brth

print('O ano atual é {}. O ano de nascimento da pessoa é {}. \nComparando-os, a pessoa tem {} anos.'.format(date.today().year, brth, age))

if age > 18:
    print('A pessoa tem mais de 18 anos, logo, já se alistou no serviço militar. Já passou {} anos de seu alistamento.'.format(age-18))
    print('A pessoa se alistou em {}.'.format(brth+18))
elif age == 18:
    print('A pessoa tem exatamente 18 anos. É hora de se alistar no serviço militar.')
else:
    print('A pessoa tem menos de 18 anos. Ela ainda vai se alistar no serviço militar. Ainda faltam {} anos para o alistamento.'.format(18-age))
    print('A pessoa se alistará no ano {}.'.format(brth+18))
    