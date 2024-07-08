# Quando usar métodos de classe e quando usar métodos estáticos?

class Item:
    @staticmethod
    def e_inteiro():
        '''
        Isso deve fazer algo que tenha relação
        com a classe, mas não algo que precise ser único
        por instância!
        '''
    @classmethod
    def instanciar_de_algo(cls):
        '''
        Isso também deve fazer algo que tenha relação
        com a classe, mas geralmente, são usados para
        manipular diferentes estruturas de dados para instanciar
        objetos, como fizemos com CSV.
        '''

# A ÚNICA DIFERENÇA ENTRE ELES:
# Métodos estáticos não passam a referência do objeto como o primeiro argumento nos bastidores!

# OBSERVAÇÃO: No entanto, eles também podem ser chamados a partir de instâncias.

item1 = Item()
item1.e_inteiro()
item1.instanciar_de_algo()