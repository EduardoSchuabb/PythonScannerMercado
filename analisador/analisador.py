#
# Pacote responsavel pela analise dos dados.
# A ideia é: Fazer metodos para analise estatistica e futuramente uma IA.
# 
#
#
import pandas as pd


def informacoesEstatisticaCSV():

    codigo = 'PETR4.SA'

    PATH_teste_diario = 'dados_historicos/' + codigo + '/' + codigo + '_diario.csv'
    PATH_teste_1H = 'dados_historicos/' + codigo + '/' + codigo + '_UmaHora.csv'
    PATH_teste_15min = 'dados_historicos/' + codigo + '/' + codigo + '_15min.csv'
    PATH_teste_5min = 'dados_historicos/' + codigo + '/' + codigo + '_5min.csv'

    df_acao = pd.read_csv(PATH_teste_diario)
    print('-----------------------------------------------------')
    print('Informacoes dos ultimos 90 dias.')
    print('-----------------------------------------------------')
    print(df_acao.tail(90))
    print('-----------------------------------------------------')
    print('Informacoes estatisticas dos ultimos 30 dias.')
    print('-----------------------------------------------------')
    print(df_acao.tail(30).describe())
    print('-----------------------------------------------------')
    print('Informacoes estatisticas dos ultimos 90 dias.')
    print('-----------------------------------------------------')
    print(df_acao.tail(90).describe())


