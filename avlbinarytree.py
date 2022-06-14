def height(p):
    if p == None:
        return -1
    else:
        return p.height

class AVLnodeTree:
    def __init__(self, k, v, lc=None, rc=None):
        self.key = k
        self.value = v
        self.left = lc
        self.right = rc
        if self.left!= None or self.right!=None:
            self.height = max(height(self.left), height(self.right)) + 1
        else:
              self.height = 0


class AVLbinaryTree:
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
            p = AVLnodeTree(x, v, None, None)
        elif x < p.key:
            p.left = self.insert(x, v, p.left)
        elif x > p.key:
            p.right = self.insert(x, v, p.right)
        else:
            return "Chave já inserida"
        return self.rebalance(p)

    def findReplacement(self, p):
        r = p.right
        while r.left != None:
            r = r.left
        return r

    def delete(self, x, p=""):
        if p == "":
            p = self.root
        if p == None:
            return "Chave não encontrado"
        else:
            if x < p.key:
                p.left = self.delete(x, p.left)
            elif x > p.key:
                p.right = self.delete(x, p.right)
            elif p.left == None or p.right == None:
                if p.left == None:
                    return self.rebalance(p.right)
                else:
                    return self.rebalance(p.left)
            else:
                r = self.findReplacement(p)
                p.value = r.value
                p.key = r.key
                p.right = self.delete(r.key, p.right)
        return self.rebalance(p)

    def updateHeight(self, p=""):
        if p == "":
            p = self.root
        p.height = max(height(p.left), height(p.right)) + 1
    def balanceFactor(self, p=""):
        if p == "":
            p = self.root
        return height(p.right) - height(p.left)

    def rotRight(self, p=""):
        q = p.left
        p.left = q.right
        q.right = p
        self.updateHeight(p)
        self.updateHeight(q)
        return q

    def rotLeft(self, p=""):
        q = p.right
        p.right = q.left
        q.left = p
        self.updateHeight(p)
        self.updateHeight(q)
        return q

    def rotRightLeft(self, p=""):
        p.right = self.rotRight(p.right)
        return self.rotLeft(p)

    def rotLeftRight(self, p=""):
        p.left = self.rotLeft(p.left)
        return self.rotRight(p)

    def rebalance(self, p=""):
        if p == "":
            p = self.root
        if p == None:
            return p
        balanceFac = self.balanceFactor(p)
        if balanceFac < -1:
            if height(p.left.left) >= height(p.left.right):
                p = self.rotRight(p)
            else:
                p = self.rotLeftRight(p)
        elif balanceFac > 1:
            if height(p.right.right) >= height(p.right.left):
                p = self.rotLeft(p)
            else:
                p = self.rotRightLeft(p)
        self.updateHeight(p)
        return p

    def print2DTree(self, root, space=0, LEVEL_SPACE=5):
        if (root == None): return
        space += LEVEL_SPACE
        self.print2DTree(root.right, space)
        # print() # neighbor space
        for i in range(LEVEL_SPACE, space): print(end=" ")
        print("|" + str(root.key) + "|<")
        self.print2DTree(root.left, space)
