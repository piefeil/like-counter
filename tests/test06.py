import pandas as pd
from collections import Counter

tabela = pd.read_excel("r01.xlsx")

tabela_enviado = tabela['Para quem gostaria de enviar a curtida?']

nome = "Anne Bicalho"

def curtidas_recebidas(nome):
    freq = Counter(tabela_enviado).get(nome)
    print(freq)

curtidas_recebidas(nome)