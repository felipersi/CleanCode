from pagamento import PagamentoCartao, PagamentoBoleto
from pedido import Pedido

if __name__ == "__main__":
    try:
        pagamento = PagamentoCartao()
        pedido = Pedido('João Silva', 1200, 'Rua A, 123', pagamento)
        pedido.processar()
    except ValueError as e:
        print(f"Erro ao processar pedido: {e}")