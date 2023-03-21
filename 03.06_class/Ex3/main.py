from livro import Livro

nome = input("Digite o nome do livro: ")
qtdaPag = int(input("Digite o número de páginas: "))
autor = input("Digite o nome do autor: ")
preco = float(input("Digite o preço do livro: "))


livro_obj = Livro(nome, qtdaPag, autor, preco)
livro_obj.getpreco()
livro_obj.newpreco(preco)