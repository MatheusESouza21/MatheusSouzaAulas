pessoas_presentes = ['john snow','Jesse Pinkman','Aria Stark','Tyrion','Lannister']
chamada = 'Aria Stark'
for pessoa in pessoas_presentes:
    if pessoa == chamada:
        print('{} está presente.'.format(chamada))
        break
    else:
        print('Só um print para mostar que passou por essa pessoa: '+ str(pessoa))

pessoas_presentes = ['john snow','Jesse Pinkman','Aria Stark','Tyrion','Lannister']
chamada = 'Aria Stark'
for pessoa in pessoas_presentes:
    if pessoa == chamada:
        print('{} está presente.'.format(chamada))
        break
    else:
        print('Só um print para mostar que passou por essa pessoa: '+ str(pessoa))
        continue
        