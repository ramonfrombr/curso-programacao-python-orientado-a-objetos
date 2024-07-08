import csv

class Item:
    taxa_de_desconto = 0.2 # Taxa de desconto de 20%
    todos = []
    
    def __init__(self, nome: str, preço: float, quantidade=0):
        # Realizar validações nos argumentos recebidos
        assert preço >= 0, f"O preço {preço} não é maior ou igual a zero!"
        assert quantidade >= 0, f"A quantidade {quantidade} não é maior ou igual a zero!"

        # Atribuir ao objeto self
        self.nome = nome
        self.preço = preço
        self.quantidade = quantidade

        # Ações a serem executadas
        Item.todos.append(self)

    def calcular_preço_total(self):
        return self.preço * self.quantidade

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
                preço=float(item.get('preço')),
                quantidade=int(item.get('quantidade')),
            )

    @staticmethod
    def é_inteiro(num):
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
        return f"{self.__class__.__name__}('{self.nome}', {self.preço}, {self.quantidade})"

class Telefone(Item):
    def __init__(self, nome: str, preço: float, quantidade=0, telefones_quebrados=0):
        # Chamar a função super para ter acesso a todos os atributos/métodos
        super().__init__(nome, preço, quantidade)

        # Realizar validações nos argumentos recebidos
        assert telefones_quebrados >= 0, f"Telefones quebrados {telefones_quebrados} não é maior ou igual a zero!"

        # Atribuir ao objeto self
        self.telefones_quebrados = telefones_quebrados

telefone1 = Telefone("jscTelefonev10", 500, 5, 1)

print(Item.todos)