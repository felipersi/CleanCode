from pagamento import Pagamento  
class Pedido:
    def __init__(self, cliente, valor, endereco, pagamento: Pagamento):
        self.cliente = cliente
        self.valor = valor
        self.endereco = endereco
        self.pagamento = pagamento

    def validar(self):
        if not self.endereco.strip():
            raise ValueError('Endereço inválido.')

    def processar(self):
        self.validar()
        self.pagamento.processar(self.valor)
        print(f"Pedido de {self.cliente} processado com sucesso!")