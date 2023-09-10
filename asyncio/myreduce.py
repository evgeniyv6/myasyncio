#!/usr/bin/env python

import functools

def do_reduce(a,b):
    print('reduce ({}, {})'.format(a,b))
    return a+b

data=range(1,5)

print(data)
res=functools.reduce(do_reduce, data, 100)
print('res: {}'.format(res))

def mm(x):
    return (x,2+x)
for i in map(mm,range(3)): print (i)

print('-'*30)
from itertools import *
for i in zip(count(),('a', 'b')): print(i)

for j, s in zip(count(), repeat('over and over', 5)): print(j,s)