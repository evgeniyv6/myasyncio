#!/usr/bin/env python

import threading
import logging
import time

class ActivePool:
    def __init__(self):
        super(ActivePool,self).__init__()
        self.active=[]
        self.lock=threading.Lock()

    def makeActive(self, name):
        with self.lock:
            self.active.append(name)
            logging.debug('Running %s', self.active)

    def makeInactive(self, name):
        with self.lock:
            self.active.remove(name)
            logging.debug('Running: %s', self.active)

def worker(s, pool):
    logging.debug('wait to join the pool')
    with s:
        name=threading.current_thread().getName()
        pool.makeActive(name)
        time.sleep(.1)
        pool.makeInactive(name)

logging.basicConfig(
    level = logging.DEBUG,
    format='%(asctime)s (%(threadName)-2s) %(message)s',
)

pool=ActivePool()
s=threading.Semaphore(2)
for i in range(4):
    t=threading.Thread(
        name=str(i),
        target=worker,
        args=(s, pool),
    )
    t.start()