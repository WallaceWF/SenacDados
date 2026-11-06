n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))
media = (n1 + n2 + n3 + n4) / 4
if media > 7:
    print('Aluno APROVADO!')
elif 5 <= media <= 7:
    print('Aluno em RECUPERAÇÃO!')
else:
    print('Aluno REPROVADO!')
 