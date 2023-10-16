class Pessoa: #Super Class 
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def resumo(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")


class Pai(Pessoa):#Classe Filho
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.filhos = []

    def adicionar_filho(self, filho):
        if isinstance(filho, Filho):
            self.filhos.append(filho)

    def resumo(self):
        super().resumo()
        print("Classe: Pai")
        print(f"Número de Filhos: {len(self.filhos)}")


class Mae(Pessoa):):#Classe Filho
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.filhos = []

    def adicionar_filho(self, filho):
        if isinstance(filho, Filho):
            self.filhos.append(filho)

    def resumo(self):
        super().resumo()
        print("Classe: Mãe")
        print(f"Número de Filhos: {len(self.filhos)}")


class Filho(Pessoa): ):#Classe Filho
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.pai = None
        self.mae = None

    def adicionar_pai(self, pai):
        if isinstance(pai, Pai):
            self.pai = pai

    def adicionar_mae(self, mae):
        if isinstance(mae, Mae):
            self.mae = mae

    def resumo(self):
        super().resumo()
        print("Classe: Filho")
        if self.pai:
            print(f"Pai: {self.pai.nome}")
        if self.mae:
            print(f"Mãe: {self.mae.nome}")


# Exemplo de uso
pai = Pai("João", 40)
mae = Mae("Maria", 35)
filho1 = Filho("Pedro", 10)
filho2 = Filho("Ana", 8)

pai.adicionar_filho(filho1)
mae.adicionar_filho(filho1)
pai.adicionar_filho(filho2)
mae.adicionar_filho(filho2)

filho1.adicionar_pai(pai)
filho1.adicionar_mae(mae)
filho2.adicionar_pai(pai)
filho2.adicionar_mae(mae)

print("Resumo do Pai:")
pai.resumo()
print("\nResumo da Mãe:")
mae.resumo()
print("\nResumo do Filho 1:")
filho1.resumo()
print("\nResumo do Filho 2:")
filho2.resumo()




