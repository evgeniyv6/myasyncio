#!/usr/bin/env python

import functools
import inspect
from pprint import pprint

@functools.total_ordering
class MyObject:
    def __init__(self, val):
        self.val=val

    def __eq__(self, other):
        print('\ttesting __eq__({}, {})'.format(self.val, other.val))
        return self.val == other.val
    def __gt__(self, other):
        print('\ttesting __gt__({}, {})'.format(self.val, other.val))
        return self.val > other.val

print('Methods:\n')
pprint(inspect.getmembers(MyObject, inspect.isfunction))

a=MyObject(1)
b=MyObject(2)

print('\nCompares:')
for expr in ['a<b', 'a<=b', 'a==b', 'a>=b', 'a>b']:
    print('\n{:<6}'.format(expr))
    res=eval(expr)
    print('\tresult of {}: {}'.format(expr, res))