import pandas as pd
from datetime import datetime

# Importa as bibliotecas necessárias do código
    # Pandas é usado para ler a tabela de dados
    # Datetime é usado para ler a coluna das datas em que as curtidas foram enviadas



# Loop 01
# Permite que o programa rode novamente após encerrar todos os processos
while True:
    
    
    
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



    #Função responsável por exibir os valores desejados
    def mostrar_resultados(tabela):
        
        
        # Condição 01
        # Verifica se o usuário quer obter uma tabela geral ou informações individuais
        if NOME.lower() == 'todos':
            
            
           
            # Verifica se o usuário gostaria de definir um intervalo de tempo
            intervalo = input('Gostaria de definir um intervalo? (S/N): ')
            
            # Condição 02
            if intervalo.lower() == 's':
                
                data_inicial = input('Insira a data inicial:')
                data_final = input('Insira a data final:')
                intervalo_df = tabela.loc[(tabela['Criado em']>= data_inicial) & (tabela['Criado em'] <= data_final)]


                curtidas_enviadas = curtidas_recebidas_todos(intervalo_df)
                print(curtidas_enviadas)


                curtidas_recebidas = curtidas_enviadas_todos(intervalo_df)
                print(curtidas_recebidas)
                
               
            else:
                
                intervalo_df = tabela


                curtidas_enviadas_df = curtidas_enviadas_todos(tabela)
                print('\nCurtidas enviadas:')
                print()
                print(curtidas_enviadas_df)


                print()


                curtidas_recebidas_df = curtidas_recebidas_todos(tabela)
                print('\nCurtidas recebidas:')
                print()
                print(curtidas_recebidas_df)
              
              
             
        else:
            
            print('\nO que você gostaria de ver sobre', NOME, '?')
            print('\n1 - Quantas curtidas', NOME, 'enviou.')
            print('2 - Quantas curtidas', NOME, 'recebeu.')
            print('3 - Total de curtidas de', NOME)
            print('4 - Total de XP de', NOME)

            escolha = int(input('\nInsira aqui o número: '))
            intervalo = input('Gostaria de definir um intervalo? (S/N): ')
            
            # Condição 03
            # Verifica se o usuário gostaria de definir um intervalo de tempo
            if intervalo.lower() == 's':   
                 
                data_inicial = input('Insira a data inicial:')
                data_final = input('Insira a data final:')
                intervalo_df = tabela.loc[(tabela['Criado em']>= data_inicial) & (tabela['Criado em'] <= data_final)]
                tabela = intervalo_df
                
            else:
                
                intervalo_df = tabela 

            # Condição 04
            # Verifica quais informações o usuário gostaria de saber sobre o indivíduo em específico
            if escolha == 1:
                
                curtidas_enviadas = curtidas_enviadas_individual(intervalo_df)
                print(NOME, 'enviou', curtidas_enviadas, 'curtidas.')
                
                
            elif escolha == 2:
                
                curtidas_recebidas = curtidas_recebidas_individual(intervalo_df)
                print(NOME, 'recebeu', curtidas_recebidas, 'curtidas.')
                
                
            elif escolha == 3:
                
                somatorio = total_curtidas_individual(intervalo_df)
                print(NOME, 'possui', somatorio, 'curtidas no total.')
                
                
            elif escolha == 4:
                
                xp = total_xp_individual(intervalo_df)
                print(NOME, 'possui', xp, 'de Xp.')   
    
    
    
    mostrar_resultados(tabela_df)
    
    
    
    # Loop 02
    # Permite que o usuário execute o programa novamente com nome definido anteriormente
    while True: 
        resposta = input('Deseja saber mais sobre? (S/N): ')
        if resposta.lower() == "s":
            mostrar_resultados(tabela_df)
        else:
            break



    # Encerra o loop 01
    # Bloco responsável por verificar se o usuário gostaria de executar novamente o código
    resposta = input("Deseja executar o programa novamente? (S/N): ")
    if resposta.lower() != "s":
        break