from item import Item

class Telefone(Item):
    def __init__(self, nome: str, preço: float, quantidade=0, telefones_quebrados=0):
        # Chamada para a função super para ter acesso a todos os atributos/métodos
        super().__init__(nome, preço, quantidade)

        # Executar validações nos argumentos recebidos
        assert telefones_quebrados >= 0, f"Telefones quebrados {telefones_quebrados} não é maior ou igual a zero!"

        # Atribuir ao objeto self
        self.telefones_quebrados = telefones_quebrados