import pandas as pd

tabela = pd.read_excel("curtidas.xlsx")

tabela_enviado = tabela['Quem está enviando a curtida?']
tabela_recebido = tabela['Para quem gostaria de enviar a curtida?']


def somatorio_tabelas():


    nomes_enviado = []

    for nome in tabela_enviado:
        nomes_enviado.append(nome) # Adiciona todos os nomes (repetidos) em uma lista 



    nomes_unicos = set() # Armazena elementos únicos

    for nome in tabela_enviado:
        if nome not in nomes_unicos:
            nomes_unicos.add(nome) # Adiciona uma fez na lista todos os nomes que tem na tabela



    def contagem_nomes(nomes_enviado, nomes_unicos):
        nome_count_enviado = {nome: nomes_enviado.count(nome) for nome in nomes_unicos}
        return nome_count_enviado

    nome_count_enviado = contagem_nomes(nomes_enviado, nomes_unicos)

    for nome in nomes_unicos:
        if nome in nome_count_enviado:
            continue
  
        else:
            print(f"{nome} não está presente na contagem.") # Verifica se o nome está presente no dicionário




    nomes_recebido = []

    for nome in tabela_recebido:
        nomes_recebido.append(nome) # Adiciona todos os nomes (repetidos) em uma lista 



    nomes_unicos = set() # Armazena elementos únicos

    for nome in tabela_recebido:
        if nome not in nomes_unicos:
            nomes_unicos.add(nome) # Adiciona uma fez na lista todos os nomes que tem na tabela



    def contagem_nomes(nomes_recebido, nomes_unicos):
        nome_count_recebido = {nome: nomes_recebido.count(nome) for nome in nomes_unicos}
        return nome_count_recebido

    nome_count_recebido = contagem_nomes(nomes_recebido, nomes_unicos)

    for nome in nomes_unicos:
        if nome in nome_count_recebido:
            continue
        else:
            print(f"{nome} não está presente na contagem.")



######################################### Soma total de outro jeito ###########################################



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

    nome_count_enviado_ordenado = dict(sorted(nome_count_enviado.items(), key=lambda item: item[1], reverse=True))
    nome_count_recebido_ordenado = dict(sorted(nome_count_recebido.items(), key=lambda item: item[1], reverse=True))

    for nome, valor in nome_count_enviado_ordenado.items():
        print(f"{nome}: {valor}")

    print()

    for nome, valor in nome_count_recebido_ordenado.items():
        print(f"{nome}: {valor}")

    print()

    soma_total_ordenado = dict(sorted(soma_total.items(), key=lambda item: item[1], reverse=True))
    
    for nome, valor in soma_total_ordenado.items():
        print(f"{nome}: {valor}")


    
print(somatorio_tabelas())