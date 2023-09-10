#!/usr/bin/env python

import logging
import threading
import time

def wait_ev(e):
    logging.debug('wait event starting')
    ev_is_set = e.wait()
    logging.debug('ev set: {}'.format(ev_is_set))

def wait_ev_timeout(e, t):
    while not e.is_set():
        logging.debug('wait event timeout starting')
        ev_is_set = e.wait(t)
        logging.debug('event set: {}'.format(ev_is_set))
        if ev_is_set:
            logging.debug('processing event')
        else:
            logging.debug('doing other work')

logging.basicConfig(
    level = logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

e = threading.Event()
t1=threading.Thread(
    name='block',
    target=wait_ev,
    args=(e,),)
t1.start()

t2=threading.Thread(
    name='nonblock',
    target=wait_ev_timeout,
    args=(e,2),
)
t2.start()

logging.debug('Waiting before calling Event.set()')
time.sleep(.3)
e.set()
logging.debug('event is set')