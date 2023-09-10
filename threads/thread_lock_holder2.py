import threading
import logging
import time

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] (%(threadName)-10s) (%(message)s)'
)

def lock_holder(lock):
    logging.debug('start lock holder daemon')
    while 1:
        with lock:
            time.sleep(.5)
        time.sleep(.5)

class myThread(threading.Thread):
    def __init__(self, group=None, name=None,target=None,daemon=None, kwargs=None, args=()):
        super(myThread, self).__init__(group=group, name=name,target=target,daemon=daemon)
        self.kwargs=kwargs
        self.args=args

    def run(self):
        acquire=retr=0
        logging.debug('start my thread run')
        lock = self.args[0]
        while acquire < 3:
            retr+=1
            time.sleep(.5)
            have_it = lock.acquire(0)
            try:
                if have_it:
                    logging.debug(f'have_it after {retr} iters')
                    acquire+=1
                else:
                    logging.debug('do some other work')
            finally:
                if have_it: lock.release()

def event_wait(e):
    logging.debug('wait event')
    is_event = e.wait()
    logging.debug(f'event set {is_event}')

def event_timeout(e,t):
    logging.debug('start event timeout')
    while not e.is_set():
        is_set = e.wait(t)
        if is_set:
            logging.debug(f'wait event is set {is_set}')
        else: logging.debug('do some other work')

def cond_consumer(cond):
    logging.debug('start cond consumer')
    with cond:
        cond.wait()
        logging.debug('get resourese')

def cond_producer(cond):
    logging.debug('start cond producer')
    with cond:
        logging.debug('make res available')
        cond.notifyAll()

def bar_worker(bar):
    logging.debug(f'bar {bar.n_waiting}')
    try:
        bar.wait()
    except threading.BrokenBarrierError:
        logging.debug('bar abort')
    else:
        logging.debug('bar work')


class ActivePool:
    def __init__(self):
        # Rsuper(ActivePool, self).__init__()
        self.active=[]
        self.lock = threading.Lock()

    def makeActive(self, name):
        with self.lock:
            self.active.append(name)
            logging.debug(f'running {self.active}')

    def makeInactive(self, name):
        with self.lock:
            self.active.remove(name)
            logging.debug(f'running {self.active}')

def pool_worker(s, pool):
    logging.debug('start pool worker')
    with s:
        name = threading.current_thread().getName()
        pool.makeActive(name)
        time.sleep(.2)
        pool.makeInactive(name)

if __name__=='__main__':
    # lock = threading.Lock()
    # dt=threading.Thread(name='lock holder', target=lock_holder, args=(lock,), daemon=True)
    # dt.start()
    # mt = myThread(name=f'my thread',args=(lock,))
    # mt.start()

    # e = threading.Event()
    #
    # tw = threading.Thread(name=f'event waiter', target=event_wait, args=(e,))
    # twt = threading.Thread(name='event timeout waiter', target=event_timeout, args=(e,1,))
    # tw.start();twt.start()
    # time.sleep(5)
    # e.set()
    # logging.debug('event is set')
    # cond=threading.Condition()
    # for i in range(4):
    #     t = threading.Thread(name=f'worker # {i}', target=cond_consumer, args=(cond,))
    #     t.start()
    # time.sleep(5)
    # tp = threading.Thread(name='start producer', target=cond_producer, args=(cond,))
    # tp.start()
    # main_t = threading.main_thread()

    # NUM_THREADS = 3
    #
    # bar = threading.Barrier(NUM_THREADS)
    # for i in range(NUM_THREADS):
    #     t = threading.Thread(name=f'worker # {i}', target=bar_worker, args=(bar,))
    #     t.start()
    # time.sleep(5)
    # bar.abort()
    print(myThread.__mro__)
    pool = ActivePool()
    s=threading.Semaphore(3)
    for i in range(5):
        t = threading.Thread(name=f'worker # {i}',target=pool_worker, args=(s, pool,))
        t.start()




