class Autor:
    def __init__(self, autor) -> None:
        self.__autor = autor
    @property
    def autor(self):
        return self.__autor
    @autor.setter
    def autor(self, b):
        raise ValueError("Você não pode alterar o valor manualmente")    

class Livro(Autor):
    def __init__(self, autor, nome, qtdaPag, preco) -> None:
        super().__init__(autor)
        self.nome = nome
        self.qtdaPag = qtdaPag
        self.preco = preco
    
    def getpreco(self, preco):
        print("Preço antigo: ", preco)

    def newpreco(self, preco):
        preco =float(input("Digite o novo preco:"))
        print("Novo preço:", preco)