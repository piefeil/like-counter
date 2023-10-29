import pandas as pd

tabela = pd.read_excel("curtidas.xlsx")

tabela_enviado = tabela['Quem está enviando a curtida?']
tabela_recebido = tabela['Para quem gostaria de enviar a curtida?']

# Dicionários para armazenar as contagens de envio e recebimento para cada pessoa
nome_count_enviado = {}
nome_count_recebido = {}

# Calcular as contagens de envio e recebimento
for nome in tabela_enviado:
    if nome in nome_count_enviado:
        nome_count_enviado[nome] += 1
    else:
        nome_count_enviado[nome] = 1

for nome in tabela_recebido:
    if nome in nome_count_recebido:
        nome_count_recebido[nome] += 1
    else:
        nome_count_recebido[nome] = 1

print(nome_count_enviado)
print()
print(nome_count_recebido)


###### Abaixo não está funcionando #######


# Comparar os dicionários e calcular a soma total para nomes correspondentes
soma_total = {}
for nome in nome_count_enviado:
    if nome in nome_count_recebido and nome_count_enviado[nome] == nome_count_recebido[nome]:
        soma_total[nome] = nome_count_enviado[nome] + nome_count_recebido[nome]

# Imprimir a soma total para cada pessoa
for nome, soma in soma_total.items():
    print(f"{nome}: {soma}")

print (soma_total)
