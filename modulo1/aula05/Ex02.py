for p in range(1,13):
    nome = input('Seu nome: ')
    ano = int(input('Ano de nascimento:'))
    idade = 2026 - ano
    print('=~'*15)
    if idade < 18:
        print(f'Candidato(a): {nome}')
        print(f'Idade: {idade}')
        print(f'Situação: MENOR DE IDADE! Não será possível participar')
    else:
        print(f'Situação: Admissível para participar!')
        email = input('Informe o E-mail: ')
        telefone = int(input('Informe o núm de telefone [Digitar apenas números]: '))
        print('=~'*15)
        print(f'Candidato(a): {nome}')
        print(f'Idade: {idade}')
        print(f'E-mail: {email}')
        print(f'Telefone: {telefone}')
    print('=~'*15)