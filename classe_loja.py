import datetime as dt
from classe_cliente import Cliente

class Loja:
    total_alugueis = 0
    
    def __init__(self, estoque):
        self.estoque_inicial = estoque
        self.estoque_atual = estoque
        self.alugueis_ativos = []
        self.valores = {'hora': 5, 'dia': 25, 'semana': 100}
        self.desconto_familia = 0.3

    def __str__(self) -> str:
        return f"Ada Let's Bike \nEstoque: {self.consultar_estoque()} | Valores: Hora: R${self.valores['hora']}, Dia: R${self.valores['dia']}, Semana: R${self.valores['semana']}"

    def __validar_modo(self, valor):
        '''Recebe a modalidade de aluguel inserida e valida a entrada.'''
        valor = valor.lower()
        if valor in self.valores.keys():
            return valor
        else:
            raise ValueError("Modalidade de aluel inválida. As opções válidas são 'hora', 'dia' e 'semana'.")
    
    @property
    def alugueis_ativos(self):
        return self.__alugueis_ativos
    @alugueis_ativos.setter
    def alugueis_ativos(self, valor):
        if valor == []:
            self.__alugueis_ativos = valor
        else:
            self.__alugueis_ativos.append(valor)    
 
    @property
    def desconto_familia(self):
        return self.__desconto_familia
    @desconto_familia.setter
    def desconto_familia(self, valor):
        try:
            valor = float(valor)
        except ValueError:
            raise ValueError(("O valor do desconto deve ser numérico"))
        self.__desconto_familia = valor
    
    @property
    def estoque_inicial(self):
        return self.__estoque_inicial
    @estoque_inicial.setter
    def estoque_inicial(self, valor):
        self.__estoque_inicial = valor
                 
    @property
    def valores(self):
        return self.__valores
    @valores.setter
    def valores(self, novos_valores: dict):
        self.__valores = novos_valores   
    
    def alugar_item(self, modo, quantidade, cliente):
        '''Registra o aluguel da quantidade de itens informada, relacionada ao objeto Cliente recebido.
        Completa a operação apenas se a loja tiver a quantidade necessária de itens no estoque. Cada operação
        é relacionada a uma ID incremental.'''
        
        if isinstance(cliente, Cliente):
            modo = self.__validar_modo(modo)
            if self.consultar_estoque() >= quantidade:
                Loja.total_alugueis += 1
                self.estoque_atual -= quantidade
                data_aluguel = dt.datetime.now()
                self.alugueis_ativos= {Loja.total_alugueis: [cliente, data_aluguel, quantidade, modo]}
            else:
                raise ValueError(f"Quantidade requisitada excede o estoque atual da loja. No momento existem apenas {self.consultar_estoque()} disponíveis.")
        else:
            raise ValueError(f"Cliente inválido")

    def buscar_aluguel_ativo(self, id_aluguel):
        '''Procura se há algum registro de aluguel ativo com a ID informada'''
        
        aluguel = [i for i in self.alugueis_ativos if id_aluguel in i.keys()]
        if aluguel:
            return aluguel[0]
        else:
            raise ValueError(f"Cadastro de id {id_aluguel} não encontrado.")

    def calcular_valor(self, id_aluguel):
        '''Recebe a ID do aluguel e calcula o valor final de acordo com a modalidade de aluguel.
        Leva em consideração a existência do desconto para famílias em registros de 3 ou mais itens.'''
        
        id_aluguel = int(id_aluguel)
        aluguel = self.buscar_aluguel_ativo(id_aluguel)[id_aluguel]
        conversao_seg = {'hora': 60, 'dia': 86400, 'semana': (86400 * 7)}
        data_retirada = aluguel[1]
        quantidade = aluguel[2]
        modo = aluguel[3]
        desconto_familia = self.desconto_familia if quantidade >= 3 else 0
        data_devolucao = dt.datetime.now()
        tempo_total = (data_devolucao - data_retirada).total_seconds()
        valor_total = (tempo_total / conversao_seg[modo]) * self.valores[modo] * quantidade
        return round(valor_total - (desconto_familia * valor_total), 2)
    
    def consultar_estoque(self) -> int:
        '''Consulta quantos itens disponíveis a loja tem. Retorna um inteiro'''
        return self.estoque_atual

    def devolver_item(self, id_aluguel):
        '''Retorna os itens relativos à ID informada para o estoque e informa o valor final a ser pago
        pelo cliente.'''
        
        id_aluguel = int(id_aluguel)
        aluguel = self.buscar_aluguel_ativo(id_aluguel)
        valor_final = self.calcular_valor(id_aluguel)
        self.alugueis_ativos.remove(aluguel)
        quantidade = aluguel[id_aluguel][2]
        self.estoque_atual += quantidade
        
        return f'ID: {id_aluguel} | Itens devolvidos: {quantidade} | Valor final: R${valor_final}'
    
        
