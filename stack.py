class Pilha:
    def __init__(self):
        self.dados = []

    def get(self, i):
        if i >= len(self.dados):
            return None
        else:
            return self.dados[i]

    def length(self):
        return len(self.dados)

    def push(self, x):
        self.dados.append(x)

    def pop(self):
        return self.dados.pop()

    def top(self):
        return self.dados[len(self.dados) - 1]
