class Prodduto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))


    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace("R$",""))
        self._preco = valor



p1 = Prodduto("Camiseta", 50)
p1.desconto(10)
print("A camisa com desconto sai por R$ {}".format(p1.preco))

p2 = Prodduto("Caneca", "R$15")
p2.desconto(10)
print("A caneca com desconto sai por R$ {}".format(p2.preco))



