#Faça um programa que receba uma nota do aluno e se for superior ou igual a 7 apareça mensagem que ele esta aprovado, se for iferior a 5 ele esta "nao aprovado/reprovado direto" 
#e se estiver entre 5 e 7 apareça a mensagem "nao aprovado/ recuperação"
nota = float(input("Digite a nota do aluno: "))

if nota >= 7:
    print('Ele está aprovado')
else:
    if nota < 5:
        print('Ele está reprovado')
    else:
        print('Ele está de recuperação')