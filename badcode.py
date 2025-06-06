# bad code example
# Exemplo de código ruim: Processamento de pedidos com várias responsabilidades
# Este código mistura lógica de pagamento, validação de endereço e processamento de pedidos,
# tornando difícil a manutenção e a compreensão.
def processar_pedido(pedido):
    if pedido['tipo_pagamento'] == 'cartao':
        print('Processando pagamento com cartão...')
        print(f"Valor: {pedido['valor']}")
        if pedido['valor'] > 1000:
            print('Transação recusada: valor excede o limite do cartão.')
            return False
    elif pedido['tipo_pagamento'] == 'boleto':
        print('Gerando boleto...')
        print(f"Valor: {pedido['valor']}")
    else:
        print('Tipo de pagamento inválido.')
        return False

    if pedido['endereco'] == '':
        print('Endereço inválido!')
        return False

    print(f"Pedido de {pedido['cliente']} processado com sucesso!")
    return True


pedido = {
    'cliente': 'João Silva',
    'valor': 1200,
    'tipo_pagamento': 'cartao',
    'endereco': 'Rua A, 123'
}

processar_pedido(pedido)