import csv


class Item:
    taxa_de_desconto = 0.2 # Taxa de desconto de 20%
    todos = []
    
    def __init__(self, nome: str, preco: float, quantidade=0):
        # Realizar validações nos argumentos recebidos
        assert preco >= 0, f"preco {preco} não é maior ou igual a zero!"
        assert quantidade >= 0, f"Quantidade {quantidade} não é maior ou igual a zero!"

        # Atribuir ao objeto self
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

        # Ações a serem executadas
        Item.todos.append(self)

    def calcular_preco_total(self):
        return self.preco * self.quantidade

    def aplicar_desconto(self):
        self.preco = self.preco - (self.preco * self.taxa_de_desconto)

    @classmethod
    def instanciar_do_csv(cls):
        with open('itens.csv', 'r') as f:
            leitor = csv.DictReader(f)
            itens = list(leitor)

        for item in itens:
            Item(
                nome=item.get('nome'),
                preco=float(item.get('preco')),
                quantidade=int(item.get('quantidade')),
            )

    @staticmethod
    def e_inteiro(num):
        # Vamos contar os floats que são ponto zero
        # Por exemplo: 5.0, 10.0
        if isinstance(num, float):
            # Contar os floats que são ponto zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item('{self.nome}', {self.preco}, {self.quantidade})"