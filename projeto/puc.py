"""
    Sistema de análise de dados meteorológicos a partir de um arquivo CSV.

    O programa lê um arquivo contendo registros diários de clima
    (data, precipitação, temperaturas, insolação, umidade e vento).

    A partir desses dados, o sistema permite:

    - Visualizar informações meteorológicas filtradas por mês e ano
    - Identificar o mês mais chuvoso do período
    - Calcular a média da temperatura mínima de um mês específico em cada ano
    - Gerar um gráfico com as médias da temperatura mínima por ano
    - Calcular a média geral da temperatura mínima de um mês ao longo dos anos
"""

from datetime import datetime
import matplotlib.pyplot as plt

"""
    Organiza os dados de um arquivo CSV em uma lista de dicionários.

    Cada linha do arquivo é convertida em um dicionário, onde as chaves
    correspondem aos nomes das colunas do cabeçalho.

    Parâmetros:
    arquivo (str): nome do arquivo CSV informado pelo usuário.

    Retorno:
    list: lista contendo dicionários com os dados do arquivo.
"""
def ler_arquivo_csv(arquivo):
    with open(f"{arquivo}.csv", "r", encoding="utf-8") as arq:

        dados = []

        cabecalho = arq.readline().strip().split(",")

        for linha in arq:

            if linha.strip() != "":

                data, precipitacao, temperatura_max, temperatura_min, hora_sol, temperatura_media, umidade_ar, velocidade_vento = linha.strip().split(",")

                dados.append(
                    {
                        cabecalho[0]: data,
                        cabecalho[1]: precipitacao,
                        cabecalho[2]: temperatura_max,
                        cabecalho[3]: temperatura_min,
                        cabecalho[4]: hora_sol,
                        cabecalho[5]: temperatura_media,
                        cabecalho[6]: umidade_ar,
                        cabecalho[7]: velocidade_vento
                    }
                )

        return dados


"""

    Visualiza informações meteorológicas do CSV filtrando
    por intervalo de meses e anos.

    Parâmetros:
    mes_inicio (int): mês inicial do intervalo (1-12)
    ano_inicio (int): ano inicial do intervalo
    mes_fim (int): mês final do intervalo (1-12)
    ano_fim (int): ano final do intervalo
    opcao (int): tipo de dado que será exibido
        1 - todos os dados
        2 - apenas precipitação
        3 - apenas temperaturas
        4 - apenas umidade e vento
    dados (list): lista de dicionários contendo os dados do arquivo CSV

    Retorno:
    None
    A função apenas exibe os dados na tela.

"""
def visualizar_dados(mes_inicio,ano_inicio,mes_fim,ano_fim,opcao,dados):

    inicio = datetime(ano_inicio,mes_inicio,1)

    if mes_fim == 12:
        fim = datetime(ano_fim + 1, 1, 1)
    else:
        fim = datetime(ano_fim, mes_fim + 1, 1)

    for linha in dados:

        atual = datetime.strptime(linha["data"], "%d/%m/%Y")

        if opcao == 1:
            
            if inicio <= atual < fim:

                print("------------------------------------------------------------------------------------")
                print("DATA | PRECIP | TEMP MAX | TEMP MIN | HORA INSOLAÇÃO | TEMP MÉDIA | UMIDADE | VENTO")
                print("-------------------------------------------------------------------------------------")

                print(f"Data: {linha['data']}\n"
                      f"Precipitação: {linha['precip']} m2\n"
                      f"Temperatura Máxima: {linha['maxima']} graus\n"
                      f"Temperatura Mínima: {linha['minima']} graus\n"
                      f"Horas de Insolação: {linha['horas_insol']}\n"
                      f"Temperatura Média: {linha['temp_media']} graus\n"
                      f"Umidade relativa do ar: {linha['um_relativa']}%\n"
                      f"Velocidade do vento: {linha['vel_vento']} m/s\n"
                      )

        elif opcao == 2:

            if inicio <= atual < fim:

                print("---------------")
                print("DATA | PRECIP")
                print("---------------")

                print(f"Data: {linha['data']}\n"
                      f"Precipitação: {linha['precip']} m2\n")

        elif opcao == 3:

            if inicio <= atual < fim:
                
                print("-----------------------------------------")
                print("DATA | TEMP MAX | TEMP MIN | TEMP MÉDIA")
                print("-----------------------------------------")

                print(f"Data:{linha['data']}\n"
                      f"Temperatura Máxima: {linha['maxima']} graus\n"
                      f"Temperatura Mínima: {linha['minima']} graus\n"
                      f"Temperatura Média: {linha['temp_media']} graus\n")

        elif opcao == 4:

            
            if inicio <= atual < fim:

                print("------------------------")
                print("DATA | UMIDADE | VENTO")
                print("------------------------")

                print(f"Data:{linha['data']}\n"
                      f"Umidade relativa do ar: {linha['um_relativa']}%\n"
                      f"Velocidade do vento: {linha['vel_vento']} m/s\n"
                      )


