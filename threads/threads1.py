import threading
import random
import time
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] (%(threadName)-15s) (%(message)s)'
)

class MyCounter:
    def __init__(self, start=0):
        self.lock = threading.Lock()
        self.val = start

    def inc(self):
        with self.lock:
            self.val +=1

def worker(c):
    for _ in range(5):
        pause = random.random()
        time.sleep(pause)
        c.inc()

if __name__ == '__main__':
    c = MyCounter()
    main_thread = threading.main_thread()

    for _ in range(5):
        t = threading.Thread(target=worker,args=(c,))
        t.start()
    for th in threading.enumerate():
        if th is main_thread: continue
        else: th.join()
    logging.debug(c.val)