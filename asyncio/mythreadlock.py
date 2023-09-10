#!/usr/bin/env python

import threading
import logging
import time
import random

class Counter:
    def __init__(self, start=0):
        self.lock = threading.Lock()
        self.value = start

    def increment(self):
        logging.debug('wait lock')
        self.lock.acquire()
        try:
            logging.debug('Acquire lock')
            self.value += 1
            logging.debug(self.value)
        finally:
            self.lock.release()

def worker(c):
    for i in range(2):
        pause = random.random()
        logging.debug('sleep %0.02f', pause)
        time.sleep(pause)
        c.increment()
    logging.debug('Done')

logging.basicConfig(
    level = logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

counter=Counter()
for i in range(2):
    t= threading.Thread(target=worker, args=(counter,),)
    t.start()

logging.debug('wait for worker thread')
main_thread = threading.main_thread()
for t in threading.enumerate():
    if t is not main_thread: t.join()
logging.debug('Counter %d', counter.value)