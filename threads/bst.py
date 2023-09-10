import time
class Node:
    def __init__(self, k, v):
        self.k = k
        self.v = v
        self.l = None
        self.r = None

class BST:
    def __init__(self):
        self.root = None
        self.n = 0

    def set(self, x, k, v):
        if x is None: x = Node(k, v)
        if k < x.k: x.l = self.set(x.l, k, v)
        elif k > x.k: x.r = self.set(x.r, k, v)
        else: x.v = v
        return x

    def __setitem__(self, k, v):
        self.root = self.set(self.root, k, v)
        self.n +=1

    def __len__(self):
        return self.n

    def get(self, x, k):
        if x is None: return KeyError
        if k < x.k: return self.get(x.l, k)
        elif k > x.k: return self.get(x.r, k)
        else: return x.v

    def __getitem__(self, k):
        return self.get(self.root, k)

    def inorder(self, x, a):
        if x is None: return
        self.inorder(x.l, a)
        a+=[x.k]
        self.inorder(x.r, a)

    def preorder(self,x, a):
        if x is None: return
        a+=[x.k]
        self.preorder(x.l, a)
        self.preorder(x.r, a)

    def postorder(self,x , a):
        if x is None: return
        self.postorder(x.l, a)
        self.postorder(x.r, a)
        a+=[x.k]

    def __iter__(self):
        a=[]
        self.preorder(self.root, a)
        return iter(a)

    def get_min(self,x):
        cur = x
        while cur.l is not None:
            cur = cur.l
        return cur.k


    def min(self):
        return self.get_min(self.root)

    def get_max(self, x):
        cur =x
        while cur.l is not None: cur=cur.r
        return cur.k

    def max(self):
        return self.get_max(self.root)

if __name__=='__main__':
    '''
    pre:
    1 -> 4
    2 -> 5
    3 -> 6
    '''
    b = BST()
    b[2]=4309
    b[1]=3874324
    b[3]=3284763284768
    for k in b: print(f'{k} -> {b[k]}')
    print(list(b))
    print(b.min())
    print(b.max())
    print(f'len - {len(b)}')