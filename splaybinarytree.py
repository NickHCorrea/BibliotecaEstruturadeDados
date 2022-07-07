class splaynodeTree:
    def __init__(self, k, v, lc=None, rc=None):
        self.key = k
        self.value = v
        self.left = lc
        self.right = rc
        self.parent = None


class splaybinaryTree:
    def __init__(self, rt=None):
        self.root = rt

    def zigzigLL(self, p, q, r):
        prev = r.parent
        r.left = q.right
        q.left = p.right
        p.right = q
        q.right = r

        if r.left is not None:
            r.left.parent = r
        if q.right is not None:
            q.right.parent = q
        p.parent = prev
        q.parent = p
        r.parent = q

    def zigzigRR(self, p, q, r):
        prev = r.parent
        r.right = q.left
        q.right = p.left
        p.left = q
        q.left = r

        if r.right is not None:
            r.right.parent = r
        if q.left is not None:
            q.left.parent = q
        p.parent = prev
        q.parent = p
        r.parent = q

    def zigzagLR(self, p, q, r):  # r.left = q, q.right = p
        prev = r.parent
        r.left = p.right
        q.right = p.left
        p.left = q
        p.right = r

        if r.left is not None:
            r.left.parent = r
        if q.right is not None:
            q.right.parent = q
        p.parent = prev
        q.parent = p
        r.parent = p

    def zigzagRL(self, p, q, r):  # r.right = q, q.left = p
        prev = r.parent
        r.right = p.left
        q.left = p.right
        p.right = q
        p.left = r

        if r.right is not None:
            r.right.parent = r
        if q.left is not None:
            q.left.parent = q
        p.parent = prev
        q.parent = p
        r.parent = p

    def zigL(self, p, oldRoot):
        oldRoot.left = p.left
        p.right = oldRoot

        p.right.parent = p
        p.parent = None
        # Update root
        self.root = p

    def zigR(self, p, oldRoot):
        oldRoot.right = p.right
        p.left = oldRoot

        p.left.parent = p
        p.parent = None
        # Update root
        self.root = p

    def aux_splay(self, x, p=''):
        if p == '':
            p = self.root
        if p is None:
            return p
        if p.key == x:
            return p
        elif p.key > x:
            if p.left is None:
                return p
            else:
                return self.aux_splay(x, p.left)
        elif p.key < x:
            if p.right is None:
                return p
            else:
                return self.aux_splay(x, p.right)

    def splay(self, x):
        p = self.aux_splay(x)
        if self.root is None:
            raise Exception("Empty tree")

        while p.parent is not None:
            if p.parent == self.root:
                if p == p.parent.left:
                    self.zigL(p, p.parent)
                else:
                    self.zigR(p, p.parent)

            else:
                father = p.parent
                granpa = father.parent

                if p.parent.left == p and father.parent.left == father:
                     self.zigzigLL(p, father, granpa)
                elif p.parent.right == p and father.parent.right == father:
                    self.zigzigRR(p, father, granpa)
                elif p.parent.right == p and father.parent.left == father:
                    self.zigzagLR(p, father, granpa)
                else:
                    self.zigzagRL(p, father, granpa)
        self.root = p
        self.root.parent = None
    def insert(self, x, v):
        self.root = self.aux_insert(x, v)
        self.splay(x)

    def aux_insert(self, x, v, p=""):
        if p == "":
            p = self.root
        if p is None:
            p = splaynodeTree(x,v)
        elif x < p.key:
            if p.left is None:
                p.left = splaynodeTree(x, v, None, None)
                p.left.parent = p
                return p
            else:
                p.left = self.aux_insert(x, v, p.left)
        elif x > p.key:
            if p.right is None:
                p.right = splaynodeTree(x, v, None, None)
                p.right.parent = p
                return p
            else:
                p.right = self.aux_insert(x, v, p.right)
        else:
            raise Exception("Chave já inserida")
        return p

    def print2DTree(self, root, space=0, LEVEL_SPACE=5):
        if root == None: return
        space += LEVEL_SPACE
        self.print2DTree(root.right, space)
        # print() # neighbor space
        for i in range(LEVEL_SPACE, space): print(end=" ")
        print("|" + str(root.key) + "|<")
        self.print2DTree(root.left, space)


st = splaybinaryTree()
st.insert(1, 'a')
st.insert(2, 'b')
st.insert(3, 'a')
st.insert(5, 'c')

st.insert(4, 'd')
st.insert(7, 'v')
st.insert(6, 'a')
st.insert(8, 'f')

st.insert(0, 'x')
st.print2DTree(st.root)
