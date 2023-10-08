import pandas as pd

tabela = pd.read_excel("r01.xlsx")

tabela_enviado = tabela['Para quem gostaria de enviar a curtida?']

nomes = set() # Armazena elementos únicos

for nome in tabela_enviado:
    if nome not in nomes:
        nomes.add(nome)


print(nomes)    

# Esse comando adiciona em uma lista todos os nomes presentes na tabela