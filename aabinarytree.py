class Nil:
    def __init__(self):
        self.level = 0
        self.right = self
        self.left = self


nil = Nil()


class AAnodeTree:
    def __init__(self, k, v, lc=nil, rc=nil):
        self.key = k
        self.value = v
        self.left = lc
        self.right = rc
        self.level = 1


class AAbinaryTree:
    def __init__(self, rt=nil):
        self.root = rt

    def find(self, x, p=""):
        if p == "":
            p = self.root
        while not (isinstance(p, Nil)):
            if x < p.key:
                return self.find(x, p.left)
            if x > p.key:
                return self.find(x, p.right)
            else:
                return p.value
        return "Chave não encontrada"

    def split(self, p):
        if isinstance(p, Nil) or isinstance(p.right, Nil):
            return p
        else:
            if p.right.right.level == p.level:
                print('split')
                q = p.right
                p.right = q.left
                q.left = p
                q.level += 1
                return q
            else:
                return p

    def skew(self, p):
        if p.left.level == p.level:
            print('skew')
            q = p.left
            p.left = q.right
            q.right = p
            return q
        else:
            return p

    def insert(self, x, v, p=""):
        if p == "":
            p = self.root
        if isinstance(p, Nil):
            p = AAnodeTree(x, v, nil, nil)
        elif x < p.key:
            p.left = self.insert(x, v, p.left)
        elif x > p.key:
            p.right = self.insert(x, v, p.right)
        else:
            return "Chave já inserida"
        return self.split(self.skew(p))

    def updateLevel(self, p):
        idealLevel = 1 + min(p.left.level, p.right.level)
        if p.level > idealLevel:
            p.level = idealLevel
        if p.right.level > idealLevel:
            p.right.level = idealLevel
        return p

    def fixupAfterDelete(self, p):
        print('fix')
        p = self.updateLevel(p)
        self.print2DTree(self.root)
        p = self.skew(p)
        self.print2DTree(self.root)
        p.right = self.skew(p.right)
        self.print2DTree(self.root)
        p.right.right = self.skew(p.right.right)
        self.print2DTree(self.root)
        p = self.split(p)
        self.print2DTree(self.root)
        p.right = self.split(p.right)
        self.print2DTree(self.root)

        return p

    def findleftReplacement(self, p):
        p = p.left
        while not (isinstance(p.right, Nil)):
            p = p.right
        return p

    def findrightReplacement(self, p):
        p = p.right
        while not (isinstance(p.left, Nil)):
            p = p.left
        return p

    def delete(self, x, p=""):
        if p == "":
            p = self.root
        if isinstance(p, Nil):
            return "Chave não encontrada"
        else:
            if x < p.key:
                p.left = self.delete(x, p.left)
            elif x > p.key:
                p.right = self.delete(x, p.right)
            else:
                if isinstance(p.left, Nil) and isinstance(p.right, Nil):
                    return Nil()
                elif isinstance(p.left, Nil):
                    r = self.findrightReplacement(p)
                    p.value = r.value
                    p.key = r.key
                    p.right = self.delete(r.key, p.right)
                else:
                    r = self.findleftReplacement(p)
                    p.value = r.value
                    p.key = r.key
                    p.left = self.delete(r.key, p.left)
        return self.fixupAfterDelete(p)

    def print2DTree(self, root, space=0, LEVEL_SPACE=5):
        if isinstance(root, Nil): return
        space += LEVEL_SPACE
        self.print2DTree(root.right, space)
        # print() # neighbor space
        for i in range(LEVEL_SPACE, space): print(end=" ")
        print("|" + str(root.level) + "|<")
        self.print2DTree(root.left, space)
