#!/usr/bin/env python

import threading, time
import logging

logger = logging.basicConfig(
    level=logging.DEBUG,
    format='%(threadName)-10s %(message)s',
)

def daemon():
    print('Daemon Starting..')
    time.sleep(.2)
    print('Daemon Complete')

def non_daemon():
    print('NonDaemon Starting...')
    time.sleep(.1)
    print('NonDaemon complete')

t1 = threading.Thread(name='daemon',target=daemon, daemon=True)
t2=threading.Thread(name = 'nondaemon',target=non_daemon)
t1.start()
t2.start()
main_thread = threading.main_thread()
for th in threading.enumerate():
    if th==main_thread: continue
    else:
        th.join()

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
lil = ListNode(3,2)
print(lil.val, lil.next)


# [0,1,2,2,3,0,4,2], val = 2

def del_val(l,v):
    for e in l:
        if e==v:
            l.pop(l.index(e))
            del_val(l,v)
ll =[0,1,2,2,3,0,4,2]
# del_val(ll, 2)
# print(ll)

def llinl(l):
    newl=[]
    for e in l:
        if e not in newl: newl.append(e)
    return newl
print('---')
#print(llinl(ll))
from collections import OrderedDict
def llorder(l):
    return list(OrderedDict.fromkeys(l))
print(llorder([1,1,2]))


def find_needle(haystack, needle):
    for e in range(0, len(haystack) - len(needle) + 1):
        if haystack[e:e+len(needle)] == needle:
            return e
    return -1

print(find_needle('aaa', 'baa'))

def find_undex(l, n):
    maxv=0
    try:
        return l.index(n)
    except ValueError:
        for e in l:
            if n-e > 0:
                maxv+=1
            else:
                maxv +=0
        return maxv
print('['*46)
print(find_undex([1,2,3],5))