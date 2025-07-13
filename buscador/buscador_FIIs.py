import requests

def requestBrapiFii(codigo_fii, tempo='1mo', intervalo='1d'):
    # Contra free apenas os seguintes valores:
    # tempo: 1d, 5d, 1mo, 3mo
    # intervalo: 1d
    

    #salvar token de forma mais segura, apenas para teste.
   token = '6KkGZ7xQ1YQ2wqw3xYJrd5'
   url = f'https://brapi.dev/api/quote/{codigo_fii}?token={token}&range={tempo}&interval={intervalo}'
   resposta = requests.get(url)
   data = resposta.json()
   print(data)