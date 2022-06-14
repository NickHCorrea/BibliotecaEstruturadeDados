class Fila:
    def __init__(self):
        self.dados = []

    def get(self, i):
        if i > len(self.dados):
            return None
        else:
            return self.dados[i]

    def length(self):
        return len(self.dados)

    def enqueue(self, x):
        self.dados.append(x)

    def dequeue(self):
        return self.dados.pop(0)
