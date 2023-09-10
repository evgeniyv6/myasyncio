class Node:
    def __init__(self, item = 0, next = None):
        self.item = item
        self.next = next


class Stack:
    def __init__(self):
        self.first = None
        self.n = 0

    def isEpmty(self):
        return self.first is None

    def push(self, item):
        self.first = Node(item, self.first)
        self.n +=1

    def pop(self):
        old = self.first.item
        self.first = self.first.next
        self.n -=1
        return old

    def __len__(self):
        return self.n

    def __repr__(self):
        res = []
        cur = self.first
        while cur:
            res.append(cur.item)
            cur = cur.next
        return str(res)

    def get_max(self, l = None):
        if l is None: l = self.first
        if l is None: return None
        elif l.next is None: return l.item
        else:
            return max(l.item, self.get_max(self.first.next))

    def get_min(self, l = None):
        if l is None: l = self.first
        if l is None: return None
        elif l.next is None: return l.item
        else:
            return min(l.item, self.get_min(self.first.next))

    def reverse(self, l: Node = None):
        if l is None: l = self.first
        if l is None: return None
        elif l.next is None: return l
        second = l.next
        rev = self.reverse(second)
        second.next = l
        l.next = None
        return rev


    def insert_after(self, l: Node):
        l.next = self.first.next
        self.first.next = l

class Queue(Stack):
    def __init__(self):
        self.first = self.last = None
        self.n =0

    def isEmpty(self):
        return self.first is None

    def dequeue(self):
        item = self.first.item
        self.first = self.first.next
        if self.isEpmty(): self.last = None
        self.n -=1
        return item

    def enqueue(self, item):
        old = self.last
        self.last = Node(item, None)
        if self.isEpmty(): self.first = self.last
        else: old.next = self.last
        self.n+=1


class PrintLink:
    def __init__(self, l: Node, res = None):
        self.l = l
        if res is None: self.res = []
        else: self.res = res

    @classmethod
    def print_link(cls, l: Node, res: list = None):
        if res is None: res = []
        cur =l
        while cur:
            res.append(cur.item)
            cur = cur.next
        return cls(l, res)

    def __repr__(self):
        return f'Link list is {self.res}'


if __name__=='__main__':
    st=Stack()
    st.push(1);st.push(5);st.push(9);st.pop()
    print(st)
    print(len(st))
    print(st.get_max())
    print(st.get_min())
    print('-'*10)
    q = Queue()
    q.enqueue(1)
    q.enqueue(3)
    q.enqueue(9)
    q.dequeue()
    print(q)
    print(len(q))
    print(q.get_min())
    print(q.get_max())
    print('-'*10)
    myl = Node(1, Node(3, Node(5)))
    print(PrintLink.print_link(myl))

    myl2 = Node(1, Node(2, Node(3)))
    myl3 = Node(4, Node(5, Node(6)))

    mySt2 = Stack()
    mySt2.push(1); mySt2.push(2); mySt2.push(3)
    print(mySt2)
    mySt2.insert_after(myl3)
    print(mySt2)
    print('-'*10)
    print(PrintLink.print_link(mySt2.reverse()))