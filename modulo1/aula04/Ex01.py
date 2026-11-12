from math import ceil
potencia = float(input('Potencia: '))
largura = float(input('Digite a largura: '))
comprimento = float(input('Digite o comprimento: '))
area = largura * comprimento
bocal = ceil(area / 3)
wats_total = area * 3
quantia_lampadas = bocal
wats_obtido = quantia_lampadas * potencia
print('=~'*20)
print('INFORMAÇÕES SOBRE O AMBIENTE'.center(40))
print('=~'*20)

print(f'Area total: {area}')
print(f'Quantidade total de bocais: {bocal}')
print(f'Quantidade de watts necessária para iluminar todo o ambiente: {wats_total}')
print(f'Potência utilizada pelas lampadas: {potencia}')
print('=~'*20)
if wats_total > wats_obtido:
    print('Potência insuficiente para iluminar o ambiente!')
else:
    print('O ambiente foi devidamente iluminado!')
    