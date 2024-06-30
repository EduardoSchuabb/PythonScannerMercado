
from datetime import datetime
from dateutil.relativedelta import relativedelta

import pandas as pd
import yfinance as yf
import os


    
def obterEmpresasIBOV_csv():
    data_frame_csv = pd.read_csv('IBOVDia.csv', delimiter=';')
    #print(data_frame_csv['Codigo yfinance'])
    return data_frame_csv
        
def obterDadosAcoesYfinance():
    data_frame_acoes = obterEmpresasIBOV_csv()

    #print(codigo_acao.info)
    # Informações desejadas:
    # codigo_acao.info['website']
    # codigo_acao.info['sector']
    # codigo_acao.info['longBusinessSummary']
    # codigo_acao.info['longName']
    
    dadosHistoricoCompletoIntervaloDiario(data_frame_acoes['Codigo yfinance'])
    obterHistoricoIntervaloUmaHora(data_frame_acoes['Codigo yfinance'])
    obterHistoricoIntervalo15Min(data_frame_acoes['Codigo yfinance'])
    obterHistoricoIntervalo5Min(data_frame_acoes['Codigo yfinance'])

    obterIndiceBovespa()

def obterIndiceBovespa():

    indice_bovespa_str = '^BVSP'

    verifiaDiretorioBase()
    verificaDiretorioIndice(indice_bovespa_str)
    criaArquivoCsvDiario(indice_bovespa_str)
    criaArquivoCsvUmaHora(indice_bovespa_str)
    criaArquivoCsv15Min(indice_bovespa_str)
    criaArquivoCsv5Min(indice_bovespa_str)

def modificaData(data):
    return data.strftime('%d/%m/%Y')

def modificaDataHora(data):
    return data.strftime('%d/%m/%Y %H:%M' )

def verifiaDiretorioBase():
    diretorio_base = 'dados_historicos'
    if not os.path.exists(diretorio_base):
        os.makedirs(diretorio_base)
    else:
        #print(f'O diretório "{diretorio_base}" já existe.')
        pass

def verificaDiretorioIndice(indice):
    diretorio_acao = 'dados_historicos/' + indice
    if not os.path.exists(diretorio_acao):
        os.makedirs(diretorio_acao)
    else:
        #print(f'O diretório "{diretorio_base}" já existe.')
        pass

def dadosHistoricoCompletoIntervaloDiario(codigosYfinance):

    verifiaDiretorioBase()

    for acao in codigosYfinance:
    #acao = codigosYfinance[0]
        verificaDiretorioIndice(acao)
        criaArquivoCsvDiario(acao)

def criaArquivoCsvDiario(acao):
    diretorio_arquivo = 'dados_historicos/' + acao + '/' + acao + '_diario.csv'
    if os.path.isfile(diretorio_arquivo):
        #print(f'O arquivo "{diretorio_arquivo}" existe. Adicionar linhas novas, se existirem...')
        atualizaCsvDiario(acao)
    else:
        ticker_acao = yf.Ticker(acao)
        historico = ticker_acao.history(period='max')
        historico.drop(columns=["Dividends", "Stock Splits"], inplace=True)
        historico.rename(columns={'Open': 'Abertura',
                                'High': 'Máxima',
                                'Low':'Mínima',
                                'Close':'Fechamento',}, inplace=True)
        historico['Data'] = historico.index.to_series().apply(modificaData)
        historico = historico.round({'Abertura': 2,'Máxima': 2,'Mínima': 2,'Fechamento': 2})
        historico = historico[['Data','Abertura','Máxima','Mínima','Fechamento', 'Volume']]
        historico = historico.reset_index(drop=True)

        historico.to_csv(diretorio_arquivo, encoding='utf-8', index=False)

def atualizaCsvDiario(acao):

    hoje = datetime.now()
    data_passada = hoje - relativedelta(days=21)
    ticker_acao = yf.Ticker(acao)
    historico = ticker_acao.history(start=data_passada, end=hoje, interval='1d')
    historico.drop(columns=["Dividends", "Stock Splits"], inplace=True)
    historico.rename(columns={'Open': 'Abertura',
                            'High': 'Máxima',
                            'Low':'Mínima',
                            'Close':'Fechamento',}, inplace=True)
    historico['Data'] = historico.index.to_series().apply(modificaData)
    historico = historico.round({'Abertura': 2,'Máxima': 2,'Mínima': 2,'Fechamento': 2})
    historico = historico[['Data','Abertura','Máxima','Mínima','Fechamento', 'Volume']]
    historico = historico.reset_index(drop=True)

    diretorio_arquivo = 'dados_historicos/' + acao + '/' + acao + '_diario.csv'
    df_csv = pd.read_csv(diretorio_arquivo)

    contem_valores = historico['Data'].isin(df_csv['Data'])
    indices_falsos = contem_valores[contem_valores == False].index
    linhas_novas = historico.loc[indices_falsos]

    if not linhas_novas.empty:
        linhas_novas.to_csv(diretorio_arquivo, mode='a', header=False, index=False)
    else:
        #print("dataframe a adicionar vazio.")
        pass

