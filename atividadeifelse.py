#Faça um programa que o usuario digite um número e diga se o númeo é superior a 20, inferior a 10 ou se esta entre 10 e 20
num = int(input('Digite um número: '))

if num < 10:
    print('Ele é menor que 10')
elif num > 20:
    print('Ele é maior que 20')
else:
    print('Ele está entre 10 e 20')