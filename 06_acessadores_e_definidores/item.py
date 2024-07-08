import csv

class Item:
    taxa_de_desconto = 0.2 # Taxa de desconto de 20%
    todos = []
    
    def __init__(self, nome: str, preço: float, quantidade=0):
        # Executar validações nos argumentos recebidos
        assert preço >= 0, f"Preço {preço} não é maior ou igual a zero!"
        assert quantidade >= 0, f"Quantidade {quantidade} não é maior ou igual a zero!"

        # Atribuir ao objeto self
        self.__nome = nome
        self.preço = preço
        self.quantidade = quantidade

        # Ações a serem executadas
        Item.todos.append(self)

    @property
    # Decorador Property = Atributo Somente Leitura
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        if len(valor) > 10:
            raise Exception("O nome é muito longo!")
        else:
            self.__nome = valor

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
        return f"{self.__class__.__name__}('{self.nome}', {self.preço}, {self.quantidade})"