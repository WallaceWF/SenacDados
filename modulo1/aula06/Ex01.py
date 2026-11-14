resultado = list()
print('=~'*10)
for n in range(1,6):
    print(f'Aluno {n}')
    n1 = float(input('Primeira nota: '))
    n2 = float(input('Segunda nota: '))
    print('=~'*10)
    media = (n1 + n2)/ 2
    if media >= 6:
        resultado.append(f'Aluno {n} - Situação: APROVADO!')
    elif 3 <= media < 6:
        resultado.append(f'Aluno {n} - Situação: EM RECUPERAÇÃO!')
    else:
        resultado.append(f'Aluno {n} - Situação: REPROVADO!')
for n in resultado:
    print(n)

        