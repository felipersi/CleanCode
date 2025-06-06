from abc import ABC, abstractmethod

class Pagamento(ABC):
    @abstractmethod
    def processar(self, valor):
        pass

class PagamentoCartao(Pagamento):
    def processar(self, valor):
        if valor > 1000:
            raise ValueError('Transação recusada: valor excede o limite do cartão.')
        print(f'Pagamento de R${valor:.2f} com cartão processado.')

class PagamentoBoleto(Pagamento):
    def processar(self, valor):
        print(f'Boleto gerado para o valor de R${valor:.2f}.')