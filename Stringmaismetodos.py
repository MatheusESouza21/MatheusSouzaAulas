#TRANSOFMA APENAS A PRIMEIRA LETRA DE UMA STRING EM MAIÚSCULA
nome = "matheus"
print(nome.capitalize(),"\n")

#TRANSFORMA TODAS AS LETRAS EM MINUSCULA
nome = "MATHEUS"
print(nome.casefold(),"\n")

#CONTA O NUMERO DE VEZES QUE UM CARACTERE ESPECIFICO APARECE NA STRING
nome = "matheusesouza@mail.com"
print(nome.count('s'),"\n")

#RETORNA true OU false PARA UM TESTE SE A STRING TERMINA COM UMA STRING ESPECIFICA
nome = "matheusesouza@gmail.com"
print(nome.endswith('gmail.com'),"\n")

#ENCONTRA A POSIÇÃO DO TERMO PROCURADO. LEMBRE-SE COMEÇA DO zero
nome = "matheusesouza@gmail.com"
print(nome.find('@'),"\n")

#VERIFICA SE O TEXTO É todo FEITO COM LETRAS
nome = "Matheus"
print(nome.isalpha(),"\n")

#VERIFICA SE O TEXTO É FEITO COM numeros
nome = "123"
print(nome.isnumeric(),"\n")

#SUBSTITUI UM CARACTERE ESCOLHIDO POR OUTRO
nome = "Matheus"
print(nome.replace('us','o'),"\n")

#SEPARA O TEXTO string BASEADO EM ALGUM CARACTERE INDICADO
nome = "Matheus @ Camille"
print(nome.split('@'),"\n")

#COLOCAR TODAS AS LETRAS INICIAIS EM MAIUSCULA
nome = "Matheus Eduardo Souza"
print(nome.title(),"\n")

#RETIRA OS CARACTERES INDESEJADOS, COMO POR EXEMPLO espaços QUE NÃO AGREGAM VALOR
nome = "  matheus eduardo souza  "
print(nome.strip(),"\n")

#RETORNA true OU false PARA UM TESTE DE UMA STRING SE INICIA COM UM TEXTO ESPECIFICO
nome = "matheus 2009"
print(nome.startswith("ser"),"\n")
print(nome.startswith("ser"),"\n")