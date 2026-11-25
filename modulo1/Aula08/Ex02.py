def contar_caractere(msg,caractere):
    quantidade = msg.count(caractere)
    return quantidade

msg = input('Digite uma frase: ').lower()
caractere = input('Digite o caractere a ser contado: ').strip().lower()

contador = contar_caractere(msg,caractere)
print(f'O total de letra "{caractere}" no texto é de: {contador} unidades')
