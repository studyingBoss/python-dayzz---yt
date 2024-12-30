from datetime import date
from time import sleep
yr = int(input('Digite o ano (Coloque 0 para analisar o ano atual): '))  # será bissexto se for divisível por 4  
print('Analisando se tal ano é bissexto...')
sleep(3)

if yr == 0:
    yr = date.today().year

if yr % 4 == 0 and yr % 100 != 0 or yr % 400 == 0:
    print('O ano {} é bissexto.'.format(yr))
else:
    print('O ano {} não é bissexto.'.format(yr))