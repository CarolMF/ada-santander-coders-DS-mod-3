# modulo-3-projeto_final
 Projeto final do módulo de OOP do programa Santander Coders.

 Enunciado:
 Sistema de Empréstimo de Bicicletas

Vocês farão um sistema de empréstimo de bicicletas, que envolverá duas classes principais (Cliente, Loja).

Cliente pode:
Ver as bicicletas disponíveis na loja
Alugar Bicicletas por hora (R\$5/hora)
Alugar bicicletas por dia (R\$25/dia)
Alugar bicicletas por semana (R\$100/semana)
Aluguel para família, uma promoção que 3 ou mais empréstimos (de qualquer tipo) com 30% de desconto no valor final.

Loja pode:
Calcular a conta quando o cliente decidir devolver a bicicleta
Mostrar o estoque de bicicleta
Receber pedidos de aluguéis por hora, diários ou semanais validando a possibilidade com o estoque e modo de aluguel existente

Por questão de simplicidade vamos assumir que:
Cada empréstimo segue apenas um modelo de cobrança (hora, dia ou semana)
O cliente pode decidir livremente quantas bicicletas quer alugar
Os pedidos de aluguéis só podem ser efetuados se houver bicicletas suficientes disponíveis
Não se preocupem quanto a dinheiro em caixa das Lojas nem dos Clientes

Utilize a biblioteca `datetime` para trabalhar com tempo no seu programa
