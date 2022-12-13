#VIDEO 6

class DataBase:
    def __init__(self):
        self.__dados = {}

    def insereCliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def listaClientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apagaCliente(self, id):
        del self.__dados['clientes'][id]

bd = DataBase()
bd.insereCliente(1, 'Otávio')
bd.insereCliente(2, 'Miranda')
bd.insereCliente(3, 'Rose')
bd.apagaCliente(2)
bd.listaClientes()