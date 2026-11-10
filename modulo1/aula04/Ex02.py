from math import ceil
comprimento = float(input('Digite o comprimento: '))
largura = float(input('Digite a largura: '))
altura = float(input('Digite a altura: '))
area_total = (comprimento * altura) * 2 + (largura * altura) * 2
total_caixas = (area_total) / 1.5
print(f'O total de caixas de azuleijo é {ceil(total_caixas)}')
