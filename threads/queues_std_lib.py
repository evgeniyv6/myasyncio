#!/usr/bin/env python

import queue

q=queue.Queue()
for i in range(5): q.put(i)
while not q.empty():
    print(q.get(), end=' ')

print()

lq=queue.LifoQueue()
for i in range(5): lq.put(i)
while not lq.empty():
    print(lq.get(), end=' ')

print()
import functools, threading, time

@functools.total_ordering
class Job:
    def __init__(self, prior, descr):
        self.prior = prior
        self.descr = descr
        print('New job: ', descr)
        return

    def __eq__(self, other):
        try:
            return self.prior == other.prior
        except AttributeError:
            return NotImplemented

    def __lt__(self, other):
        try:
            self.prior < other.prior
        except AttributeError:
            return NotImplemented

pq=queue.PriorityQueue()
pq.put(Job(3,'Middle'))
pq.put(Job(10,'Junior'))
pq.put(Job(1,'Senior'))

def process_job(dpq):
    while 1:
        next_job = dpq.get()
        print('Processing job:', next_job.descr)
        time.sleep(.2)
        dpq.task_done()

workers = [
    threading.Thread(target=process_job, args=(pq,)),
    threading.Thread(target=process_job, args=(pq,)),
]

for w in workers:
    w.setDaemon(True)
    w.start()

pq.join()