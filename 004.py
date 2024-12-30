a = input('Digite algo: ')
print('O tipo primitivo desse valor é: ',type(a))
print('Só tem espaços? ', a.isspace())
print('Só tem números?', a.isnumeric())
print('É alfabético, as in, there is nothing but letters?', a.isalpha())
print('É alfanumérico?', a.isalnum())
print('É tudo letra maiúscula?', a.isupper()) #checks only the letters
print('É tudo letra minúscula?', a.islower()) #checks only the letters; having a number on the string won't change it to False
print('Está capitalizada?', a.istitle())
