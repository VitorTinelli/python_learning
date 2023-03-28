class Animal():
    def __init__(self):
        pass

    def andar(self):
        pass

class Gato(Animal):
    def __init__(self):
        super().__init__()

    def andar(self):
        print("O gato está andando.")

class Cachorro(Animal):
    def __init__(self):
        super().__init__()

    def andar(self):
        print("O cachorro está andando.")
        