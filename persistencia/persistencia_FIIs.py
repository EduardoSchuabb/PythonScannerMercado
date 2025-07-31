import os
import pandas as pd

PATH_BASICO_FIIS = 'arquivos/FIIs'
PATH_FILE_LISTA_FIIS = 'FIIs_analise.csv'

'''
    criaDiretorioFIIs
    Parâmetros: Nenhum
    Função: Cria ou verifica a pasta de arquivos para FIIs
    Retorno: Sem retorno
'''
def criaDiretorioFIIs():
    os.makedirs(PATH_BASICO_FIIS, exist_ok=True)

'''
    obterListaFIIs()
    Parâmetros: Nenhum
    Função: Verifica se existe o arquivo FIIs_analise.csv e realiza a leitura desse arquivo.
    Esse arquivo é responsável pela lista de FIIs que são analisadas nesse projeto.
    Retorno: Retorna a lista de arquivos.
'''
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

'''
    Método salvarDadoHistorico
    Argumentos:
        - jsonDados: Dados do histórico de uma FII no formado de json (obtidos pela API da brapi)
        - codigo_fii: Código de FII relacionado ao historico
    Função: Realiza a atualização dos dados das FIIs e salva nos arquivos .csv
    Retorno: Nenhum
'''
def salvarDadoHistorico(jsonDados, codigo_fii):

    os.makedirs(PATH_BASICO_FIIS + '/' + codigo_fii, exist_ok=True)

    if(jsonDados == ''):
        return 'Erro - Não foi possível salvar os dados, estão sem informações.'
    
    data_frame = pd.DataFrame(jsonDados)
    data_frame['date'] = pd.to_datetime(data_frame['date'], unit='s').dt.strftime('%d-%m-%Y')

    if os.path.exists(PATH_BASICO_FIIS+ '/' + codigo_fii + '/' + codigo_fii +'.csv'):
        data_frame_existente = pd.read_csv(PATH_BASICO_FIIS+ '/' + codigo_fii + '/' + codigo_fii +'.csv', sep=';', usecols=['date'])
        mascara_novo = ~data_frame['date'].isin(data_frame_existente['date'])
        data_frame_anexar = data_frame[mascara_novo]

        if not data_frame_anexar.empty:
            data_frame_anexar.to_csv(
                PATH_BASICO_FIIS+ '/' + codigo_fii + '/' + codigo_fii +'.csv',
                mode='a',
                sep=';',
                index=False,
                header=False
                )
            print(f'{len(data_frame_anexar)} registros novos inseridos. Em {codigo_fii}')
        else:
            print(f'Nenhum registro novo para inserir. Em {codigo_fii}. Ultimo registro em {data_frame_existente['date'].tail(1).to_string(index=False)}')
    else:
        data_frame.to_csv(
            PATH_BASICO_FIIS+ '/' + codigo_fii + '/' + codigo_fii +'.csv',
            sep=';',
            index=False,
            header=True,
            encoding='utf-8'
            )
        print(f'Criado arquivo csv. Em {codigo_fii}')


def obterUltimaDataRegistro(codigo_fii):

    data_ultima_atualizacao = ''
    if os.path.exists(PATH_BASICO_FIIS+ '/' + codigo_fii + '/' + codigo_fii +'.csv'):
        data_frame_existente = pd.read_csv(PATH_BASICO_FIIS+ '/' + codigo_fii + '/' + codigo_fii +'.csv', sep=';', usecols=['date'])
        #print(data_frame_existente.tail(1))
        data_ultima_atualizacao = data_frame_existente.tail(1)["date"].values[0]
    return data_ultima_atualizacao


def obterdataFramePorCodigo(codigo_fii):

    data_frame_existente = ''
    if os.path.exists(PATH_BASICO_FIIS+ '/' + codigo_fii + '/' + codigo_fii +'.csv'):
        data_frame_existente = pd.read_csv(PATH_BASICO_FIIS+ '/' + codigo_fii + '/' + codigo_fii +'.csv', sep=';')

    return data_frame_existente

def criadataEstatisticoFrameMMsPorCodigo(codigo_fii, data_frame_codigo_estatistico):

    data_frame_codigo_estatistico.to_csv(
            PATH_BASICO_FIIS+ '/' + codigo_fii + '/' + codigo_fii +'_estatistico.csv',
            sep=';',
            index=False,
            header=False
            )

