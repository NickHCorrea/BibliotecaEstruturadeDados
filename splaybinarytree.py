class Nil:
    def __init__(self):
        self.right = self
        self.left = self


nil = Nil()


class splaynodeTree:
    def __init__(self, k, v, lc=nil, rc=nil):
        self.key = k
        self.value = v
        self.parent = nil
        self.left = lc
        self.right = rc


class splaybinaryTree:
    def __init__(self, rt=nil):
        self.root = rt

    def rotRight(self, p):
        q = p.left
        p.left = q.right
        q.right = p
        q.parent = p.parent
        q.left.parent = q
        q.right.parent = q
        return q

    def rotLeft(self, p):
        q = p.right
        p.right = q.left
        q.left = p
        q.parent = p.parent
        q.left.parent = q
        q.right.parent = q
        return q

    def splay(self, p=""):
        if p == "":
            p = self.root
        while not isinstance(p.parent, Nil):
            if p.parent == self.root:
                if self.root.left == p:
                    newParent = p.parent.parent
                    p.parent = self.rotRight(p.parent)
                    p.parent = newParent
                else:
                    newParent = p.parent.parent
                    p.parent = self.rotLeft(p.parent)
                    p.parent = newParent
            elif p.parent.left == p and p.parent.parent.left == p.parent:  # Left Left grandkid - zig zig
                newParent = p.parent.parent.parent
                p.parent.parent = self.rotRight(p.parent.parent)
                p.parent = self.rotRight(p.parent)
                p.parent = newParent
            elif p.parent.right == p and p.parent.parent.right == p.parent:  # right right grandkid - zig zig
                newParent = p.parent.parent.parent
                p.parent.parent = self.rotLeft(p.parent.parent)
                p.parent = self.rotLeft(p.parent)
                p.parent = newParent
            elif p.parent.right == p and p.parent.parent.left == p.parent:  # left right grandkid - zig zag
                newParent = p.parent.parent.parent
                p.parent = self.rotLeft(p.parent)
                p.parent.parent = self.rotRight(p.parent.parent)
                p.parent = newParent
            elif p.parent.left == p and p.parent.parent.right == p.parent:  # right left grandkid - zig zag
                newParent = p.parent.parent.parent
                p.parent = self.rotRight(p.parent)
                p.parent.parent = self.rotLeft(p.parent.parent)
                p.parent = newParent
        return p
    def find(self, x, p=""):
        if p == "":
            p = self.root
        if x < p.key:
            return self.find(x, p.left)
        if x > p.key:
            return self.find(x, p.right)
        else:
            if x == p.key:
                self.splay(p)
                return p
            else:
                return None

    def insert(self, x, v, p=""):
        if p == "":
            if isinstance(self.root, Nil):
                self.root = splaynodeTree(x, v)
            else:
                p = self.root
                return self.insert(x, v, p)

        elif x < p.key:
            if not isinstance(p.left, Nil):
                p.left = self.insert(x, v, p.left)
            else:
                p.left = splaynodeTree(x, v)
                p.left.parent = p
                return self.splay(p.left)
        elif x > p.key:
            if not isinstance(p.right,Nil):
                p.right = self.insert(x, v, p.right)
            else:
                p.right = splaynodeTree(x, v)
                p.right.parent = p
                return self.splay(p.right)
        else:
            return "Chave já inserida"

    def findReplacement(self, p):
        r = p.right
        while r.left != None:
            r = r.left
        return r

    def delete(self, x, p=""):
        if p == "":
            p = self.root
        if p == None:
            return "Chave não encontrada"
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
        if isinstance(root,Nil): return
        space += LEVEL_SPACE
        self.print2DTree(root.right, space)
        # print() # neighbor space
        for i in range(LEVEL_SPACE, space): print(end=" ")
        print("|" + str(root.key) + "|<")
        self.print2DTree(root.left, space)


st = splaybinaryTree()
st.insert(1, 'a')
st.root = st.insert(2, 'b')
st.root = st.insert(0, 'x')

