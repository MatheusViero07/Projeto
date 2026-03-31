"""
    Sistema que registra a temperatura de cada mês do ano.

    O programa solicita ao usuário a temperatura de cada mês
    e armazena essas informações em um dicionário.

    Após o cadastro, o sistema retorna:

    - Meses escaldantes (temperatura acima de 33°C)
    - Mês mais quente do ano
    - Mês menos quente do ano
    - Temperatura média anual

"""

"""

    Retorna um dicionário contendo apenas os meses
    com temperatura acima de 33°C.

    Parâmetros:
    dic (dict): dicionário com mês e temperatura

    Retorno:
    dict: meses escaldantes

"""
def meses_escaldantes(dic):
    return {mes: temp for mes, temp in dic.items() if temp > 33}
 
"""

    Retorna o mês que possui a maior temperatura registrada.

    Parâmetros:
    dic (dict): dicionário com os meses e suas temperaturas.

    Retorno:
    int: número do mês com a maior temperatura.

"""
def mais_escaldante(dic):
    return max(dic, key=dic.get)

"""

    Retorna o mês que possui a menor temperatura registrada.

    Parâmetros:
    dic (dict): dicionário com os meses e suas temperaturas.

    Retorno:
    int: número do mês com a menor temperatura.

"""
def menos_escaldante(dic):
    return min(dic, key=dic.get)

"""

    Calcula a temperatura média anual com base nas
    temperaturas registradas.

    Parâmetros:
    dic (dict): dicionário contendo as temperaturas dos meses.

    Retorno:
    float: valor da temperatura média anual.

"""
def media(dic):
    return sum(dic.values()) / len(dic)

"""

    Verifica se a temperatura informada pelo usuário
    está dentro do intervalo permitido.

    Parâmetros:
    valida (float): temperatura informada pelo usuário.

    Retorno:
    bool: True se a temperatura estiver entre -60 e 50,
        False caso contrário.

"""
def valida_temp(valida):
    return -60 <= valida <= 50

"""

    Valida o número do mês informado pelo usuário e verifica
    se o mês já foi cadastrado anteriormente.

    Parâmetros:
    valida (int): número do mês informado pelo usuário.
    meses (dict): dicionário contendo os meses já cadastrados.

    Retorno:
    bool: True se o mês for válido e ainda não estiver
        cadastrado, False caso contrário.

"""
def valida_mes(valida, meses):
    if not 1 <= valida <= 12:
        print("\nErro, apenas numeros entre 1 e 12")
        return False
    if valida in meses:
        print("\nErro, mês ja existente")
        return False
    return True

meses = {}
mes_escrito = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
i = 0

while len(meses) < 12:
    try:
        mes = int(input("\nO numero do mês: "))
        if not valida_mes(mes,meses):
            continue

        temperatura = float(input(f"\nDigite a temperatura do mês {mes}: "))
        if not valida_temp(temperatura):
            print("\nErro, apenas numero entre -60 e 50")
            continue
        
    except ValueError:
        print("\nErro apenas numeros")
        continue

    meses[mes] = temperatura

mes_quente = mais_escaldante(meses)
mes_menos_quente = menos_escaldante(meses)

print(f"\nQuantidade de meses escaldantes: {len(meses_escaldantes(meses))}")

print(f"\nMês mais escaldante do ano: {mes_escrito[mes_quente-1]}, Temperatura: {meses[mes_quente]} graus")

print(f"\nMês menos quente do ano: {mes_escrito[mes_menos_quente-1]}, Temperatura: {meses[mes_menos_quente]} graus")

print(f"\nTemperatura média máxima anual: {media(meses):.2f} graus")