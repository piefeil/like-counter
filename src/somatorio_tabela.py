import pandas as pd


def somatorio_tabelas():

    tabela = pd.read_excel("curtidas.xlsx")

    tabela = tabela.drop(tabela[tabela['Deixe seu recado!'] == '.'].index)
    tabela = tabela.dropna()

    tabela_enviado = tabela['Quem está enviando a curtida?']
    tabela_recebido = tabela['Para quem gostaria de enviar a curtida?']



    # Dicionário para armazenar as contagens combinadas de envio e recebimento para cada pessoa
    soma_total = {}

    # Iterar sobre os valores de envio e calcular a contagem
    for nome in tabela_enviado:
        if nome in soma_total:
            soma_total[nome] += 1
        else:
            soma_total[nome] = 1

    # Iterar sobre os valores de recebimento e adicionar à contagem existente
    for nome in tabela_recebido:
        if nome in soma_total:
            soma_total[nome] += 1
        else:
            soma_total[nome] = 1


    print()

    soma_total_ordenado = dict(sorted(soma_total.items(), key=lambda item: item[1], reverse=True))
    
    for nome, valor in soma_total_ordenado.items():
        print(f"{nome}: {valor}")
    

