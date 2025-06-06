# Refatoração de Código com Princípios de Clean Code

Este repositório apresenta a refatoração de um código legado com más práticas, utilizando os princípios do Clean Code para torná-lo mais legível, modular, testável e fácil de manter.

## Objetivo

O objetivo deste projeto é demonstrar a aplicação prática de boas práticas de programação e princípios de Clean Code através da refatoração de um código Python mal estruturado.

Foram aplicados:

- Princípios de Clean Code (legibilidade, nomes claros, simplicidade)
- Boas práticas: SOLID
- Padrão de projeto Strategy
- Separação de responsabilidades entre módulos
- Testes automatizados com `unittest`

## Problemas do Código Original

O código original misturava múltiplas responsabilidades em funções monolíticas, utilizava estruturas condicionais complexas e dificultava manutenção e testes. Não havia organização em classes, nem modularização adequada.

## Solução Aplicada

- Criamos a classe `Pedido` para representar os dados e lógica de um pedido.
- Implementamos a interface `Pagamento`, com as estratégias `PagamentoCredito` e `PagamentoBoleto`.
- Aplicamos o padrão Strategy para abstrair as formas de pagamento.
- Modularizamos o código separando arquivos por responsabilidade.
- Escrevemos testes unitários para verificar o funcionamento após a refatoração.

## Estrutura de Arquivos

CleanCode/

├── main.py # Ponto de entrada do sistema

├── pedido.py # Classe Pedido com validações e execução

├── pagamento.py # Interface e estratégias de pagamento (Strategy)

├── test_pedido.py # Testes unitários com unittest

└── README.md # Documentação do projeto

## Como Executar o Código

### Pré-requisitos

- Python 3.8 ou superior instalado

### Executar o código principal

bash
python3 main.py

### Executar testes unitários

python3 -m unittest test_pedido.py
