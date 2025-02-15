nomes = ['Matheus','Rafael','Daniel','Caio']
telefone = [1000,2000,3000,4000]
bairro = ['bairro1','bairro2''bairro3','bairro4']

nome = input('Insira um nome: ')

if nome in nomes:
    i = nome.index(nome)
    telefones = telefone[i]
    bairros = bairro[i]
    print('O número de {} é {} e seu bairro é o {}'.format(nome,telefones,bairros))
else:
    print('{} não existe na lista'.format(nome))
