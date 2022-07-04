class nodeTree:
    def __init__(self, k, v, lc=None, rc=None):
        self.key = k
        self.value = v
        self.left = lc
        self.right = rc

class binaryTree:
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

    def insert(self, x, v, p=""):
        if p == "":
            p = self.root
        if p == None:
            p = nodeTree(x, v, None, None)
        elif x<p.key:
            p.left = self.insert(x, v, p.left)
        elif x>p.key:
            p.right = self.insert(x, v, p.right)
        else:
            #return "Chave já inserida"
            raise Exception("Chave já inserida")
        return p

    def findReplacement(self, p):
        r = p.right
        while r.left != None:
            r = r.left
        return r
    def delete(self, x, p=""):
        if p == "":
            p = self.root
        if p == None:
            #return "Chave não encontrada"
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
                r = self.findReplacement(p)
                p.value = r.value
                p.key = r.key
                p.right = self.delete(r.key, p.right)
        return p
    def print2DTree(self, root, space=0, LEVEL_SPACE=5):
        if (root == None): return
        space += LEVEL_SPACE
        self.print2DTree(root.right, space)
        # print() # neighbor space
        for i in range(LEVEL_SPACE, space): print(end=" ")
        print("|" + str(root.key) + "|<")
        self.print2DTree(root.left, space)
