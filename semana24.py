class ProdutoEletronico:
    def __init__(self, marca, modelo, preco):
        self.marca = marca
        self.modelo = modelo
        self.preco = preco
        self.valor_desconto = 0

    def exibir_informacoes(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Preço original: R$ {self.preco:.2f}")
        print(f"Preço com desconto: R$ {self.preco - self.valor_desconto:.2f}\n")

    def aplicar_desconto(self, desconto):
        if "%" in desconto:
            self.valor_desconto = self.preco * (float(desconto.replace('%', '')) / 100)
        elif desconto.replace('.', '', 1).isdigit():
            self.valor_desconto = float(desconto)
        elif desconto.isnumeric():
            self.valor_desconto = self.preco * (float(desconto) / 100)
        else:
            print("Formato de desconto inválido.")

class Smartphone(ProdutoEletronico):
    def __init__(self, marca, modelo, preco):
        super().__init__(marca, modelo, preco)

    def aplicar_desconto(self, desconto):
        super().aplicar_desconto(desconto)
        # Aplica bônus de 5%
        bonus = self.preco * 0.1
        self.valor_desconto += bonus
        print(f"Bônus de {int(desconto)}% aplicado: R$ {bonus:.2f}")

    def exibir_informacoes(self):
        super().exibir_informacoes()
        
class Televisor(ProdutoEletronico):
    def __init__(self, marca, modelo, preco):
        super().__init__(marca, modelo, preco)

    def aplicar_desconto(self, desconto):
        super().aplicar_desconto(desconto)
        # Aplica bônus de 10%
        bonus = self.preco * 0.1
        self.valor_desconto += bonus
        print(f"Bônus de {int(desconto)}% aplicado: R$ {bonus:.2f}")

    def exibir_informacoes(self):
        super().exibir_informacoes()
        
class Tablet(ProdutoEletronico):
    def __init__(self, marca, modelo, preco):
        super().__init__(marca, modelo, preco)

    def aplicar_desconto(self, desconto):
        super().aplicar_desconto(desconto)
        # Aplica bônus de 10%
        bonus = self.preco * 0.1
        self.valor_desconto += bonus
        print(f"Bônus de {int(desconto)}% aplicado: R$ {bonus:.2f}")

    def exibir_informacoes(self):
        super().exibir_informacoes()

#desconto_input = input("Desconto (ex: 20%, 30, 0.2): \n")
Aparelhos = [Smartphone("Xiaomi", "Mi 15 Ultra", 5600), Televisor("Xiaomi", "Mi TV PLUS", 4800), Tablet("Xiaomi", "Mi Pad 6", 2200)]

for Aparelho in Aparelhos:
    #Aparelho.aplicar_desconto(desconto_input)
    Aparelho.aplicar_desconto('10')
    Aparelho.exibir_informacoes()
