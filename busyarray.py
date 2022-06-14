class busyArray:
    def __init__(self, n, v):
        self.definedIndex = Pilha()
        self.stackIndex = [0] * n
        self.data = [0] * n
        self.v = v
        self.top = 0

    def isDefined(self, i):
        if self.stackIndex[i] <= self.top:
            if self.definedIndex.get(self.stackIndex[i]) == i:
                return 1
        return 0

    def define(self, i):
        self.definedIndex.push(i)
        self.top = self.definedIndex.top()
        self.stackIndex[i] = self.definedIndex.length()-1

    def get(self, i):
        if self.isDefined(i):
            return self.data[i]
        else:
            return self.v

    def set(self, i, x):
        if self.isDefined(i):
            self.data[i] = x
        else:
            self.define(i)
            self.data[i] = x
