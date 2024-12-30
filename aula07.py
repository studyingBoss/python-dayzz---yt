"""  nome = input('Qual é seu nome? ')
print('Prazer em te conhecer, {:23}!'.format(nome)) #  :23 dentro de {} faz nome ser printado num total de 23 characters; printa o nome e enche de blank até totalizar 23 characters; se ultrapassar os 23 foda-se;

print('Prazer em te conhecer, {:>23}!'.format(nome)) # símbolo > faz nome começar à direita dos 23 espaços; por padrão, usa-se < e começa à esquerda dos 23 espaços

print('Prazer em te conhecer, {:^23}!'.format(nome)) #símbolo ^ alinha nome no meio dos 23 espaços

print('Prazer em te conhecer, {:=^20}!'.format(nome)) #símbolo ^ alinha nome no meio dos 23 espaços, e símbolo de igualdade = preenche todos os espaços não preenchidos por input 

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma vale {}!'.format(n1+n2))
print('A soma vale {}, o produto vale {} e a divisão vale {:.3f}!'.format(s, m, d), end=' ') # end=' ' faz não quebrar a linha entre este print e o próximo; o que está dentro dos parenteses fica entre eles


print('Divisão inteira vale {} e exponenciação vale {}!'.format(di, e))

# print('A soma vale {}, o produto vale {} e a divisão vale {:.3f}!'.format(s, m, d))    se quisesse com apenas três casas decimais; f de float, "3 float", 3 casas decimais

print('A soma vale {} \no produto vale {}\ne a divisão vale {:.3f}!'.format(s, m, d)) # \n faz a quebra de linha no print; tive que colar o resto da string no \n, senão a próxima linha do print já viria com um espaço de distância da extremidade esquerda
 """

#desafio besta
""" 
num1 = int(input('Digite o número: '))
print('O número é {} \nseu antecessor é {} \nseu sucessor é {}!'.format(num1, num1-1, num1+1)) """
""" 
num1 = int(input('Digite o número: '))
print('O número é {}! \nSeu dobro é {}! \nSeu triplo é {}! \nSua raiz quadrada é {}!'.format(num1, num1*2, num1*3, num1**(1/2))) """

""" n1 = int(input('Uma nota: '))
n2 = int(input('Outra nota: '))
m = (n1+n2)/2

print('A nota da P1 é {}. \nA nota da P2 é {}. \nA média aritmética do aluno é {}.'.format(n1, n2, m))
 """
""" 
m = int(input('Um valor em metros: '))
c = m*100
mm = m*1000

print('O valor em metros é {}. \nO valor em centímetros é {}. \nO valor em milímetros é {}.'.format(m, c, mm)) """
""" 
n1 = int(input('Um valor: '))
print('O valor é {0}. \nSua tabuada é: \n{1} X 0 = {2} \n{3} X 1 = {4} \n{5} X 2 = {6} \n{7} X 3 = {8} \n{9} X 4 = {10} \n{11} X 5 = {12} \n{13} X 6 = {14} \n{15} X 7 = {16} \n{17} X 8 = {18} \n{19} X 9 = {20} \n{21} X 10 = {22} \nFim da tabuada!'.format(n1, n1, n1*0, n1, n1*1, n1, n1*2, n1, n1*3, n1, n1*4, n1, n1*5, n1, n1*6, n1, n1*7, n1, n1*8, n1, n1*9, n1, n1*10)) """
""" 
w = int(input('Valor na carteira: '))
print('A pessoa pode comprar {} dólares.'.format(w/3.27)) """
""" 
largura = int(input('Largura: '))
altura = int(input('Altura: '))
área = largura * altura

#cada litro de tinta pinta 2m²

print('A parede tem uma largura de {} metros. \nA parede tem uma altura de {} metros. \nA parede tem uma área de {} metros quadrados. \nSão necessários {} litros de tinta para pintar a parede.'.format(largura, altura, área, área/2)) """

""" p = int(input('Preço: '))
print('O preço do produto é {} reais. \nSeu novo preço, com desconto de 5%, será {} reais.'.format(p, p*0.95))
 """

""" s = int(input('Salário: '))
print('O salário normal do funcionário é {}. \nSeu novo salário, com aumento de 15%, é de {}.'.format(s, s*1.15))
 """

#fui burro fiz os exs. na file da aula na real o guanabara que foi paia sla