
import threading
import logging
import time

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] (%(threadName)-10s) (%(message)s)'
)

def lock_holder(lock):
    logging.debug('starting')
    while 1:
        with lock:
            time.sleep(.5)
        time.sleep(.5)

def worker(lock):
    logging.debug('starting')
    retries = acquires =0
    while acquires < 3:
        time.sleep(.5)
        logging.debug('try to ascuire')
        have_it = lock.acquire(0)
        try:
            retries +=1
            if have_it:
                logging.debug(f'iter {retries}: acquired')
                acquires+=1
            else:
                logging.debug(f'iter {retries} not ascuired')
        finally:
            if have_it: lock.release()
    logging.debug(f'Done after {retries} iters')

class myThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon = None):
        super().__init__(group=group, name=name, target=target,daemon=daemon)
        self.args = args
        self.kwargs = kwargs

    def run(self):
        logging.debug(f'run with args - {self.args} and kwargs - {self.kwargs}')

class MyThread(threading.Thread):
    def __init__(self, group = None, name=None, target = None, args=(), kwargs = None, *,daemon = None):
        super().__init__(group=group, name=name, target=target, daemon=daemon)
        self.args = args
        self.kwargs = kwargs

    def run(self):
        logging.debug(f'run with args - {self.args} and kwargs - {self.kwargs}')

def my_thread_worker():
    for i in range(5):
       th = myThread(args=(i,), kwargs={1:2,3:4})
       th.start()


if __name__=='__main__':
    lock = threading.Lock()
    holder = threading.Thread(target=lock_holder, args=(lock,), daemon=True)
    holder.setName('Lock holder')
    holder.start()

    worker = threading.Thread(target=worker, args=(lock,))
    worker.setName('Worker')
    worker.start()
    # my_thread_worker()