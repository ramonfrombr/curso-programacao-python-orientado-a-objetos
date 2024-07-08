# Sem programação orientada a objetos, as linhas de código e as variáveis ficam avulsas e sem relaçções definidas entre si.
# nome = "Telefone"
# preco = 100
# quantidade = 5
# preco_total = 100 * 5
# print(f"Produto: {nome}. Preço total: {preco_total}.")
#
# def calcular_preco_total(preco, quantidade):
#       return preco * quantidade

# Com classes, podemos juntar variáveis e funções em um bloco e criar o que chamamos de objeto

# Como criar uma classe
class Item:
    def calcular_preco_total(self, preco, quantidade):
        return preco * quantidade

# Criando uma instância de uma classe
item1 = Item()

# Definindo atributos
item1.nome = "Telefone"
item1.preco = 100
item1.quantidade = 5

# Chamando métodos de uma instância de uma classe
print(item1.calcular_preco_total(item1.preco, item1.quantidade))

# Criando uma instância de uma classe
item2 = Item()

# Definindo atributos
item2.nome = "Computador"
item2.preco = 1000
item2.quantidade = 3

# Chamando métodos de uma instância de uma classe
print(item2.calcular_preco_total(item2.preco, item2.quantidade))