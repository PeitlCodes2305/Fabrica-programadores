#definindo variaveis

nome = input("Digite o nome do aluno: ")
nota_1 = float(input("Digite a primeira nota do aluno: "))
nota_2 = float(input("Digite a segunda nota do aluno: "))
nota_3 = float(input("Digite a terceira nota do aluno: "))

#calculando a media
media = (nota_1 + nota_2 + nota_3) / 3

if media >= 7:
    print(f"{nome} foi aprovado com média {media:.2f}")
elif media >= 4:
    print(f"{nome} ficou de recuperação com média {media:.2f}")
else:
    print(f"{nome} foi reprovado")