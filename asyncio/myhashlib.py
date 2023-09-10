#!/usr/bin/env python

import hashlib

# print(hashlib.algorithms_guaranteed)
# print(hashlib.algorithms_available)

import multiprocessing
import time
import sys
import logging

## ex1
def worker(i):
    print('Worker', i)

# ex2
def daemon():
    p = multiprocessing.current_process()
    print('Starting: ', p.name, p.pid)
    sys.stdout.flush()
    time.sleep(2)
    print('Exiting: ', p.name, p.pid)
    sys.stdout.flush()
# ex2
def non_daemon():
    p = multiprocessing.current_process()
    print('Starting: ', p.name, p.pid)
    sys.stdout.flush()
    time.sleep(2)
    print('Exiting: ', p.name, p.pid)
    sys.stdout.flush()

# ex 3
class worker(multiprocessing.Process):
    def run(self):
        print('IN {}'.format(self.name))
        return

if __name__=='__main__':
    # ex1
    # jobs=[]
    # for i in range(5):
    #     p = multiprocessing.Process(target=worker, args=(i,))
    #     jobs.append(p)
    #     p.start()

    # # ex2
    # d = multiprocessing.Process(name='daemon', target=daemon,)
    # d.daemon = True
    # nd = multiprocessing.Process(name='non_daemon', target=non_daemon,)
    # nd.daemon=False
    # d.start()
    # time.sleep(1)
    # nd.start()
    #
    # d.join() # to wait process end
    # nd.join(5) # 5 sec timeout

    # ex 3
    jobs=[]
    for i in range(3):
        p = worker()
        jobs.append(p)
        p.start()
    for j in jobs: j.join()