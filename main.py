from classe_cliente import Cliente
from classe_loja import Loja

nova_loja = Loja(30)

menu_cliente = ''' 
                    1. Ver bicicletas disponíveis na loja.
                    2. Alugar bicicletas.
                    3. Sair.
                    '''

menu_loja = ''' 
                    1. Ver bicicletas disponíveis na loja.
                    2. Retornar bicicletas.
                    3. Calcular valor de cobrança
                    4. Listar aluguéis ativos
                    5. Sair.
                    '''

tipo_usuario = input("Escolha o tipo de usuário - 1. Loja | 2. Cliente: ")
if tipo_usuario == '1':
    while True:
        print(menu_loja)
        opcao = input("Insira a opção desejada: ")
        if opcao == '5':
            print("Encerrando sistema. Até mais!")
            break
        elif opcao == '1':
            estoque = nova_loja.consultar_estoque()
            print(f"A loja possui {estoque} bicicletas em disponíveis.")
        elif opcao == '2':
            id_aluguel = input("Insira a ID do aluguel a ser encerrado: ")
            try:
                print(nova_loja.devolver_item(id_aluguel))
            except ValueError as ve:
                print(f"Erro: {ve}")
        elif opcao == '3':
            id_aluguel = input("Insira a ID do aluguel a ser calculado: ")
            try:
                print(f'Total do aluguel {id_aluguel}: R${nova_loja.calcular_valor(id_aluguel)}')
            except ValueError as ve:
                print(f"Erro: {ve}")
        elif opcao == '4':
            if nova_loja.alugueis_ativos:
                for aluguel in nova_loja.alugueis_ativos:
                    print(aluguel)
            else:
                print("Não há registro de aluguéis ativos no momento.")


if tipo_usuario == '2':
    novo_cliente = None
    while True:
        if not novo_cliente:
            nome_cliente = input("Digite o nome do cliente: ")
            cpf_cliente = input("Digite o CPF do cliente: ")
            try:
                novo_cliente = Cliente(nome_cliente, cpf_cliente)
                print(f"Olá, {nome_cliente}! Bem-vindo(a) à loja {nova_loja}")
            except ValueError as ve:
                print(f"Erro: {ve}")
        else:        
            print(menu_cliente)
            opcao = input("Insira a opção desejada: ")
            if opcao == '3':
                print("Encerrando sistema. Até mais!")
                break
            elif opcao == '1':
                print(novo_cliente.consultar_bicicletas(nova_loja))
            elif opcao == '2':
                quantidade = input("Insira a quantidade desejada: ")
                modo = input("Insira a modalidade escolhida - Hora | Dia | Semana: ")
                try:
                    print(novo_cliente.registrar_aluguel(nova_loja, quantidade, modo))
                except ValueError as ve:
                    print(f"Erro: {ve}")
    

