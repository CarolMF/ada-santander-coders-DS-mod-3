class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        
    def __repr__(self):
        return f'Nome: {self.nome} | CPF: {self.cpf}'
        
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, novo_nome):
        if len(novo_nome) > 3 and type(novo_nome) == str:
            self.__nome = novo_nome.title()
        else:
            raise ValueError("Nome do cliente inválido")
        
    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self, valor):
        '''Valida a entrada do CPF do cliente de acordo com as regras de dígito verificador.'''
        caracteres = [int(n) for n in valor if n.isnumeric()]
        if len(caracteres) == 11 and len(set(caracteres)) > 1:
            total = sum(x * y for x, y in zip(caracteres[-3::-1], range(2, 11)))
            resto = total % 11
            if resto < 2:
                primeiro_digito = 0
            else:
                primeiro_digito = 11 - resto
            
            total = sum(x * y for x, y in zip(caracteres[-2::-1], range(2, 12)))
            resto = total % 11
            if resto < 2:
                segundo_digito = 0
            else:
                segundo_digito = 11 - resto
                
            if primeiro_digito == caracteres[-2] and segundo_digito == caracteres[-1]:
                cpf = ''.join(str(n) for n in caracteres)
                self.__cpf = cpf
                return self.__cpf
        raise ValueError("CPF inválido")
        
    def consultar_bicicletas(self, loja) -> int: 
        '''Consulta estoque da loja e retorna quantidade de bicicletas disponíveis'''        
        estoque_atual = loja.consultar_estoque()
        return f"Total de bicicletas disponívels: {estoque_atual}"
    
    def registrar_aluguel(self, loja, quantidade, modo):
        '''Caso a loja tenha a quantidade suficiente de itens disponíveis, registra o empréstimo
        de acordo com a modalidade escolhida (hora, dia, semana)'''
        try:
            quantidade = int(quantidade)
        except ValueError:
            raise ValueError(f"A quantidade deve ser um valor numérico: {quantidade}")
        if quantidade > 0:
            loja.alugar_item(modo, quantidade, self)
            return f'Aluguel por {modo} de {quantidade} itens confirmado.'
        else:
            raise ValueError(f"A quantidade deve ser maior que zero.")
        