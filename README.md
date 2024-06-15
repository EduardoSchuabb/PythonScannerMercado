# PythonScannerMercado
Projeto em python para fazer a busca de dados sobre mercado financeiro.

Ideia inicial:
    - Módulo buscador: Realiza a busca das informações utilizando a API do yahoo finance.
    - Atualmente:
        - Já busca as informações das empresas que possuem ações que compõe o índice Bovespa, porém ainda não salvo essas informações.
        - Já realiza a busca e salva em arquivos .csv as infformações sobre o histórico das ações. Os históricos são salvos da seguinte forma:
            - Um arquivo .csv na pasta dados_historicos/(codigo da ação da empresa). Exemplo: dados_historicos/VALE3.SA
            - Dentro de cada diretório são gerados 4 arquivos .csv. Os arquivos são separados por tempo gráffico de 5 min, 15 min, 1 hora e diário.
            - O cabeçalho do arquivo .csv é: Data,Abertura,Máxima,Mínima,Fechamento,Volume
            - Exemplo de uma linha do arquivo .csv é: 15/06/2023 11:00,68.64,68.99,68.6,68.7,3674600
            - Para o .csv diário, não existe a informação da hora no campo Data.