def obterHistoricoIntervaloUmaHora(codigosYfinance):
    verifiaDiretorioBase()

    for acao in codigosYfinance:
    #acao = codigosYfinance[0]
        verificaDiretorioIndice(acao)
        criaArquivoCsvUmaHora(acao)

def criaArquivoCsvUmaHora(acao):
    diretorio_arquivo = 'dados_historicos/' + acao + '/' + acao + '_UmaHora.csv'
    if os.path.isfile(diretorio_arquivo):
        #print(f'O arquivo "{diretorio_arquivo}" existe. Adicionar linhas novas, se existirem...')
        atualizaCsvUmaHora(acao)
    else:
        ticker_acao = yf.Ticker(acao)
        historico = ticker_acao.history(period='1y', interval='1h')
        historico.drop(columns=["Dividends", "Stock Splits"], inplace=True)
        historico.rename(columns={'Open': 'Abertura',
                                'High': 'Máxima',
                                'Low':'Mínima',
                                'Close':'Fechamento',}, inplace=True)
        historico['Data'] = historico.index.to_series().apply(modificaDataHora)
        historico = historico.round({'Abertura': 2,'Máxima': 2,'Mínima': 2,'Fechamento': 2})
        historico = historico[['Data','Abertura','Máxima','Mínima','Fechamento', 'Volume']]
        historico = historico.reset_index(drop=True)

        historico.to_csv(diretorio_arquivo, encoding='utf-8', index=False)

def atualizaCsvUmaHora(acao):

    hoje = datetime.now()
    data_passada = hoje - relativedelta(days=12)
    ticker_acao = yf.Ticker(acao)
    historico = ticker_acao.history(start=data_passada, end=hoje, interval='1h')
    historico.drop(columns=["Dividends", "Stock Splits"], inplace=True)
    historico.rename(columns={'Open': 'Abertura',
                            'High': 'Máxima',
                            'Low':'Mínima',
                            'Close':'Fechamento',}, inplace=True)
    historico['Data'] = historico.index.to_series().apply(modificaDataHora)
    historico = historico.round({'Abertura': 2,'Máxima': 2,'Mínima': 2,'Fechamento': 2})
    historico = historico[['Data','Abertura','Máxima','Mínima','Fechamento', 'Volume']]
    historico = historico.reset_index(drop=True)

    diretorio_arquivo = 'dados_historicos/' + acao + '/' + acao + '_UmaHora.csv'
    df_csv = pd.read_csv(diretorio_arquivo)

    contem_valores = historico['Data'].isin(df_csv['Data'])
    indices_falsos = contem_valores[contem_valores == False].index
    linhas_novas = historico.loc[indices_falsos]

    if not linhas_novas.empty:
        linhas_novas.to_csv(diretorio_arquivo, mode='a', header=False, index=False)
    else:
        #print("dataframe a adicionar vazio.")
        pass

def obterHistoricoIntervalo15Min(codigosYfinance):
    verifiaDiretorioBase()

    for acao in codigosYfinance:
    #acao = codigosYfinance[0]
        verificaDiretorioIndice(acao)
        criaArquivoCsv15Min(acao)

def criaArquivoCsv15Min(acao):
    diretorio_arquivo = 'dados_historicos/' + acao + '/' + acao + '_15min.csv'
    if os.path.isfile(diretorio_arquivo):
        #print(f'O arquivo "{diretorio_arquivo}" existe. Adicionar linhas novas, se existirem...')
        atualizaCsv15Min(acao)
    else:
        hoje = datetime.now()
        dois_meses_atras = hoje - relativedelta(days=59)
        ticker_acao = yf.Ticker(acao)
        historico = ticker_acao.history(interval='15m', start=dois_meses_atras, end=hoje)
        #print(historico.tail(30))
        historico.drop(columns=["Dividends", "Stock Splits"], inplace=True)
        historico.rename(columns={'Open': 'Abertura',
                                'High': 'Máxima',
                                'Low':'Mínima',
                                'Close':'Fechamento',}, inplace=True)
        historico['Data'] = historico.index.to_series().apply(modificaDataHora)
        historico = historico.round({'Abertura': 2,'Máxima': 2,'Mínima': 2,'Fechamento': 2})
        historico = historico[['Data','Abertura','Máxima','Mínima','Fechamento', 'Volume']]
        historico = historico.reset_index(drop=True)

        historico.to_csv(diretorio_arquivo, encoding='utf-8', index=False)

