meta = 20000
vendas = 50000

if vendas < meta:
    print('Não ganhou bônus')
elif vendas > (meta*2):
    bonus = 0.07 * vendas
    print('Ganhou {} e bônus'.format(bonus))
else:
    bonus = 0.03 * vendas
    print('Ganhou {} de bonus'.format(bonus))