import pandas as pd

tabela = pd.read_excel("r01.xlsx")
#tabela_df = pd.DataFrame(tabela)

curtidas_recebidas_total = tabela['Para quem gostaria de enviar a curtida?'].value_counts()
curtidas_recebidas_df = pd.DataFrame(curtidas_recebidas_total)

#print (curtidas_recebidas_df.values.tolist())

print(list(curtidas_recebidas_df.columns))

print(curtidas_recebidas_total.values.tolist())

print(list(tabela.columns))