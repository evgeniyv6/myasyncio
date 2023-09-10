#!/usr/bin/env python

import threading
import logging
import time

def consumer(cond):
    logging.debug('Start consumer thread')
    with cond:
        cond.wait()
        logging.debug('resource is available to consumer')

def producer(cond):
    logging.debug('Start producer thread')
    with cond:
        logging.debug('Make resourse available')
        cond.notifyAll()

logging.basicConfig(
    level = logging.DEBUG,
    format='%(asctime)s (%(threadName)-2s) %(message)s',
)


condition = threading.Condition()
c1= threading.Thread(
    name='c1',
    target=consumer,
    args=(condition,),
)
c2=threading.Thread(
    name='c2',
    target=consumer,
    args=(condition,),
)

p=threading.Thread(
    name='p',
    target=producer,
    args=(condition,),
)

c1.start()
time.sleep(.2)
c2.start()
time.sleep(.2)
p.start()



