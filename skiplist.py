import random


class Nil:
    def __init__(self):
        self.key = float('inf')
        self.value = None


nil = Nil()


class SkipListNode:
    def __init__(self, k, v, l):
        self.key = k
        self.value = v
        self.level = l
        self.next = [nil] * l


class SkipList:
    def __init__(self):
        self.maxLevel = 5
        self.head = SkipListNode(float('-inf'), None, self.maxLevel)

    def find(self, x):
        p = self.head
        level = self.maxLevel - 1
        while level >= 0:
            if p.next[level].key == x:
                return True
            if p.next[level].key < x:
                p = p.next[level]
            else:
                level = level - 1
        return False

    def createLevel(self):
        level = 0
        while random.random() < 0.5 and level < self.maxLevel -1 :
            level += 1
        print(level)
        return level

    def insert(self, x, v):
        p = self.head
        update = [nil] * self.maxLevel
        level = p.level - 1
        while level >= 0:
            if p.next[level].key == x:
                raise ("Chave já inserida")
            if p.next[level].key < x:
                p = p.next[level]
            else:
                update[level] = p
                level = level - 1
        newLevel = self.createLevel() + 1
        newNode = SkipListNode(x, v, newLevel)
        if newLevel == 0:
            newNode.next[0] = update[0].next[0]
            update[0].next[0] = newNode
        else:
            for i in range(newLevel):
                newNode.next[i] = update[i].next[i]
                update[i].next[i] = newNode

    def displayList(self):
        print("\n*****Skip List******")
        head = self.head
        for lvl in range(self.maxLevel):
            print("Level {}: ".format(lvl), end=" ")
            node = head.next[lvl]
            while not isinstance(node, Nil):
                print(node.key, end=" ")
                node = node.next[lvl]
            print("")


Mysl = SkipList()
Mysl.insert(2, "b")
Mysl.insert(3, "b")
Mysl.insert(4, "b")
Mysl.insert(6, "b")
print(Mysl.find(1))

Mysl.displayList()  
