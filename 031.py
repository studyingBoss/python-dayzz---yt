dist = float(input('Distância da viagem: '))

if dist <= 200:
    prc = 0.5 * dist
else:
    prc = 0.45 * dist

print('O preço da viagem é de R${:.2f}. \nA distância viajada é de {} Km.'.format(prc, dist))
