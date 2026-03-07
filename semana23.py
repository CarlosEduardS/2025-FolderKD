
class ProdutoEletronico:
    def __init__(self, marca, modelo, preco):
        self.marca = marca
        self.modelo = modelo
        self.preco = preco

    def exibir_informacoes(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Preço: R$ {self.preco:.2f}")
        
class tablet(ProdutoEletronico):
    def __init__(self, marca, modelo, preco, caneta = False):
        super().__init__(marca, modelo, preco)
        self.caneta = caneta
        
    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"O tablet possui caneta? ", self.caneta)
    
intance = tablet("Xiaomi",'Mi 6', 2200).exibir_informacoes()