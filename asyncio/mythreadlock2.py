#!/usr/bin/env python

import threading
import logging
import time

def lock_holder(lock):
    logging.debug('Starting')
    while 1:
        lock.acquire()
        try:
            logging.debug('Holding')
            time.sleep(.5)
        finally:
            logging.debug('Not holding')
            lock.release()
        time.sleep(.5)

def worker(lock):
    logging.debug('Starting')
    num_tries = 0
    num_acquire = 0
    while num_acquire<3:
        time.sleep(.5)
        logging.debug('Try to acquire')
        have_it = lock.acquire(0) # 0 to check if another thread have lock without stop current thread
        try:
            num_tries+=1
            if have_it:
                logging.debug('Iter %d: Acquire', num_tries)
                num_acquire +=1
            else:
                logging.debug('Iter %d: Not acquire', num_tries)
        finally:
            if have_it: lock.release()
    logging.debug('Done after %d iters', num_tries)


logging.basicConfig(
    level = logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

lock=threading.Lock()
holder=threading.Thread(
    name='lock holder',
    target=lock_holder,
    args=(lock,),
    daemon=True,
)
holder.start()

worker=threading.Thread(
    name='Worker',
    target=worker,
    args=(lock,),
)

worker.start()


# infinite cycle
# main_thread = threading.main_thread()
# for t in threading.enumerate():
#     if t is not main_thread: t.join()