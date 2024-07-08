class Item:
    def __init__(self, nome: str, preco: float, quantidade=0):
        # Valida os argumentos recebidos
        assert preco >= 0, f"Preço {preco} não é igual ou maior que zero!"
        assert quantidade >= 0, f"Quantidade {quantidade} não é maior ou igual a zero!"

        # Atribui ao objeto self
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_preco_total(self):
        return self.preco * self.quantidade

item1 = Item("Telefone", 100, 1)
item2 = Item("Computador", 1000, 3)

print(item1.calcular_preco_total())
print(item2.calcular_preco_total())