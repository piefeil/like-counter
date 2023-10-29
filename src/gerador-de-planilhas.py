import pandas as pd
import random
from datetime import datetime, timedelta



# Lista de nomes
nomes = ['Lucas Silva', 'Pablo Laud', 'Carol Mendonça', 'Vitor Cruz', 'Mariana Andrade', 
         'Breno De Paula', 'Iara Rodrigues', 'Dairus Martins', 'Marcela Braga', 'Pietro Kainã', 
         'Antônio Lucas', 'Rosilene Santos', 'Lauren Iensse', 'Ariane Miranda', 'Aline Martins', 'Rafael Santos']



# Probabilidades dos nomes
probabilidades = [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]  # As probabilidades podem ser ajustadas conforme necessário



# Mensagens de elogio das curtidas
mensagens = ["Parabéns pela pauta na reunião hoje", 
             "Curtida por todas as reuniões das diretorias que você participa! Manda muito na sua diretoria", 
             "Like por você se empenhar tanto na empresa", 
             "Você é um exemplo a ser seguido", 
             "Seu comprometimento é inspirador", 
             "Curtida pela visita técnica feita essa semana", 
             "Mandou bem participando da reunião com o cliente", ]



# Função para gerar nomes com base em probabilidades
def gerar_nomes_com_frequencia(nomes, probabilidades, tamanho):
    return random.choices(nomes, weights=probabilidades, k=tamanho)



# Função para obter datas aleatórias dentro de um intervalo específico
def gerar_datas_aleatorias(inicio, fim, quantidade, datas_existente=None):
    formato = '%d/%m/%Y'
    data_inicio = datetime.strptime(inicio, formato)
    data_fim = datetime.strptime(fim, formato)
    delta = data_fim - data_inicio


    # Bloco para possibilitar a inserção de datas repetidas
    if datas_existente is None:
        datas_existente = []

    datas_aleatorias = []
    for _ in range(quantidade):
        if len(datas_existente) > 0 and len(datas_existente) <= quantidade:
            data = random.choice(datas_existente)
            datas_aleatorias.append(data)
        else:
            data_aleatoria = data_inicio + timedelta(days=random.randint(0, delta.days))
            datas_aleatorias.append(data_aleatoria)

    return [data.strftime(formato) for data in datas_aleatorias]


# Lógica para garantir nomes diferentes nas colunas de envio e recebimento
def obter_nomes_recebendo(nomes_enviando, nomes):
    nomes_restantes = [nome for nome in nomes if nome not in nomes_enviando]
    if len(nomes_restantes) < 2000:
        nomes_restantes = nomes.copy()
        random.shuffle(nomes_restantes)  # Reorganizar aleatoriamente a lista de nomes

    return [random.choice(nomes_restantes) for _ in range(2000)]



# Gerar dados
nomes_enviando = gerar_nomes_com_frequencia(nomes, probabilidades, 2000)
nomes_recebendo = obter_nomes_recebendo(nomes_enviando, nomes)
datas_criacao = gerar_datas_aleatorias('01/01/2023', '31/12/2023', 2000)



# Criar o DataFrame
data = {'Quem está enviando a curtida?': nomes_enviando,
        'Para quem gostaria de enviar a curtida?': nomes_recebendo,
        'Deixe seu recado!': [random.choice(mensagens) for _ in range(2000)],
        'Criado em': datas_criacao}



# Exporta o arquivo .xlsx
df = pd.DataFrame(data)
df.to_excel('curtidas.xlsx', index=False)
