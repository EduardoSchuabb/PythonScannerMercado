from buscador import buscador_FIIs
from persistencia import persistencia_FIIs


def analisador_FIIs():

    persistencia_FIIs.criaDiretorioFIIs()
    lista_codigos_fiis = persistencia_FIIs.obterListaFIIs()
    
    #codigo = 'ALZR11'
    tempo = '3mo'
    for codigo in lista_codigos_fiis:
        json_historico = buscador_FIIs.requestBrapiFiiHistorico(codigo, tempo)
        persistencia_FIIs.salvarDadoHistorico(json_historico, codigo)
    
   
