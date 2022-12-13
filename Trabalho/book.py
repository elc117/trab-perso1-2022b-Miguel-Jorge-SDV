class book:                 #Não precisa declarar as variaveis antes das funções
    def __init__(self, nomeLivro, autor, preco, anoLancamento):     #__init__ é a palavra reservada para
        self.nomeLivro = nomeLivro                                  #ser o construtor da classe, também é
        self.autor = autor                                          #declarado as variaves aqui
        self.preco = preco
        self.anoLancamento = anoLancamento

    def getNomeLivro(self):                 #"self" é uma palavra reservada com função similar ao "this"
        return self.nomeLivro

    def setNomeLivro(self, novoNome):
        self.nomeLivro = novoNome

    def getAutor(self):
        return self.autor

    def setAutor(self, novoAutor):
        self.autor = novoAutor

    def getPreco(self):
        return self.preco

    def setPreco(self, novoPreco):
        self.preco = novoPreco

    def getAnoLancamento(self):
        return self.anoLancamento

    def setAnoLancamento(self, novoAno):
        self.anoLancamento = novoAno

    def exibeLivro(self):
        print('\n\nNome:', self.getNomeLivro(),'\nautor:', self.getAutor(), '\npreço:', self.getPreco(), '\nano de lançamento:' , self.getAnoLancamento())

    def atualizaDados(self):
        self.setNomeLivro(input('Insira o nome: '))
        self.setAutor(input('Insira autor: '))
        self.setPreco(input('Insira o preço: '))
        self.setAnoLancamento(input('Insira o ano de lançamento: '))

    def deletaDados(self):          #Para deletar os dados aparentemente é bem simples
        del self.nomeLivro
        del self.autor
        del self.preco
        del self.anoLancamento