import pandas as pd

tabela = pd.read_excel("curtidas.xlsx")

tabela_enviado = tabela['Para quem gostaria de enviar a curtida?']

nomes = []

for nome in tabela_enviado:
    nomes.append(nome)

print(nomes)

