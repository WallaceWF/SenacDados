cont = 3
usuario = 'teste'
senha = 123
print('Números de tentativas para executar o login: 3')
while cont != 0:
    usuario_ver = input('Nome de usuário: ')
    senha_ver = int(input('Senha: '))
    if usuario_ver == usuario and senha_ver == senha:
        print('Login efetuado com sucesso!')
        break
    elif usuario_ver == usuario and senha_ver != senha:
        print('Senha incorreta!')
    elif usuario_ver != usuario and senha_ver == senha:
        print('Usuário incorreto!')
    else:
        print('Usuário ou senha incorretos!')
    cont -= 1
    if cont > 0:
        print(f'Número de tentativas restantes: {cont}')
    else:
        print('Número de tentativas excedidas. Tente novamente mais tarde!')
