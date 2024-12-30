v = float(input('Velocidade: '))

print('A velocidade do carro é de {} Km/h.'.format(v))

if v > 80:
    multa = 7*(v-80)
    print('Por ter passado {} quilômetros acima do limite, o motorista terá que pagar uma multa de {} reais.'.format(v-80, multa))