"""

    Identifica o mês/ano com maior volume total de precipitação.

    A função percorre todos os registros do arquivo e soma
    a precipitação de cada mês e ano. Ao final, identifica
    qual mês teve o maior valor acumulado.

    Parâmetros:
    dados (list): lista de dicionários contendo os dados meteorológicos.

    Retorno:
    tuple:
        mes_chuvoso (str): mês e ano com maior precipitação
        precipitacao_maior (float): volume total de chuva registrado

"""
def mes_mais_chuvoso(dados):

    meses_precipitacao = {}

    for linha in dados:

        data = datetime.strptime(linha["data"], "%d/%m/%Y")

        mes_ano = f"{data.month}/{data.year}"

        precipitacao = float(linha["precip"])

        if mes_ano in meses_precipitacao:

            meses_precipitacao[mes_ano] += precipitacao

        else:

            meses_precipitacao[mes_ano] = precipitacao

    mes_chuvoso = max(meses_precipitacao, key=meses_precipitacao.get)

    precipitacao_maior = meses_precipitacao[mes_chuvoso]

    return mes_chuvoso, precipitacao_maior


"""

    Calcula a média da temperatura mínima de um mês específico
    entre os anos de 2006 e 2016.

    A função percorre os dados do arquivo e, para cada ano,
    soma as temperaturas mínimas do mês informado e calcula
    a média correspondente.

    Parâmetros:
    dados (list): lista de dicionários contendo os dados meteorológicos
    mes (int): mês desejado para análise (1-12)

    Retorno:
    dict:
        chave (int): ano
        valor (float): média da temperatura mínima naquele ano

"""
def temperatura_media_mes(dados, mes):

    meses_temperatura_minima = {}

    for linha in dados:

        data = datetime.strptime(linha["data"], "%d/%m/%Y")

        temp_minima = float(linha["minima"])

        if data.month == mes and 2006 <= data.year <= 2016:

            if data.year in meses_temperatura_minima:

                meses_temperatura_minima[data.year][0] += temp_minima
                meses_temperatura_minima[data.year][1] += 1

            else:

                meses_temperatura_minima[data.year] = [temp_minima, 1]

    medias = {}

    for ano, valores in meses_temperatura_minima.items():

        soma, dias = valores

        medias[ano] = soma / dias

    return medias


"""

    Gera um gráfico de barras com as médias da temperatura
    mínima de um determinado mês entre 2006 e 2016.

    Cada barra representa um ano e sua respectiva média
    de temperatura mínima.

    Parâmetros:
    medias (dict): dicionário contendo as médias calculadas
        chave (int): ano
        valor (float): média da temperatura mínima

    Retorno:
    None
    A função apenas exibe o gráfico na tela.

"""
def grafico_temperatura(medias):

    anos = list(medias.keys())

    temperaturas = list(medias.values())

    plt.figure(figsize=(10,5))

    plt.bar(anos, temperaturas)

    plt.title("Média da Temperatura Mínima por Ano (2006-2016)")

    plt.xlabel("Ano")

    plt.ylabel("Temperatura Média Mínima (°C)")

    plt.xticks(rotation=45)

    plt.show()


