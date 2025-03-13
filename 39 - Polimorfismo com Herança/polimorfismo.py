class Passaro:
    def voar(self):
        print("Voando...")

class Pardal(Passaro):
    def voar(self):
        print("O Pardal pode voar")
    
class Avestruz(Passaro):
    def voar(self):
        print("O Avestruz não pode voar")

class Aviao(Passaro):
    def voar(self):
        print("O Avião está decolando...")

def plano_voo(obj):
    obj.voar()

plano_voo(Pardal())
plano_voo(Avestruz())
plano_voo(Aviao())