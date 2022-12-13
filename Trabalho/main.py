from book import book

livro = book("Pequeno Principe", "Antoine de Saint-Exupéry", 20.50, 1943)                             #CREATE
#livro = book(input('Insira o nome: '),                                                               CREATE 2
# input('Insira o autor: '), input('Insira o preço: '), input("Insira o ano de lançamento: "))
livro.exibeLivro()                                                                                    #READ

escolha  = int(input('\n\nDeseja alterar os dados? 1 Sim 2 Não: '))     #Inicialmente foi um pouco dificil 
                                                                        #entender esta estrutura por acontecer 
                                                                        #diversas coisas em sequencia


if escolha == 1:            #Em python não é necessario usar "{}" para identar funções,
                            #nem ";" no final da maioria das linhas e também não é necessario
                            #Explicitar o tipo de uma variavel primitiva o que pode confundir em códigos
                            #Mais complexos
    livro.atualizaDados()                                                                             #UPDATE
    livro.exibeLivro()

escolha  = int(input('\n\nDeseja deletar os dados? 1 Sim 2 Não: '))
if escolha == 1:
    livro.deletaDados()                                                                               #DELETE
    print("O objeto foi deletado")  #Para fazer um print em Python é mais rapido e simples