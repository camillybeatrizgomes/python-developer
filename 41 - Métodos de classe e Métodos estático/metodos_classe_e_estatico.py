class Pessoa:
    def __init__(self, nome = None, idade = None):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_apartir_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2025 - ano
        return cls(nome, idade)
    
    @staticmethod
    def maior_de_idade(idade):
        return idade >= 18
    
p1 = Pessoa.criar_apartir_data_nascimento(2003, 2, 20, "Camilly")
print(p1.nome, p1.idade)

print(Pessoa.maior_de_idade(17))
print(Pessoa.maior_de_idade(20))