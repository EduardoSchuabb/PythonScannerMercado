import requests



'''
    Método requestBrapiFiiHistorico
    Parâmetros: Por motivos de conta free, apenas esses parâmetros são permitidos
        - codigo_fii:
        - tempo: 1d, 5d, 1mo, 3mo
        - intervalo: 1d
    Função: Realiza a obtenção do histórico de valores de uma FII na API https://brapi.dev/dashboard
    Retorno: Um Json com o histório dos dados no padrão: Data, Abertura, Max, Min, Fechamento, Volume e fechamento de ajuste.
'''
def requestBrapiFiiHistorico(codigo_fii, tempo='3mo', intervalo='1d'):
    #salvar token de forma mais segura, apenas para teste.
    token = obterCodigoToken()
    url = f'https://brapi.dev/api/quote/{codigo_fii}?token={token}&range={tempo}&interval={intervalo}'
    resposta = requests.get(url)
    if resposta.ok:
        dados = resposta.json()
        dados = dados['results'][0]['historicalDataPrice']
    else:
        dados = ''

    return dados

'''
    Método obterCodigoToken
    Parâmetros: nenhum
    Função: Realiza a leitura de um arquivo com do token para acessar a API da brapi.
    Retorno: String que contém um token.

'''
def obterCodigoToken():
    with open ('buscador/code.txt', 'r', encoding='utf-8') as file:
        token = file.read()
    return token




