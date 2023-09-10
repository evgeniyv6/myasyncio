#!/usr/bin/env python

import threading
import time
import logging

def worker():
    # print(i,'\tMyWorker\n')
    #print(threading.current_thread().getName(),'Starting') -> change on the next line
    logging.debug('Starting')
    time.sleep(.2)
    # print(threading.current_thread().getName(), 'Exit')
    logging.debug('Exit')

def my_serv():
    # print(threading.current_thread().getName(),'Starting')
    logging.debug('Starting')
    time.sleep(.3)
    # print(threading.current_thread().getName(), 'Exit')
    logging.debug('Exit')

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
)

def mydaemon():
    logging.debug('Starting')
    time.sleep(.5)
    logging.debug('Exit')
def mynon_daemon():
    logging.debug('Starting')
    logging.debug('Exit')
# threads=[]
# for i in range(5):
#     t = threading.Thread(target=worker,args=(i,))
#     threads.append(t)
#     t.start()

t = threading.Thread(name='my_srv', target=my_serv)
w = threading.Thread(name='worker', target=worker)
w2 = threading.Thread(target=worker)

# w.start()
# w2.start()
# t.start()


d = threading.Thread(name='mydaemon', target=mydaemon, daemon=True)
nd=threading.Thread(name='my non daemon', target=mynon_daemon)

# d.start()
# nd.start()
#
# d.join(.1)
# print('d.isAlive()', d.is_alive())
# nd.join()

print('-'*25)
import random
def randWorker():
    pause = random.randint(1,5)/10
    logging.debug('sleeping %0.2f',pause)
    time.sleep(pause)
    logging.debug('Exit')

for i in range(3):
    rt= threading.Thread(target=randWorker, daemon=True)
    rt.start()
main_thread = threading.main_thread()
for j in threading.enumerate(): #return all threads incl main thread< but we need disable main thread for prevent self-blocking
    if j is main_thread: continue
    logging.debug('joining %s', j.getName())
    j.join()