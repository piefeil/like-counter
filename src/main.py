import pandas as pd
import collections
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
        return  qtd_curtidas_enviadas_int

    def curtidas_recebidasf(tabela):
        curtidas_recebidas = tabela['Para quem gostaria de enviar a curtida?']
        qtd_curtidas_recebidas = (curtidas_recebidas.loc[curtidas_recebidas == nome].value_counts())
        qtd_curtidas_recebidas_int = int(qtd_curtidas_recebidas.iloc[0])
        return  qtd_curtidas_recebidas_int

    def total_de_curtidasf(tabela):
        curtidas_enviadas = curtidas_enviadasf(tabela)
        curtidas_recebidas =curtidas_recebidasf(tabela)
        somatorio = curtidas_enviadas + curtidas_recebidas
        return somatorio

    def total_de_xpf(tabela):
        curtidas_enviadas = curtidas_enviadasf(tabela)
        curtidas_recebidas =curtidas_recebidasf(tabela)
        somatorio = curtidas_enviadas + curtidas_recebidas
        somatorio_int = somatorio.iloc[0]
        xp = somatorio_int * 50
        return xp

    def curtidas_enviadas_totalf(tabela):
        # Exibe quantidade de curtidas enviadas de todos em ordem decrescente
        curtidas_enviadas_total = tabela['Quem está enviando a curtida?'].value_counts()
        curtidas_enviadas_df = pd.DataFrame(curtidas_enviadas_total)
        curtidas_enviadas_df['XP'] = curtidas_enviadas_df['count'] * 50
        curtidas_enviadas_df.rename(columns={'count': 'Total'}, inplace=True)
        return curtidas_enviadas_df


    def curtidas_recebidas_totalf(tabela):
        # Exibe quantidade de curtidas recebidas de todos em ordem decrescente
        curtidas_recebidas_total = tabela['Para quem gostaria de enviar a curtida?'].value_counts()
        curtidas_recebidas_df = pd.DataFrame(curtidas_recebidas_total)
        curtidas_recebidas_df['XP'] = curtidas_recebidas_df['count'] * 50
        curtidas_recebidas_df.rename(columns={'count': 'Total'}, inplace=True)
        return curtidas_recebidas_df

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

    def mostrar_resultados(tabela):
        if nome.lower() == 'todos':
            intervalo = input('Gostaria de definir um intervalo? (s/n): ')
            if intervalo == 's':
                data_inicial = input('Insira a data inicial:')
                data_final = input('Insira a data final:')
                intervalo_df = tabela.loc[(tabela['Criado em']>= data_inicial) & (tabela['Criado em'] <= data_final)]

                curtidas_enviadas = curtidas_recebidas_totalf(intervalo_df)
                print (curtidas_enviadas)

                curtidas_recebidas = curtidas_enviadas_totalf(intervalo_df)
                print(curtidas_recebidas)
                
            else:
                intervalo_df = tabela

                tabela_soma = tabela_somatorio(intervalo_df)
                print(tabela_soma)

                curtidas_enviadas_df = curtidas_enviadas_totalf(tabela)
                print('\nCurtidas enviadas:')
                print()
                print(curtidas_enviadas_df)

                print()

                curtidas_recebidas_df = curtidas_recebidas_totalf(tabela)
                print('\nCurtidas recebidas:')
                print()
                print(curtidas_recebidas_df)
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
            else:
                intervalo_df = tabela 

            if escolha == 1:
                curtidas_enviadas = curtidas_enviadasf(intervalo_df)
                print(nome, 'enviou', curtidas_enviadas, 'curtidas.')
            elif escolha == 2:
                curtidas_recebidas = curtidas_recebidasf(intervalo_df)
                print(nome, 'recebeu', curtidas_recebidas, 'curtidas.')
            elif escolha == 3:
                somatorio = total_de_curtidasf(intervalo_df)
                print(nome, 'possui', somatorio, 'curtidas no total.')
            elif escolha == 4:
                xp = total_de_xpf(intervalo_df)
                print(nome, 'possui', xp, 'de Xp.')   
    
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


