#
# Pacote responsavel pela analise dos dados.
# A ideia é: Fazer metodos para analise estatistica e futuramente uma IA.
import pandas as pd


# Método para obter valores como média, quartis e outros...
# priorizar coluna de fechamento e obter relações entre os tempos gráficos.
# fazer comparações com o valor atual da acao (ultimo fechamento?).
#
# #
def informacoesEstatisticaCSVFechamento(codigos):

    #for codigo in codigosYfinance:
    codigo = 'PETR4.SA'
    criaDataframeEstatistico(codigo)
    


def criaDataframeEstatistico(codigo):

    PATH_csv = ['dados_historicos/' + codigo + '/' + codigo + '_diario.csv',
                'dados_historicos/' + codigo + '/' + codigo + '_UmaHora.csv',
                'dados_historicos/' + codigo + '/' + codigo + '_15min.csv',
                'dados_historicos/' + codigo + '/' + codigo + '_5min.csv']
    
    tempo_grafico = ['Diario', 'Uma hora', '15 min', '5 min']
    posicao = 0

    for path in PATH_csv:

        df_estatistica = pd.DataFrame()
        df_acao = pd.read_csv(path)
  
        df_estatistica.insert(0, '150 Periodos', df_acao['Fechamento'].tail(150).describe())
        df_estatistica.insert(1, '75 Periodos', df_acao['Fechamento'].tail(75).describe())
        df_estatistica.insert(2, '21 Periodos', df_acao['Fechamento'].tail(21).describe())
        df_estatistica.insert(3, '7 Periodos', df_acao['Fechamento'].tail(7).describe())
        df_estatistica = df_estatistica.round(2)
        print('--------------------------------------------------------------')
        print(f'Tempo: {tempo_grafico[posicao]}')
        print('--------------------------------------------------------------')
        
        print(df_estatistica)
        posicao +=1



#
# Método para fazer a correlação das ações com o indice bovespa.
# plotar em um gráfico de inicio para análise visual.
# 
def correlacoesCSVcomIBOVESPA():
    pass


#
#
# Fazer a analise da variação diária da ação.
# Verificar qual é a média de variação das ações entre os dias
# verificar quais foram os dias com maiores variações.
#
#
def variacaoPorCandleFechamento(codigos):
    
    #for codigo in codigosYfinance:
    codigo = 'PETR4.SA'
    analiseResultadoPorCandle(codigo)



def analiseResultadoPorCandle(codigo):

    PATH_csv = ['dados_historicos/' + codigo + '/' + codigo + '_diario.csv',
                'dados_historicos/' + codigo + '/' + codigo + '_UmaHora.csv',
                'dados_historicos/' + codigo + '/' + codigo + '_15min.csv',
                'dados_historicos/' + codigo + '/' + codigo + '_5min.csv']
    
    tempo_grafico = ['Diario', 'Uma hora', '15 min', '5 min']
    posicao = 0

    for path in PATH_csv:

        df_acao = pd.read_csv(path)

        # Essa valor de 200 pode variar. Por enquanto deixar assim, mas analisar a quantidade de candle que serão utilizados.
        df_acao = df_acao.tail(100)
        df_acao = df_acao.reset_index()

        cont_candle_tendencia = 1
        resultado_anterior = 0
        cont_candle_positivo = 0
        cont_candle_negativo = 0
        string_result = ""

        print('--------------------------------------------------------------')
        print(f'Tempo: {tempo_grafico[posicao]}')
        print('--------------------------------------------------------------')

        for index, linha in df_acao.iterrows():
            if index > 0:
                pos_ant = index - 1
            else:
                pos_ant = index
        
            resultado = round(linha['Fechamento'] - df_acao.loc[pos_ant]['Fechamento'], 2)
            string_result = " ---"
            if(resultado > 0):
                cont_candle_positivo +=1
                string_result = "POS"
            if(resultado < 0):
                cont_candle_negativo +=1
                string_result = "NEG"

            if(resultado*resultado_anterior <= 0):
                cont_candle_tendencia = 1
            else:
                cont_candle_tendencia+=1

            resultado_anterior = resultado
            print(f"Índice: {index}, Data: {linha['Data']}, Fechamento: {linha['Fechamento']}, Resultado: {resultado}, Contagem: {cont_candle_tendencia} - {string_result}")

        print("--------------------------------------------------------------------------------------------")
        print(f"Candles positivos: {cont_candle_positivo}")
        print(f"Candles negativos: {cont_candle_negativo}")

        posicao += 1


#
# Fazer a analise da variação diária do volume de negócios da ação
# verificar qual é a média de variação do volume das ações entre os dias
#
def variacaoVolume():
    pass