#Codigo para registro semana 5 de Processos
import random
from datetime import date
import time

class site:
    def __init__(self):
        self.categorias = {}
        self.carrinho = {}  # Dicionário para o carrinho de compras

    def cliente(self,nome,contato,endereço,historico_de_pedido=0):
        self.nm = nome
        self.cont = contato
        self.end = endereço

    def produtos(self, categoria, quantidade, descricao, preco):
        # Gera IDs únicos para cada produto
        idd = random.randint(1000,9999)
        sub_idd = random.randint(100,999)

        # Adiciona o produto à categoria
        self.adicionar_categoria(categoria, quantidade, idd, sub_idd, descricao, preco)

    def adicionar_categoria(self, categoria, quantidade, idd, sub_idd, descricao, preco):
        if categoria in self.categorias:
            if f"{idd}.{sub_idd}" in self.categorias[categoria]:
                self.categorias[categoria][f"{idd}.{sub_idd}"]['quantidade'] += quantidade
            else:
                self.categorias[categoria][f"{idd}.{sub_idd}"] = {
                    'quantidade': quantidade,
                    'descricao': descricao,
                    'preco': preco
                }
        else:
            self.categorias[categoria] = {f"{idd}.{sub_idd}": {
                'quantidade': quantidade,
                'descricao': descricao,
                'preco': preco
            }}

    def mostrar_estoque(self):
        print("\nEstoque Atual:")
        for categoria, produtos in self.categorias.items():
            print(f"Categoria: \033[32m{categoria}\033[m")
            for id_produto, info in produtos.items():
                print(f" - ID do Produto: \033[33m{id_produto}\033[m")
                print(f"    - Descrição: {info['descricao']}")
                print(f"    - Preço: R$ {info['preco']:.2f}")
                print(f"    - Quantidade: {info['quantidade']}")

    def adicionar_ao_carrinho(self, id_produto, quantidade):
        """Adiciona um produto ao carrinho de compras."""
        if id_produto in self.carrinho:
            self.carrinho[id_produto] += quantidade
        else:
            self.carrinho[id_produto] = quantidade
        print(f"Produto {id_produto} adicionado ao carrinho com {quantidade} unidades.")

    def mostrar_carrinho(self):
        """Exibe os itens no carrinho de compras."""
        if not self.carrinho:
            print("Seu carrinho está vazio.")
            return

        print("\nCarrinho de Compras:")
        self.total = 0
        for id_produto, quantidade in self.carrinho.items():
            categoria = self.obter_categoria_do_produto(id_produto)
            if categoria:
                produto = self.categorias[categoria][id_produto]
                preco_total = quantidade * produto['preco']
                print(f" - {categoria} (ID: {id_produto}) - {produto['descricao']} - Quantidade: {quantidade} - Preço: R$ {preco_total:.2f}, horario: {date.today()}")
                self.total += preco_total
            else:
                print(f" - Produto com ID {id_produto} não encontrado no estoque.")
        print(f"Total: R$ {self.total:.2f}")

    def obter_categoria_do_produto(self, id_produto):
        """Retorna a categoria do produto com base no ID."""
        for categoria, produtos in self.categorias.items():
            if id_produto in produtos:
                return categoria
        return None
    def pagamento(self,saldo,forma_de_pagamento):
        self.sal = saldo
        self.pix = forma_de_pagamento
        while True:
            if self.pix in ['credito','cre','c','cr','cred','credi','credit']:
                if self.sal >= self.total - 20:
                    self.sal -= self.total + 20
                    print(f'\nPagamento feito com sucesso, saldo restante {self.sal:.2f}\n')
                    break
                else:
                    self.sal = float(input('Erro saldo insuficiente, qual é seu saldo:\n'))
                    continue
            elif self.pix in ['debito','deb','d','de','debi','debit']:
                if self.sal >= self.total:
                    self.sal -= self.total
                    print(f'\nPagamento feito com sucesso, saldo restante {self.sal:.2f}\n')
                    break
                else:
                    self.sal = float(input('Erro saldo insuficiente, qual é seu saldo:\n'))
                    exit
                    continue
            else:
                self.saldo = float(input('Erro saldo insuficiente, qual é seu saldo:\n'))
                exit
                continue
    def entrega(self):
        print(f'A encomenda sera enviada para seu endereço {self.end}')
        for i in range(0,4):
            match i:
                case 0:
                    print('\nSua encomenda foi \033[32mprocessada\033[m')
                case 1:
                    print('\nSua encomenda foi \033[32mrecebida\033[m')
                case 2:
                    print('\nSua encomenda foi \033[32menviada\033[m')
                case 3:
                    print('\nSua encomenda foi \033[32mentrege\033[m')
            time.sleep(random.randint(1,5))
    
# Exemplos de uso
print('-'*50,'\033[36m\nbem vindo a nossa loja online!!\n\033[m')
loja = site()
loja.cliente(input('Digite seu nome\n'),input('Digite seu telefone\n'),input('Digite seu endereço\n'))

# Adicionando produtos com IDs únicos, descrição e preço
loja.produtos('Tênis Esportivo', 34, 'Tênis de corrida leve e confortavel', 120.00)
loja.produtos('Camisetas Esportivas', 23, 'Camiseta 100% poliester', 35.50)
loja.produtos('Calça Social', 56, 'Calça casual ingrivelmente confortavel', 80.99)
loja.produtos('Jaqueta Casual',29,'Perfeita para o frio do verão',255.99)

# Mostrando o estoque
loja.mostrar_estoque()

# Adicionando itens ao carrinho
while True:
    loja.adicionar_ao_carrinho(input('Digite o id do produto:\n').lower(), int(input('Digite a quantidade:\n')))
    res = input('\nDeseja comprar mais algum item? s/n\n').lower()
    if res == 'n':
        break
    if res == 's':
        continue
    else:
        continue

# Mostrando o carrinho
loja.mostrar_carrinho()
loja.pagamento(float(input('\nqual é seu saldo báncario:\n')),input('Deseja pagar usando credito ou debito\n').lower())
loja.entrega()