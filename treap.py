import random

from pygments.lexers import math


class TreapnodeTree:
    def __init__(self, k, v, pr, lc=None, rc=None):
        self.key = k
        self.value = v
        self.priority = pr
        self.left = lc
        self.right = rc


class TreapbinaryTree:
    def __init__(self, rt=None):
        self.root = rt

    def find(self, x, p=""):
        if p == "":
            p = self.root
        while p != None:
            if x < p.key:
                return self.find(x, p.left)
            if x > p.key:
                return self.find(x, p.right)
            else:
                return p.value
        return None

    def rotRight(self, p=""):
        q = p.left
        p.left = q.right
        q.right = p
        return q

    def rotLeft(self, p=""):
        q = p.right
        p.right = q.left
        q.left = p
        return q

    def insert(self, x, v, p=""):
        if p == "":
            p = self.root
        if p == None:
            p = TreapnodeTree(x, v, random.random(), None, None)
        elif x < p.key:
            p.left = self.insert(x, v, p.left)
            if p.left and p.left.priority > p.priority:
                p = self.rotRight(p)
        elif x > p.key:
            p.right = self.insert(x, v, p.right)
            if p.right and p.right.priority > p.priority:
                p = self.rotLeft(p)
        else:
            raise Exception("Chave já inserida")
        return p

    def delete(self, x, p=""):
        if p == "":
            p = self.root
        if p == None:
            raise Exception("Chave não encontrada")
        else:
            if x < p.key:
                p.left = self.delete(x, p.left)
            elif x > p.key:
                p.right = self.delete(x, p.right)
            elif p.left == None or p.right == None:
                if p.left == None:
                    return p.right
                else:
                    return p.left
            else:
                if p.left.priority < p.right.priority:
                    p = self.rotLeft(p)
                    p.left = self.delete(x, p.left)
                else:
                    p = self.rotRight(p)
                    p.right = self.delete(x, p.right)

        return p

    def print2DTree(self, root, space=0, LEVEL_SPACE=5):
        if (root == None): return
        space += LEVEL_SPACE
        self.print2DTree(root.right, space)
        # print() # neighbor space
        for i in range(LEVEL_SPACE, space): print(end=" ")
        print("|" + str(root.key) + ',' + str(root.priority) + "|<")
        self.print2DTree(root.left, space)
