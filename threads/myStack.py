#!/usr/bin/env python

class _Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Stack:
    def __init__(self):
        self._first = None
        self._n = 0

    def isEmpty(self):
        return self._first is None

    def push(self, item):
        self._first = _Node(item, self._first)
        self._n+=1

    def pop(self):
        item = self._first.val
        self._first = self._first.next
        self._n-=1
        return item

    def __len__(self):
        return self._n

    def __repr__(self):
        res = []
        cur = self._first
        while cur:
            res.append(cur.val)
            cur = cur.next
        return str(res)

def bin_stack(n):
    bs = Stack()
    while n>0:
        bs.push(n%2)
        n//=2
    while not bs.isEmpty():
        print(bs.pop(), end='')
    print()

def classic_bin(n):
    s=''
    while n>0:
        s=str((n%2))+s
        n//=2
    return s

def parenthese(s):
    st = Stack()
    open_par = tuple('{([')
    close_par = tuple('})]')
    mapa = dict(zip(close_par, open_par))
    print(f"mapa - {mapa}")
    for p in s:
        print(f'p from string - {p}')
        if p in open_par:
            st.push(p)
            print('push ', end='')
            print(st)
        elif p in close_par and not st.isEmpty():
            if st._first.val == mapa[p]:
                print('pop ', end='')
                print(st.pop())
        else:
            return False
    return st._first is None


from timeit import timeit
if __name__ == '__main__':
    print(parenthese('[()]{}{[()()]()})'))
    #print(parenthese('[([])]'))
    # st = Stack()
    # st.push(_Node(1,2))
    # print(st.isEmpty())
    # print(st.pop())
    # print(st.isEmpty())
    # print('binary battle')
    # bin_stack(9)
    # print(classic_bin(9))

