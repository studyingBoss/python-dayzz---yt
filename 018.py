""" import math

an = float(input('Digite o ângulo: '))
sin = math.sin(an)
cos = math.cos(an)
tan = math.tan(an)
print('O ângulo selecionado é {} radianos. \nO valor de seu seno vale {}. \nO valor de seu cosseno vale {}. \nO valor de sua tangente vale {}.'.format(an, sin, cos, tan))
 
#poderia usar math.radians() pra transformar graus em radianos 
import math
an = float(input('Digite o ângulo, em graus: '))
sin = math.sin(math.radians(an)) # an recebe valor em graus, transforma para radianos e usa esses radianos como parâmetro de math.sin(); o que vai dentro deste parâmetro é um valor em radianos, e math.sin() te entrega o valor do seno de tal radiano
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print('O ângul digitado é {} graus. \nEsse ângulo tem seno de valor {}. \nTambém, o ângulo tem cosseno de valor {}. \nO valor da tangente do ângulo de {} graus é {}.'.format(an, sin, cos, an, tan))
"""

from math import radians, sin, cos, tan
an = float(input('Digite o ângulo, em graus: '))
sin = sin(radians(an))
cos = cos(radians(an))
tan = tan(radians(an))
print('O ângulo é de {} graus. \nSeu seno vale {:.2f}. \nSeu cosseno vale {:.2f}. \nSua tangente vale {:.2f}.'.format(an, sin, cos, tan)) # valores trigonométricos com duas casas decimais