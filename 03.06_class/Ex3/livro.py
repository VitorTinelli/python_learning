class Livro:
    def __init__(self, nome, qtdaPag, autor, preco):
        self.nome = nome
        self.qtdaPag = qtdaPag
        self.autor = autor
        self.preco = preco
    
    def getpreco(self, preco):
        print("Preço antigo: ", preco)

    def newpreco(self, preco):
        preco =float(input("Digite o novo preco:"))
        print("Novo preço:", preco)