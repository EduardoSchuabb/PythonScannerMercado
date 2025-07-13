
import persistencia.persistencia_FIIs as persistencia_FIIs
import buscador.buscador_FIIs as buscador_FIIs
import analisador

def main():
    codigo_fii = 'XPML11'
    tempo = '1d'
    #buscador_FIIs.requestBrapiFii(codigo_fii, tempo)
    codigo_fii = 'GZIT11'
    #buscador_FIIs.requestBrapiFii(codigo_fii, tempo)
    persistencia_FIIs.criaDiretorioFIIs()

    #Carregar a lista de FIIs para análise.
    lista_codigos_fiis = persistencia_FIIs.obterListaFIIs()

    





if __name__ == "__main__":
    main()
