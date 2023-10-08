import pandas as pd

tabela = pd.read_excel("r01.xlsx")

tabela_enviado = tabela['Para quem gostaria de enviar a curtida?']
print(tabela_enviado)

anne = []

for nome in tabela_enviado:
    if nome == "Anne Bicalho":
        anne.append(nome)

print(anne)

contagem_anne = len(anne)

print(contagem_anne)