def atualizaCsv15Min(acao):
    hoje = datetime.now()
    data_passada = hoje - relativedelta(days=12)
    ticker_acao = yf.Ticker(acao)
    historico = ticker_acao.history(start=data_passada, end=hoje, interval='15m')
    historico.drop(columns=["Dividends", "Stock Splits"], inplace=True)
    historico.rename(columns={'Open': 'Abertura',
                            'High': 'Máxima',
                            'Low':'Mínima',
                            'Close':'Fechamento',}, inplace=True)
    historico['Data'] = historico.index.to_series().apply(modificaDataHora)
    historico = historico.round({'Abertura': 2,'Máxima': 2,'Mínima': 2,'Fechamento': 2})
    historico = historico[['Data','Abertura','Máxima','Mínima','Fechamento', 'Volume']]
    historico = historico.reset_index(drop=True)

    diretorio_arquivo = 'dados_historicos/' + acao + '/' + acao + '_15min.csv'
    df_csv = pd.read_csv(diretorio_arquivo)

    contem_valores = historico['Data'].isin(df_csv['Data'])
    indices_falsos = contem_valores[contem_valores == False].index
    linhas_novas = historico.loc[indices_falsos]

    if not linhas_novas.empty:
        linhas_novas.to_csv(diretorio_arquivo, mode='a', header=False, index=False)
    else:
        #print("dataframe a adicionar vazio.")
        pass

def obterHistoricoIntervalo5Min(codigosYfinance):
    verifiaDiretorioBase()

    for acao in codigosYfinance:
    #acao = codigosYfinance[0]
        verificaDiretorioIndice(acao)
        criaArquivoCsv5Min(acao)

def criaArquivoCsv5Min(acao):
    diretorio_arquivo = 'dados_historicos/' + acao + '/' + acao + '_5min.csv'
    if os.path.isfile(diretorio_arquivo):
        #print(f'O arquivo "{diretorio_arquivo}" existe. Adicionar linhas novas, se existirem...')
        atualizaCsv5Min(acao)
    else:
        hoje = datetime.now()
        dois_meses_atras = hoje - relativedelta(days=59)
        ticker_acao = yf.Ticker(acao)
        historico = ticker_acao.history(interval='5m', start=dois_meses_atras, end=hoje)
        historico.drop(columns=["Dividends", "Stock Splits"], inplace=True)
        historico.rename(columns={'Open': 'Abertura',
                                'High': 'Máxima',
                                'Low':'Mínima',
                                'Close':'Fechamento',}, inplace=True)
        historico['Data'] = historico.index.to_series().apply(modificaDataHora)
        historico = historico.round({'Abertura': 2,'Máxima': 2,'Mínima': 2,'Fechamento': 2})
        historico = historico[['Data','Abertura','Máxima','Mínima','Fechamento', 'Volume']]
        historico = historico.reset_index(drop=True)

        historico.to_csv(diretorio_arquivo, encoding='utf-8', index=False)

def atualizaCsv5Min(acao):

    hoje = datetime.now()
    data_passada = hoje - relativedelta(days=12)
    ticker_acao = yf.Ticker(acao)
    historico = ticker_acao.history(start=data_passada, end=hoje, interval='5m')
    historico.drop(columns=["Dividends", "Stock Splits"], inplace=True)
    historico.rename(columns={'Open': 'Abertura',
                            'High': 'Máxima',
                            'Low':'Mínima',
                            'Close':'Fechamento',}, inplace=True)
    historico['Data'] = historico.index.to_series().apply(modificaDataHora)
    historico = historico.round({'Abertura': 2,'Máxima': 2,'Mínima': 2,'Fechamento': 2})
    historico = historico[['Data','Abertura','Máxima','Mínima','Fechamento', 'Volume']]
    historico = historico.reset_index(drop=True)

    diretorio_arquivo = 'dados_historicos/' + acao + '/' + acao + '_5min.csv'
    df_csv = pd.read_csv(diretorio_arquivo)

    contem_valores = historico['Data'].isin(df_csv['Data'])
    indices_falsos = contem_valores[contem_valores == False].index
    linhas_novas = historico.loc[indices_falsos]


    if not linhas_novas.empty:
        linhas_novas.to_csv(diretorio_arquivo, mode='a', header=False, index=False)
    else:
        #print("dataframe a adicionar vazio.")
        pass



