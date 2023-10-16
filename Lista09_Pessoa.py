class Pessoa:
    
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.filhos = []

    def adicionar_filho(self, filho):
        self.filhos.append(filho)

    def resumo(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"

class Pai(Pessoa):
    def resumo(self):
        resumo_pai = super().resumo()
        return f"Pai - {resumo_pai}"

class Mae(Pessoa):
    def resumo(self):
        resumo_mae = super().resumo()
        return f"Mãe - {resumo_mae}"

class Filho(Pessoa):
    def adicionar_pai_mae(self, pai, mae):
        self.pai = pai
        self.mae = mae

    def resumo(self):
        resumo_filho = super().resumo()
        return f"Filho - {resumo_filho}, Pai: {self.pai.nome}, Mãe: {self.mae.nome}"


pai = Pai("João", 40)
mae = Mae("Maria", 35)
filho1 = Filho("Pedro", 10)
filho2 = Filho("Ana", 8)

filho1.adicionar_pai_mae(pai, mae)
filho2.adicionar_pai_mae(pai, mae)

pai.adicionar_filho(filho1)
mae.adicionar_filho(filho1)
pai.adicionar_filho(filho2)
mae.adicionar_filho(filho2)

print(pai.resumo())
print(mae.resumo())
print(filho1.resumo())
print(filho2.resumo())
