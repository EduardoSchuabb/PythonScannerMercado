from datetime import date, datetime
from buscador import buscador_FIIs
from persistencia import persistencia_FIIs
from analisador import estatistica_descritiva
import sys



'''
    Método: analisador_FIIs
    Argumentos: Nenhum
    Função: Realiza a parte negocial relacionada a FII. Por enquanto, apenas realiza a atualização das informações.
    Retorno: Nenhum
'''
def analisador_FIIs():
    # Primeira parte, verificação de atualização das informações.
    # Verificar como obter outras informações dos FIIs importantes para análise. Estudar isso...
    #

    persistencia_FIIs.criaDiretorioFIIs()
    lista_codigos_fiis = persistencia_FIIs.obterListaFIIs()
    
    if sys.argv[1] == 1:
        print('Atualizando base de dados.')
        tempo = '3mo'
        for codigo in lista_codigos_fiis:

            data_ultima_atualizacao = persistencia_FIIs.obterUltimaDataRegistro(codigo)

            if data_ultima_atualizacao:
                data_ultima_atualizacao_convertida = datetime.strptime(data_ultima_atualizacao, "%d-%m-%Y").date()
                data_atual = date.today()
                
                if data_ultima_atualizacao_convertida < data_atual:
                    json_historico = buscador_FIIs.requestBrapiFiiHistorico(codigo, tempo)
                    persistencia_FIIs.salvarDadoHistorico(json_historico, codigo)
                else:
                    print("A data do ultimo registro não é anterior a data atual. - Não atualizar codigo")
        
#------------------------------------------------------------------------------------------------------------
    # Fazer cálculos estatísticos:
        # Médias móveis: Verificar quais períodos (três períodos?).
            # Fazer o cálculo das médias móveis e anexar no arquivo .csv
        # Quartis: Fazer análise dos quartis?
        # Ver como analisar pontos de suporte e resistência.
    
    for codigo in lista_codigos_fiis:
        data_frame_codigo = persistencia_FIIs.obterdataFramePorCodigo(codigo)
        data_frame_estatistico = estatistica_descritiva.calculoMediaTodosFIIs(data_frame_codigo)

        #fazer analise dee quartis?


        persistencia_FIIs.criadataEstatisticoFrameMMsPorCodigo(codigo, data_frame_estatistico)








    
   
