import pandas as pd
from tabulate import tabulate
from datetime import datetime


while True:
    nome = input('\nDigite o nome (Todos para total): ')

    tabela = pd.read_excel("r01.xlsx")
    tabela_df = pd.DataFrame(tabela)

    tabela_df = tabela_df.dropna()
    tabela_df = tabela_df.drop(tabela_df[tabela_df['Deixe seu recado!'] == '.'].index)
    

    def curtidas_enviadasf(tabela):
        curtidas_enviadas = tabela['Quem está enviando a curtida?']
        qtd_curtidas_enviadas = (curtidas_enviadas.loc[curtidas_enviadas == nome].value_counts())
        qtd_curtidas_enviadas_int = int(qtd_curtidas_enviadas.iloc[0])
        print(nome, 'enviou', qtd_curtidas_enviadas_int, 'curtidas.')


    def curtidas_recebidasf(tabela):
        curtidas_recebidas = tabela['Para quem gostaria de enviar a curtida?']
        qtd_curtidas_recebidas = (curtidas_recebidas.loc[curtidas_recebidas == nome].value_counts())
        qtd_curtidas_recebidas_int = int(qtd_curtidas_recebidas.iloc[0])
        print(nome, 'recebeu', qtd_curtidas_recebidas_int, 'curtidas.')


    def total_de_curtidasf(tabela):
        curtidas_enviadas = tabela['Quem está enviando a curtida?']
        qtd_curtidas_enviadas = (curtidas_enviadas.loc[curtidas_enviadas == nome].value_counts())

        curtidas_recebidas = tabela['Para quem gostaria de enviar a curtida?']
        qtd_curtidas_recebidas = (curtidas_recebidas.loc[curtidas_recebidas == nome].value_counts())

        somatorio = qtd_curtidas_enviadas + qtd_curtidas_recebidas
        somatorio_int = int(somatorio.iloc[0])
        print(nome, 'possui', somatorio_int, 'curtidas no total.')


    def total_de_xpf(tabela):
        curtidas_enviadas = tabela['Quem está enviando a curtida?']
        qtd_curtidas_enviadas = (curtidas_enviadas.loc[curtidas_enviadas == nome].value_counts())

        curtidas_recebidas = tabela['Para quem gostaria de enviar a curtida?']
        qtd_curtidas_recebidas = (curtidas_recebidas.loc[curtidas_recebidas == nome].value_counts())

        somatorio = qtd_curtidas_enviadas + qtd_curtidas_recebidas
        somatorio_int = int(somatorio.iloc[0])
        xp = somatorio_int * 50
        print(nome, 'possui', xp, 'de Xp.')


    def curtidas_enviadas_totalf(tabela):
        # Exibe quantidade de curtidas enviadas de todos em ordem decrescente

        curtidas_enviadas_total = tabela['Quem está enviando a curtida?'].value_counts()

        curtidas_enviadas_df = pd.DataFrame(curtidas_enviadas_total)

        curtidas_enviadas_df['XP'] = curtidas_enviadas_df['count'] * 50

        curtidas_enviadas_df.rename(columns={'count': 'Total'}, inplace=True)

        curtidas_enviadas_table = tabulate(curtidas_enviadas_df, headers='keys', tablefmt='fancy_grid')
        print('\nCurtidas enviadas:')
        print()
        print(curtidas_enviadas_df)
        # print(curtidas_enviadas_table)


    def curtidas_recebidas_totalf(tabela):
        # Exibe quantidade de curtidas recebidas de todos em ordem decrescente
        curtidas_recebidas_total = tabela['Para quem gostaria de enviar a curtida?'].value_counts()

        curtidas_recebidas_df = pd.DataFrame(curtidas_recebidas_total)

        curtidas_recebidas_df['XP'] = curtidas_recebidas_df['count'] * 50

        curtidas_recebidas_df.rename(columns={'count': 'Total'}, inplace=True)

        curtidas_recebidas_table = tabulate(curtidas_recebidas_df, headers='keys', tablefmt='fancy_grid')
        print('\nCurtidas recebidas:')
        print()
        print(curtidas_recebidas_df)
        # print(curtidas_recebidas_table)

    def mostrar_resultados(tabela):
        if nome.lower() == 'todos':
            intervalo = input('Gostaria de definir um intervalo? (s/n): ')
            if intervalo == 's':
                data_inicial = input('Insira a data inicial:')
                data_final = input('Insira a data final:')
                intervalo_df = tabela.loc[(tabela['Criado em']>= data_inicial) & (tabela['Criado em'] <= data_final)]
                curtidas_recebidas_totalf(intervalo_df)
                curtidas_enviadas_totalf(intervalo_df)
            else:
                intervalo_df = tabela
                curtidas_recebidas_totalf(tabela)
                curtidas_enviadas_totalf(tabela)
        else:
            print('\nO que você gostaria de ver sobre', nome, '?')
            print('\n1 - Quantas curtidas', nome, 'enviou.')
            print('2 - Quantas curtidas', nome, 'recebeu.')
            print('3 - Total de curtidas de', nome)
            print('4 - Total de XP de', nome)

            escolha = int(input('\nInsira aqui o número: '))
            
            intervalo = input('Gostaria de definir um intervalo? (s/n): ')
            
            if intervalo == 's':    
                data_inicial = input('Insira a data inicial:')
                data_final = input('Insira a data final:')
                intervalo_df = tabela.loc[(tabela['Criado em']>= data_inicial) & (tabela['Criado em'] <= data_final)]
                tabela = intervalo_df
                
                if escolha == 1:
                    curtidas_enviadasf(intervalo_df)
                elif escolha == 2:
                    curtidas_recebidasf(intervalo_df)
                elif escolha == 3:
                    total_de_curtidasf(intervalo_df)
                elif escolha == 4:
                    total_de_xpf(intervalo_df)
                    
            else:
                intervalo_df = tabela
            
                if escolha == 1:
                    curtidas_enviadasf(tabela)
                elif escolha == 2:
                    curtidas_recebidasf(tabela)
                elif escolha == 3:
                    total_de_curtidasf(tabela)
                elif escolha == 4:
                    total_de_xpf(tabela)
    
    mostrar_resultados(tabela_df)
    
    while True: 
        resposta = input('Deseja saber mais sobre? (s/n): ')
        
        if resposta.lower() == "s":
            mostrar_resultados(tabela_df)
        else:
            break
        
    resposta = input("Deseja executar o programa novamente? (s/n): ")
    if resposta.lower() != "s":
        break
    
    
# Criar uma tabela que mostra curtidas enviadas e recebidas total e xp no geral
# Buscar uma forma de validar as mensagens
# Quantidade de curtidas que cada um enviou pra cada um 


# Mudei a chamada da função mostrar_resultados