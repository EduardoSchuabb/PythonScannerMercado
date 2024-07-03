
import buscador
import analisador


def main():

    # obtem dados das empresas que compoem o indice bovespa
    data_frame_acoes=buscador.obterEmpresasIBOV_csv()
    
    # obtem informacoes diversas do yahoo finance das empresas que compoe o indice bovespa
    #buscador.obterInformacoesAcao(data_frame_acoes['Codigo yfinance'])
    
    # obtem dados historicos das acoes.
    ### - Verificar estratégia. Não desejo esse retorno dessa funcao. - ###
    #informacoes_acoes = buscador.obterDadosAcoesYfinance(data_frame_acoes['Codigo yfinance'])


    analisador.informacoesEstatisticaCSVFechamento(data_frame_acoes['Codigo yfinance'])




if __name__ == "__main__":
    main()
