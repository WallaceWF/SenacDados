n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
if media >= 6:
    print('Situação da prova regular: APROVADO!')
elif 3 <= media < 6:
    print('Situação da prova regular: RECUPERAÇÃO')
else:
    print('Situação da prova regular: REPROVADO')

optativa = float(input('Nota Optativa [Digite -1 caso não tenha feito]: '))
if optativa == -1:
    print('O aluno não fez a prova optativa')
else:
    if n1 <= n2:
        n1 = optativa
    else:
        n2 = optativa
    media = n1 + n2
    if media >= 6:
        print('Situação da prova optativa: APROVADO!')
    elif 3 <= media < 6:
        print('Situdação da prova optativa: RECUPERAÇÃO')
    else:
        print('Situação da prova optativa: REPROVAO')




