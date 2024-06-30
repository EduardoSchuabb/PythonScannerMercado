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
        
        - Buscar apenas a atualização dos dados após a criação dos arquivos em csv.

            - Dica: Verificar a data e hora da última linha do arquivo csv com os novos dados que serão obtidos da consulta de atualização.

    - O que fazer:

        - Buscar os dados das empresas e salvar em um csv.

            - Método para consulta já escrito, porém tem que alinhar os dados que serão salvos.

        - Criar um módulo (pacote) reponsável por análise estatística.

            - Analisar se esse módulo de estatística permanecerá nesse projeto ou migrará para o projeto de web service. De inicio deixar nesse projeto.

            - Quais análises estatísticas/financeiras serão realizadas?

                - Média, mediana, quartil, variância, desvio-padrão, covariância, correlação e outras (obter mais ideias).

                - Comparação dos valores com tempo gráficos diferentes. Ex.: Comparar valor de fechamento atual com históricos anteriores.

                - Fazer análise dos meses de pagamento de dividendos.

                - Verificar criação dos gráficos a partir dos dados obtidos de cada ação.

        - Obter os valores do IBOVESPA e salvar em csv (utilizar os mesmos tempos gráficos das ações).

        - Criar um esquema de log.
        
            - Log para informar a situação de atualização dos dados (arquivos csv).
            - Log deve conter informação da data e hora (analisar possíveis outras informações).
        
        - Otimizar o Código (Não é prioridade nesse momento, mas deverá ser feito).