"""
    Calcula e exibe a média geral da temperatura mínima
    de um determinado mês considerando os anos de 2006 a 2016.

    A função utiliza o dicionário de médias calculado
    pela função temperatura_media_mes e calcula a média
    geral entre todos os anos disponíveis.

    Parâmetros:
    dados (list): lista de dicionários contendo os dados meteorológicos
    mes (int): mês escolhido para análise (1-12)

    Retorno:
    None
    A função apenas imprime a média geral na tela.
"""
def exibir_meses_temp_minima(dados, mes):

    minimo_temp = temperatura_media_mes(dados, mes)

    somatorio = 0

    anos = 0

    for temp in minimo_temp.values():

        somatorio += temp

        anos += 1

    media = somatorio / anos

    print(f"Média geral da temperatura mínima: {media:.2f}°C")


dados = ler_arquivo_csv("arquivo/arquivo")

print("\nVISUALIZAÇÃO DE DADOS")

mes_inicio = int(input("Digite o mês inicial (1-12): "))
while mes_inicio < 1 or mes_inicio > 12:
    mes_inicio = int(input("Mês inválido. Digite novamente (1-12): "))

ano_inicio = int(input("Digite o ano inicial (1961-2016): "))
while ano_inicio < 1961 or ano_inicio > 2016:
    ano_inicio = int(input("Ano inválido. Digite novamente (1961-2016): "))

mes_fim = int(input("Digite o mês final (1-12): "))
while mes_fim < 1 or mes_fim > 12:
    mes_fim = int(input("Mês inválido. Digite novamente (1-12): "))

ano_fim = int(input("Digite o ano final (1961-2016): "))
while ano_fim < 1961 or ano_fim > 2016:
    ano_fim = int(input("Ano inválido. Digite novamente (1961-2016): "))

while (ano_fim < ano_inicio) or (ano_fim == ano_inicio and mes_fim < mes_inicio):

    print("Período inválido. A data final deve ser maior que a inicial.")

    mes_inicio = int(input("Digite o mês inicial (1-12): "))
    while mes_inicio < 1 or mes_inicio > 12:
        mes_inicio = int(input("Mês inválido. Digite novamente (1-12): "))

    ano_inicio = int(input("Digite o ano inicial: "))

    mes_fim = int(input("Digite o mês final (1-12): "))
    while mes_fim < 1 or mes_fim > 12:
        mes_fim = int(input("Mês inválido. Digite novamente (1-12): "))

    ano_fim = int(input("Digite o ano final: "))

print("\nEscolha o tipo de visualização:")
print("1 - Todos os dados")
print("2 - Apenas precipitação")
print("3 - Apenas temperaturas")
print("4 - Apenas umidade e vento")

opcao = int(input("Digite a opção desejada: "))

while opcao not in [1,2,3,4]:
    opcao = int(input("Opção inválida. Digite novamente (1-4): "))

visualizar_dados(mes_inicio, ano_inicio, mes_fim, ano_fim, opcao, dados)

mes = int(input("\nDigite o mês para análise da temperatura mínima (1-12): "))

while mes < 1 or mes > 12:
    mes = int(input("Mês inválido. Digite novamente (1-12): "))

medias = temperatura_media_mes(dados, mes)

grafico_temperatura(medias)

exibir_meses_temp_minima(dados, mes)

mes_chuvoso, chuva = mes_mais_chuvoso(dados)

print(f"\nMês mais chuvoso: {mes_chuvoso}")

print(f"Precipitação total: {chuva:.2f} mm")