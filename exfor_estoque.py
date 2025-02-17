estoque = [1200,300,800,1500,19,45,20,170,102,80,1100,34,70]
produtos = ['coca cola','pepsi','guarana','skol','brahma','agua','del valle','red bull','dolly','fanta','sprite','sukita','pepsi twist']
nivel_minimo = 50
for i, qtde in enumerate(estoque):
    if qtde < nivel_minimo:
      print(produtos[i],qtde)