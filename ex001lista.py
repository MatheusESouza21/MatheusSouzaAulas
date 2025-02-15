Lista1 = [1,2,3,4,5]
Lista2 = [6,7,8,9,10]
Lista3 = [11,12,13,14,15]
todas_Listas = [Lista1,Lista2,Lista3]
print(todas_Listas)

produtos = ['tv','celular','mouse','teclado','tablet']
print(produtos[1])

produtos2 = ['tv','celular','mouse','tablet']
vendas = [1000, 1500, 350, 270, 900]
print('As vendas de {} foram de {}'.format(produtos2[1],vendas[1]))

produtos3 = ['tv','celular','mouse','teclado','tablet']

i = produtos3.index('mouse')
print('O valor de i é '+ str(i))
print('O produto da posição i é '+ str(produtos3[i]))

produtos4 = ['tv','celular','mouse','teclado','tablet','geladeira','forno']
estoque = [100,150,100,120,70,180,80]
produto4 = input('Insira o nome do produto e letra minuscula: ')

if produto4 in produto4:
    i = produtos.index(produtos4)
    qntde_estoque = estoque[i]
    print('Temos {} unidades de {} no estoque'.format(qntde_estoque,produto4))
else:
    print('temos {} não existe no estoque'.format(produto4))