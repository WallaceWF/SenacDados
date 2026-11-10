print('=~'*15)
print('TABELA DE CÓDIGOS'.center(27))
print('=~'*15)
print(f"{'Código 1':<19} -  SUL")
print(f"{'Código 2':<19} -  NORTE")
print(f"{'Código 3':<19} -  LESTE")
print(f"{'Código 4':<19} -  OESTE")
print(f"{'Código 5/6':<19} -  NORDESTE")
print(f"{'Código 7/8/9':<19} -  SUDESTE")
print(f"{'Código 10':<19} -  CENTRO-OESTE")
print(f"{'Código 11':<19} -  NOROESTE")
opcao = int(input('Digite o código para a região desejada: '))
match opcao:
    case 1:
        print('REGIÃO SUL')
    case 2:
        print('REGIÃO NORTE')
    case 3:
        print('REGIÃO LESTE')
    case 4:
        print('REGIÃO OESTE')
    case 5 | 6:
        print('REGIÃO NORDESTE')
    case 7 | 8 | 9:
        print('REGIÃO CENTRO-OESTE')
    case 10:
        print('REGIÃO CENTRO-OESTE')
    case 11:
        print('REGIÃO NOROESTE')
    case _:
        print('Produto Importado!')



