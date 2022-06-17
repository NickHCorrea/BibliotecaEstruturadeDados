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
    def aux_splay(self, x, p=''):
        if p=='':
            p = self.root
        if isinstance(p, Nil):
            return p
        if p.key == x:
            return p
        elif p.key > x:
            if isinstance(p.left, Nil):
                return p
            else:
                return self.aux_splay(x, p.left)
        elif p.key < x:
            if isinstance(p.right, Nil):
                return p
            else:
                return self.aux_splay(x, p.right)
    def splay(self, x):
        p = self.aux_splay(x)
        if isinstance(p, Nil):
            raise ("Árvore vazia")
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

    def find(self, x):
        self.splay(x)
        if isinstance(self.root, Nil):
            raise ("Árvore vazia")
        elif self.root.key == x:
            return self.root.value
        else:
            return False

    def insert(self, x, v):
        if isinstance(self.root, Nil):
            self.root = splaynodeTree(x, v)
        else:
            self.splay(x)
            print(x)
            self.print2DTree(self.root)
            if self.root.key == x:
                raise ("Chave já inserida")
            if self.root.key > x:
                newNode = splaynodeTree(x, v)
                oldRoot = self.root
                self.root = newNode
                self.root.right = oldRoot
            else:
                newNode = splaynodeTree(x, v)
                oldRoot = self.root
                self.root = newNode
                self.root.left = oldRoot

    def delete(self, x):
        self.splay(x)
        if isinstance(self.root, Nil):
            raise ("Árvore vazia")
        else:
            if self.root.key == x:
                if isinstance(self.root.left, Nil) or isinstance(self.root.right, Nil):
                    if isinstance(self.root.left, Nil):
                        return self.root.right
                    else:
                        return self.root.left
                else:
                    newRoot = self.root.right.splay(x)
                    oldChild = self.root.left
                    self.root = newRoot
                    self.root.left = oldChild

    def print2DTree(self, root, space=0, LEVEL_SPACE=5):
        if isinstance(root, Nil): return
        space += LEVEL_SPACE
        self.print2DTree(root.right, space)
        # print() # neighbor space
        for i in range(LEVEL_SPACE, space): print(end=" ")
        print("|" + str(root.key) + "|<")
        self.print2DTree(root.left, space)


st = splaybinaryTree()
st.insert(1, 'a')
st.insert(2, 'b')
st.insert(0, 'z')
st.insert(3, 'a')
st.insert(5, 'c')
st.insert(4, 'd')
