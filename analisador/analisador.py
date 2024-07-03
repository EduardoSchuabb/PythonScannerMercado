#
# Pacote responsavel pela analise dos dados.
# A ideia é: Fazer metodos para analise estatistica e futuramente uma IA.
import pandas as pd

#
#
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

    df_estatistica_diario = pd.DataFrame()
    df_estatistica_1H = pd.DataFrame()
    df_estatistica_15min = pd.DataFrame()
    df_estatistica_5min = pd.DataFrame()

    PATH_teste_diario = 'dados_historicos/' + codigo + '/' + codigo + '_diario.csv'
    PATH_teste_1H = 'dados_historicos/' + codigo + '/' + codigo + '_UmaHora.csv'
    PATH_teste_15min = 'dados_historicos/' + codigo + '/' + codigo + '_15min.csv'
    PATH_teste_5min = 'dados_historicos/' + codigo + '/' + codigo + '_5min.csv'

    df_acao = pd.read_csv(PATH_teste_diario)
  
    df_estatistica_diario.insert(0, '150 Periodos', df_acao['Fechamento'].tail(150).describe())
    df_estatistica_diario.insert(1, '75 Periodos', df_acao['Fechamento'].tail(75).describe())
    df_estatistica_diario.insert(2, '21 Periodos', df_acao['Fechamento'].tail(21).describe())
    df_estatistica_diario.insert(3, '7 Periodos', df_acao['Fechamento'].tail(7).describe())
    df_estatistica_diario = df_estatistica_diario.round(2)
    print('-----------------------------------------------------')
    print('Diario')
    print('-----------------------------------------------------')

    print(df_estatistica_diario)

    df_acao = pd.read_csv(PATH_teste_1H)
    
    df_estatistica_1H.insert(0, '150 Periodos', df_acao['Fechamento'].tail(150).describe())
    df_estatistica_1H.insert(1, '75 Periodos', df_acao['Fechamento'].tail(75).describe())
    df_estatistica_1H.insert(2, '21 Periodos', df_acao['Fechamento'].tail(21).describe())
    df_estatistica_1H.insert(3, '7 Periodos', df_acao['Fechamento'].tail(7).describe())
    df_estatistica_1H = df_estatistica_1H.round(2)
    print('-----------------------------------------------------')
    print('1 Hora')
    print('-----------------------------------------------------')
    print(df_estatistica_1H)

    df_acao = pd.read_csv(PATH_teste_15min)
    
    df_estatistica_15min.insert(0, '150 Periodos', df_acao['Fechamento'].tail(150).describe())
    df_estatistica_15min.insert(1, '75 Periodos', df_acao['Fechamento'].tail(75).describe())
    df_estatistica_15min.insert(2, '21 Periodos', df_acao['Fechamento'].tail(21).describe())
    df_estatistica_15min.insert(3, '7 Periodos', df_acao['Fechamento'].tail(7).describe())
    df_estatistica_15min = df_estatistica_15min.round(2)
    print('-----------------------------------------------------')
    print('15 min')
    print('-----------------------------------------------------')
    print(df_estatistica_15min)

    df_acao = pd.read_csv(PATH_teste_5min)
    
    df_estatistica_5min.insert(0, '150 Periodos', df_acao['Fechamento'].tail(150).describe())
    df_estatistica_5min.insert(1, '75 Periodos', df_acao['Fechamento'].tail(75).describe())
    df_estatistica_5min.insert(2, '21 Periodos', df_acao['Fechamento'].tail(21).describe())
    df_estatistica_5min.insert(3, '7 Periodos', df_acao['Fechamento'].tail(7).describe())
    df_estatistica_5min = df_estatistica_5min.round(2)
    print('-----------------------------------------------------')
    print('5 min')
    print('-----------------------------------------------------')
    print(df_estatistica_5min)

    # Salvar o dataframes - São 4 dataframes estatisticos por acao:
    # df_estatistica_diario
    # df_estatistica_1H
    # df_estatistica_15min
    # df_estatistica_5min
    #



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
def variacaoPorCandleFechamento():
    pass


#
# Fazer a analise da variação diária do volume de negócios da ação
# verificar qual é a média de variação do volume das ações entre os dias
#
def variacaoVolume():
    pass