import pandas as pd
from datetime import datetime

# Importa as bibliotecas necessárias do código
    # Pandas é usado para ler a tabela de dados
    # Datetime é usado para ler a coluna das datas em que as curtidas foram enviadas
    
    
    
# Bloco responsável pela leitura da tabela exportada do Excel
tabela = pd.read_excel("curtidas.xlsx")
tabela_df = pd.DataFrame(tabela)

NOME = input('\nDigite o nome (Todos para total): ')



# Valida as curtidas
    # Não deve haver nenhum campo em branco 
    # E não pode ter apenas um "." no recado
tabela_df = tabela_df.dropna()
tabela_df = tabela_df.drop(tabela_df[tabela_df['Deixe seu recado!'] == '.'].index)



# Retorna uma tabela de quantas curtidas cada pessoa enviou no total
def curtidas_enviadas_todos(tabela):
    
    curtidas_enviadas_total = tabela['Quem está enviando a curtida?'].value_counts()
    curtidas_enviadas_df = pd.DataFrame(curtidas_enviadas_total)
    curtidas_enviadas_df['XP'] = curtidas_enviadas_df['count'] * 50
    curtidas_enviadas_df.rename(columns={'count': 'Total'}, inplace=True)
    return curtidas_enviadas_df


# Retorna uma tabela de quantas curtidas cada pessoa recebeu no total
def curtidas_recebidas_todos(tabela):
    
    curtidas_recebidas_total = tabela['Para quem gostaria de enviar a curtida?'].value_counts()
    curtidas_recebidas_df = pd.DataFrame(curtidas_recebidas_total)
    curtidas_recebidas_df['XP'] = curtidas_recebidas_df['count'] * 50
    curtidas_recebidas_df.rename(columns={'count': 'Total'}, inplace=True)
    return curtidas_recebidas_df


# Retorna quantas curtidas uma pessoa enviou
def curtidas_enviadas_individual(tabela):
    
    curtidas_enviadas = tabela['Quem está enviando a curtida?']
    qtd_curtidas_enviadas = (curtidas_enviadas.loc[curtidas_enviadas == NOME].value_counts())
    qtd_curtidas_enviadas_int = int(qtd_curtidas_enviadas.iloc[0])
    return  qtd_curtidas_enviadas_int


# Retorna quantas curtidas uma pessoa recebeu
def curtidas_recebidas_individual(tabela):
    
    curtidas_recebidas = tabela['Para quem gostaria de enviar a curtida?']
    qtd_curtidas_recebidas = (curtidas_recebidas.loc[curtidas_recebidas == NOME].value_counts())
    qtd_curtidas_recebidas_int = int(qtd_curtidas_recebidas.iloc[0])
    return  qtd_curtidas_recebidas_int


# Retorna o somatório de quantas curtidas uma pessoa enviou e recebeu
def total_curtidas_individual(tabela):
    
    curtidas_enviadas = curtidas_enviadas_individual(tabela)
    curtidas_recebidas = curtidas_recebidas_individual(tabela)
    somatorio = curtidas_enviadas + curtidas_recebidas
    return somatorio


# Retorna quantos XP as curtidas geraram para pontuação da empresa
def total_xp_individual(tabela):
    
    somatorio = total_curtidas_individual(tabela)
    xp = somatorio * 50
    return xp