import collections
import pandas as pd

# Bloco responsável pela leitura da tabela exportada do Excel
tabela = pd.read_excel("curtidas.xlsx")
tabela_df = pd.DataFrame(tabela)


def tabela_somatorio(tabela):
    curtidas_enviadas_total = tabela['Quem está enviando a curtida?'].value_counts()
    curtidas_enviadas_df = pd.DataFrame(curtidas_enviadas_total)
    edf = curtidas_enviadas_df.rename(columns={'Quem está enviando a curtida?': 'Nome'})
    print(curtidas_enviadas_df)

    curtidas_recebidas_total = tabela['Para quem gostaria de enviar a curtida?'].value_counts()
    curtidas_recebidas_df = pd.DataFrame(curtidas_recebidas_total)
    rdf = curtidas_recebidas_df.rename(columns={'Para quem gostaria de enviar a curtida?': 'Nome'})
    print(curtidas_recebidas_df)

    print(edf.columns)
    print(rdf.columns)

    tabela_curtidas = pd.concat([edf, rdf])

    print (tabela_curtidas)

print(tabela_somatorio(tabela))    

# Preciso importar o código aqui para fazer os testes