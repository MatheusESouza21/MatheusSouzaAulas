venda = input('Registre um produto. Para cancelar o registro de um novo produto, basta apertar enter sem digitar nada: ')
vendas = [];
while venda != '':
    vendas.append(venda)
    venda = input('Registre um produto. Para cancelar o registro de um novo produto, basta apertar enter sem digitar nada: ')
print('Registros Finalizados. As vendas cadastradas foram: {}'.format(vendas))