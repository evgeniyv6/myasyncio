#!/usr/bin/env python

class _Node:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next

class Queue:
    def __init__(self):
        self._first = None
        self._last = None
        self._n = 0

    def isEmpty(self):
        return self._first is None

    def __len__(self):
        return self._n

    def dequeue(self):
        item = self._first.val
        self._first = self._first.next
        if self.isEmpty(): self._last = None
        self._n-=1
        return item

    def enqueue(self, val):
        oldLast = self._last
        self._last = _Node(val, None)
        if self.isEmpty(): self._first = self._last
        else:
            oldLast.next = self._last
        self._n+=1
