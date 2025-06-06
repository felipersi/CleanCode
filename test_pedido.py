import unittest
from pagamento import PagamentoCartao, PagamentoBoleto
from pedido import Pedido

class TestPedido(unittest.TestCase):

    def test_pagamento_cartao_valido(self):
        pedido = Pedido('Ana', 500, 'Rua B, 456', PagamentoCartao())
        pedido.processar()

    def test_pagamento_cartao_invalido(self):
        with self.assertRaises(ValueError):
            pedido = Pedido('Carlos', 1500, 'Rua C, 789', PagamentoCartao())
            pedido.processar()

    def test_pagamento_boleto(self):
        pedido = Pedido('Bia', 700, 'Rua D, 101', PagamentoBoleto())
        pedido.processar()

    def test_endereco_invalido(self):
        with self.assertRaises(ValueError):
            pedido = Pedido('Lucas', 300, '', PagamentoCartao())
            pedido.processar()

if __name__ == '__main__':
    unittest.main()