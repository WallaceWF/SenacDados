for n in range(1,11):
    aluno = input('Seu nome: ')
    n1 = float(input('Primeira nota: '))
    n2 = float(input('Segunda nota: '))
    media = (n1 + n2) / 2
    print('=~'*10)
    print(f'Aluno {aluno}')
    print('Situação: ', end='')
    if media >= 6:
        print('Aluno APROVADO!')
    elif 3 <= media < 6:
        print('Aluno em RECUPERAÇÃO!')
    else:
        print('Aluno REPROVADO!')
    print('=~'*10)

