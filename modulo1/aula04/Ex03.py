odometro_inicial = float(input('Digite o valor inicial do odômetro'))
odometro_final = float(input('Digite o valor final do odômetro'))
km_total = odometro_final - odometro_inicial
combustivel_total = odometro_final - odometro_inicial
gasto = combustivel_total * 6.15
valor_recebido = float(input('Digite o valor total recebido dos passageiros: '))
lucro = valor_recebido - gasto
media = km_total / combustivel_total
if lucro < 0:
    print(f'O valor gasto {gasto}, foi maior que o valor recebido {valor_recebido}, SALDO NEGATIVO!')
else:
    print(f'O lucro diario foi: {lucro}')
print(f'A media de combustivel por KM foi: {media}')