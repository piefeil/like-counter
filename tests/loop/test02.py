import pandas as pd

tabela = pd.read_excel("curtidas.xlsx")

tabela_enviado = tabela['Para quem gostaria de enviar a curtida?']




nomes = []

for nome in tabela_enviado:
    nomes.append(nome) # Adiciona todos os nomes (repetidos) em uma lista 

print (nomes.count("Lucas Silva")) # Conta quantas vezes "Lucas Silva" apareceu




nomes_unicos = set() # Armazena elementos únicos

for nome in tabela_enviado:
    if nome not in nomes_unicos:
        nomes_unicos.add(nome) # Adiciona uma fez na lista todos os nomes que tem na tabela

print (nomes_unicos)



def contagem_nomes(nome):
    print (nome, nomes.count(nome))



for nome in nomes_unicos:
    contagem_nomes(nome)


# Adicionar uma forma de somar as 2 colunas 
# Organizar lista em ordem decrescente