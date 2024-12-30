"""from math import sqrt

co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
 
hip = sqrt(co**2+ca**2)
print('O valor do cateto oposto é {}. \nO valor do cateto adjacente é {}. \nO valor da hipotenusa é {:.2f}, com apenas duas casas após a vírgula.'.format(co, ca, hip)) """
""" 
import math
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
hip = math.hypot(co, ca) #library math tem uma função para calcular hipotenusa; parâmetros são cateto oposto e cateto adjacente, nessa ordem (na real não importa ordem pra cálculo de hipotenusa)
print('O cateto oposto é {}. \nO cateto adjacente é {}. \nA hipotenusa é {:.2f}.'.format(co, ca, hip)) #hipotenusa com 2 casas decimais """

from math import hypot
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
hip = hypot(ca, co)
print('O cateto adjacente vale {1}. \nO cateto oposto vale {2}. \nA hipotenusa vale {0}.'.format(hip, ca, co))