import os
import pandas as pd

PATH_BASICO_FIIS = 'arquivos/FIIs'
PATH_FILE_LISTA_FIIS = 'FIIs_analise.csv'


def criaDiretorioFIIs():
    os.makedirs(PATH_BASICO_FIIS, exist_ok=True)


def obterListaFIIs():

    lista_codigos_fiis = []

    if os.path.exists(PATH_BASICO_FIIS + '/' + PATH_FILE_LISTA_FIIS):
        data_frame =  pd.read_csv(PATH_BASICO_FIIS + '/' + PATH_FILE_LISTA_FIIS)
        for index, row in data_frame.iterrows():
            codigo_fii = row['Código']
            #print(f'Código: {codigo_fii}')
            lista_codigos_fiis.append(codigo_fii)
    else:
        print('Arquivo não encontrado.')

    return lista_codigos_fiis
