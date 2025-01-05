"""Endereço por CEP"""

import requests

class CEP:
    """Representa um CEP com dados obtidos viaCEP
    
    Atributos:
        cep (str): código de endereçamento Postal.
        logradouro (str): Nome da rua/avenida.
        bairro: (str): Bairro do CEP.
        cidade (str): Localidade/cidade do CEP.
        estado (str): UF do CEP.
    """
    
    def __init__(self, cep: str) -> None:
        self.cep = cep
        self.logradouro = ''
        self.bairro = ''
        self.cidade = ''
        self.estado = ''
        
        self.__buscar_cep()
        
    def __repr__(self) -> str:
        return f'CEP: {self.cep}, '\
            f'Rua: {self.logradouro}, '\
                f'Bairro: {self.bairro}, '\
                    f'Cidade: {self.cidade}, '\
                        f'Estado: {self.estado}'

        
    def __buscar_cep(self) -> None:
        resposta = requests.get(f'https://viacep.com.br/ws/{self.cep}/json/', timeout=5)
        
        if resposta.status_code != 200:
            print(f'Algo de errado ocorreu.\nErro: {resposta.status_code}')
            return None
        
        dados = resposta.json()
        
        if 'erro' in dados:
            print(f'Erro ao acessar o CEP {self.cep}.\nVerifique o número e tente novamente.')
            return None
        
        self.logradouro = dados.get('logradouro', '')
        self.bairro = dados.get('bairro', '')
        self.cidade = dados.get('localidade', '')
        self.estado = dados.get('estado', '')


minha_casa = CEP('51021360')
print(minha_casa)