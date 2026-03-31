from datetime import datetime

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

def visualizar_dados(mes_inicio,ano_inicio,mes_fim,ano_fim,opcao,dados):
    inicio = datetime(ano_inicio,mes_inicio,1)
    fim = datetime(ano_fim,mes_fim+1,1)

    for linha in dados:
        atual = datetime.strptime(linha["data"], "%d/%m/%Y")

        if opcao == 1:
            if inicio <= atual < fim:
                print(f"Data: {linha['data']}\n"
                      f"Precipitação: {linha['precip']} m2\n"
                      f"Temperatura Máxima: {linha['maxima']} graus\n"
                      f"Temperatura Mínima: {linha['minima']} graus\n"
                      f"Horas de Insolação: {linha['horas_insol']}\n"
                      f"Temperatura Média: {linha['temp_media']} graus\n"
                      f"Umidade relativa do ar: {linha['um_relativa']}%\n"
                      f"Velocidade do vento: {linha['vel_vento']} m/s\n"
                      )
                
        if opcao == 2:
            if inicio <= atual < fim:
                print(f"Data: {linha['data']}\n"
                      f"Precipitação: {linha['precip']} m2\n")
        
        if opcao == 3:
            if inicio <= atual < fim:
                print(f"Data:{linha['data']}\n"
                      f"Temperatura Máxima: {linha['maxima']} graus\n"
                      f"Temperatura Mínima: {linha['minima']} graus\n"
                      f"Temperatura Média: {linha['temp_media']} graus\n")
                
        if opcao == 4:
            if inicio <= atual < fim:
                print(f"Data:{linha['data']}\n"
                      f"Umidade relativa do ar: {linha['um_relativa']}%\n"
                      f"Velocidade do vento: {linha['vel_vento']} m/s\n"
                      )
                      
                    



dados = ler_arquivo_csv("arquivo")   
visualizar_dados(1,2000,1,2000,4,dados)