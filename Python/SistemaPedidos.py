class Pedido:
    def __init__(self, ValorTotal = 0) -> None:
        self.__valorTotal = ValorTotal
        self.pedido = []
    @property
    def ValorTotal(self):
        return self.__valorTotal
    
    def AdicionarItem(self, produto, Quantidade):
        self.pedido.append(ItemPedido(produto, Quantidade))
        

    def Obter_Total(self, Quantidade, Valor):
        self.__valorTotal = ItemPedido(Quantidade * Valor)
        return self.__valorTotal

class ItemPedido:
    def __init__(self, Quantidade) -> None:
        self.__quantidade = Quantidade
        
    @property
    def Quantidade(self):
        return self.__quantidade
    
    def Item_pedido(self, Codigo, Valor, Descriçao):
        self.item_pedidos.append(Pedido(f'Produto: {Codigo, Valor, Descriçao} \nQuantidade: {self.Quantidade}'))

class Produto:
    def __init__(self, Codigo, Valor) -> None:
        self.__codigo = Codigo
        self.__valor = Valor

    @property
    def Codigo(self):
        return self.__codigo
    @property
    def Valor(self):
        return self.__valor

a = Pedido()
b = ItemPedido(3)
c = Produto('camisa', 20)

a.AdicionarItem('camisa', 5)