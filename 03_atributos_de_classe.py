class Item:
    taxa_de_desconto = 0.2 # Taxa de desconto de 20%
    todos = []

    def __init__(self, nome: str, preco: float, quantidade=0):
        # Valida argumentos recebidos
        assert preco >= 0, f"Preço {preco} não é maior ou igual a zero!"
        assert quantidade >= 0, f"Quantidade {quantidade} não é maior ou igual a zero!"

        # Define propriedades do objeto
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

        # Adiciona item a lista com todos os items
        Item.todos.append(self)
    
    def calcular_preco_total(self):
        return self.preco * self.quantidade
    
    def aplicar_desconto(self):
        self.preco = self.preco - (self.preco * self.taxa_de_desconto)
    
    def __repr__(self):
        return f"Item('{self.nome}', {self.preco}, {self.quantidade})"

item1 = Item("Telefone", 100, 1)
item1 = Item("Computador", 1000, 2)
item1 = Item("Videogame", 500, 5)
item1 = Item("Geladeira", 2000, 3)

print(Item.todos)