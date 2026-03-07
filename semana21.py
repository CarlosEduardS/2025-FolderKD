
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_bonus(self):
        return self.salario * 0.1

funcionario_comum = Funcionario("João", 2000)
bonus_joao = funcionario_comum.calcular_bonus()
print(f"Bônus do {funcionario_comum.nome}: R${bonus_joao:.2f}")

class Gerente(Funcionario):
    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)
        self.departamento = departamento

    def calcular_bonus(self):
        return (self.salario * 0.15) + 500

gerente_ana = Gerente("Ana", 5000, "Vendas")
print(f"Bônus da {gerente_ana.nome}: R${gerente_ana.calcular_bonus():.2f}")
                        

class Desenvolvedor(Funcionario):
    def __init__(self, nome, salario, lingPri):
        super().__init__(nome, salario)
        self.lingPri = lingPri

    def calcular_bonus(self):
        return self.salario * 0.2

dev = Gerente("Vinicius", 14000, 'Java')
print(f"Bônus da {dev.nome}: R${dev.calcular_bonus():.2f}")