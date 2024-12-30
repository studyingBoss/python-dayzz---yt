""" n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

print(type(n1))


s = n1+n2
print('A soma vale:', s)
print('A soma vale: {}'.format(s))
print('A soma entre', n1, 'e', n2, 'vale', s)
print('A soma entre {} e {} vale {}'.format(n1, n2, s))
 """

""" n = input('Digite algo:')
print(n.isnumeric())
 """

m = input('Digite algo: ')
print(type(m))
print(m.isalnum()) #checks whether m is alphanumeric (input has only numbers and/or letters)
print(m.isnumeric()) #checks whether m has only numbers and outputs True or False
print(m.isalpha()) #checks whether m is a in the alphabet, not if it is a string

