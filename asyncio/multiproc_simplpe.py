import multiprocessing
import time

def worker():
    name = multiprocessing.current_process().name
    print(name,'Starting')
    time.sleep(1)
    print(name,'Exit')

def mySrv():
    name = multiprocessing.current_process().name
    print(name, 'Start')
    time.sleep(3)
    print(name,'Exiting')


if __name__=='__main__':
    jobs=[]
    # for i in range(5):
    #     p = multiprocessing.Process(target=worker, args=(i,),)
    #     # jobs.append(p)
    #     p.start()

    srv = multiprocessing.Process(
        name = 'my_srv',
        target=mySrv,
    )

    w1 = multiprocessing.Process(
        name='worker1',
        target=worker,
    )

    w2=multiprocessing.Process(
        target=worker,
    )

    w1.start()
    w2.start()
    srv.start()