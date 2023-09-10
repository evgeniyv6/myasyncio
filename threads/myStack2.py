

class Node:
    def __init__(self, item= 0, next = None):
        self.item = item
        self.next = next

class Stack:
    def __init__(self):
        self.first = None

    def isEmpty(self):
        return self.first is None

    def push(self, val):
        self.first = Node(val, self.first)

    def pop(self):
        old = self.first.item
        self.first = self.first.next
        return old

class Print_Link:
    def __init__(self, ll, res = None):
        self.ll = ll
        if res is None: self.res = []
        else: self.res = res

    @classmethod
    def print_link(cls, ll, res = None):
        if res is None: res  = []
        while ll:
            res.append(ll.item)
            ll = ll.next
        return cls(ll, res)

    def __repr__(self):
        return f'Link is {self.res}'

import math

def math_alg(expr):
    ops = Stack()
    values = Stack()
    ops_signs = ('*', '+', '-', 'sqrt')
    for s in expr:
        if s in ops_signs: ops.push(s)
        elif s == ')':
            op = ops.pop()
            val = values.pop()
            if op == '+': val = val + values.pop()
            elif op == '-': val = val - values.pop()
            elif op == '*': val = val * values.pop()
            elif op == 'sqrt': val = math.sqrt(val)
            values.push(val)
        elif s != '(':
            values.push(float(s))
    return values.pop()


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.n = 0

    def isEmpty(self):
        return self.first is None

    def __len__(self):
        return self.n

    def dequeue(self):
        old = self.first.item
        self.first = self.first.next
        if self.isEmpty(): self.last = None
        self.n -=1
        return old

    def enqueue(self, item):
        oldVal = self.last
        self.last = Node(item, None)
        if self.isEmpty(): self.first = self.last
        else: oldVal.next = self.last
        self.n+=1



if __name__=='__main__':
    st = Stack()
    st.push(1)
    st.push(5)
    st.push(9)
    # st.pop()
    while st.first: print(st.first.item); st.first=st.first.next
    print(math_alg('(1+((2+3)*(4*5)))'))
    print(math_alg('(1+((2+3)+2))'))

