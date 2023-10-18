import pandas as pd

tabela = pd.read_excel("curtidas.xlsx")

tabela_enviado = tabela['Para quem gostaria de enviar a curtida?']
print(tabela_enviado)

lucas = []

for nome in tabela_enviado:
    if nome == "Lucas Silva":
        lucas.append(nome)

print(lucas)

contagem_lucas = len(lucas)

print(contagem_lucas)

