import pandas as pd
import collections

tabela = pd.read_excel("r01.xlsx")

tabela_enviado = tabela['Para quem gostaria de enviar a curtida?']

nomes = []

for nome in tabela_enviado:
    nomes.append(nome)

#print(nomes)

repetidos = collections.Counter(nomes)
print(repetidos)
