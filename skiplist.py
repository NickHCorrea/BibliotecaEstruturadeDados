class Nil:
    def __init__(self):
        self.key = float('inf')
        self.value = None

nil = Nil()

class SkipListNode:
    def __init__(self, k, v, l):
        self.key = k
        self.value = v
        self.next = [nil] * l


class SkipList:
    def __init__(self):
        self.maxLevel = 5
        self.head = SkipListNode(float('-inf'), None, self.maxLevel)

    def find(self, x, p=""):
        if p == "":
            p = self.head
        level = self.maxLevel
        while level >= 0:
            if p.next[level].key == x:
                return True
            if p.next[level].key < x:
                p = p.next[level]
                return self.find(x, p)
            else:
                level = level-1

    def createLevel(self):
        level = 0
        while random.random() < 0.5:
            level += 1
        if level > self.maxLevel - 1:
            return self.maxLevel
        return level

    def insert(self, x, v, p="", l=0):
        if p == "":
            p = self.head
        level = self.maxLevel
        while level >= 0:
            if p.next[level].key == x:
                raise("Chave já inserida")
            if p.next[level].key < x:
                p = p.next[level]
                return self.insert(x, v, p)
            else:
                level = level - 1
        newNode = SkipListNode(x, v, self.createLevel())
