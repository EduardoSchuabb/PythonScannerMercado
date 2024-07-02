
import buscador
import analisador


def main():

    # obtem dados das empresas que compoem o indice bovespa
    #data_frame_acoes=buscador.obterEmpresasIBOV_csv()
    
    # obtem informacoes diversas do yahoo finance das empresas que compoe o indice bovespa
    #buscador.obterInformacoesAcao(data_frame_acoes['Codigo yfinance'])
    
    # obtem dados historicos das acoes.
    #acoes = buscador.obterDadosAcoesYfinance(data_frame_acoes['Codigo yfinance'])




    analisador.informacoesEstatisticaCSV()




if __name__ == "__main__":
    main()
