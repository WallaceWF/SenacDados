candidatos_validos = list()
candidatos_invalidos = list()
candidato = dict()
print('=~'*10)
for n in range(1, 3):
    print(f'Candidato {n}')
    candidato['idade'] = int(input('Sua idade: '))
    if candidato['idade'] > 18:
        print('Candidato Valido - PROSSEGUINDO COM O CADASTRO!')
        candidato['nome'] = input('Seu nome: ')
        candidato['email'] = input('Seu E-mail: ')
        candidatos_validos.append(candidato.copy())
    else:
        print('Candidato MENOR DE IDADE - Não foi possível prosseguir!')
    print('=~'*10)
print('>>> DADOS CADASTRAIS')
print('=~'*10)
for pessoa in candidatos_validos:
    print(
        f'Nome: {pessoa['nome']}\n'
        f'Idade: {pessoa['idade']}\n'
        f'E-mail: {pessoa['email']}'
    )
    print('=~'*10)



