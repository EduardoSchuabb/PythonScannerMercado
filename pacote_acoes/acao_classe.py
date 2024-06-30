
class Acao:

    def __init__(self, codigo, website, setor, texto_empresa,
                 dividend_yield, nome_curto, preco_atual):
        self.__cogigo = codigo
        self.__website = website
        self.__setor = setor
        self.__texto_empresa = texto_empresa
        self.__dividend_yield = dividend_yield
        self.__nome_curto = nome_curto
        self.__preco_atual = preco_atual

    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def website(self):
        return self.__website
    
    @property
    def setor(self):
        return self.__setor

    @property
    def texto_empresa(self):
        return self.__texto_empresa 
    
    @property
    def dividend_yield(self):
        return self.__dividend_yield
    
    @property
    def nome_curto(self):
        return self.__nome_curto
    
    @property
    def preco_atual(self):
        return self.__preco_atual
    
    @preco_atual.setter
    def preco_atual(self, preco_atual):
        self.__preco_atual = preco_atual

