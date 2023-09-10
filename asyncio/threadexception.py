import sys
import threading
try:
    import Queue
except:
    import queue as Queue

class ExcThread(threading.Thread):
    def __init__(self, excqueue, group=None,target=None,name=None,args=(),kwargs=None,*,daemon=None):
        super().__init__(group=group,target=target,name=name,daemon=daemon)
        self.args = args
        self.kwargs = kwargs
        self.excqueue = excqueue
    def run(self):
        try:
            print(self.args[0])
            print(self.kwargs['user'])
            # raise Exception('An error occured here.')
        except Exception:
            self.excqueue.put(sys.exc_info())
def main():
    excqueue = Queue.Queue()
    thread_1 = ExcThread(excqueue,args=('s1', 's2',), kwargs=dict(user='myuser'))
    thread_1.setName('thread_1')
    thread_1.start()
    thread_2 = ExcThread(excqueue,args=('s3', 's4',), kwargs=dict(user='myuser2'))
    thread_2.setName('thread_2')
    thread_2.start()
    while True:
        try:
            exc = excqueue.get(block=False)
        except Queue.Empty:
            print('queue empty')
        else:
            exc_type, exc_obj, exc_trace = exc
            print("exc_type - {}, exc_obj - {}, exc_trace - {}".format(exc_type, exc_obj, exc_trace))
            if str(exc_obj):
                print('exit 1')
                sys.exit(1)

        thread_1.join(1)
        thread_2.join(1)
        if thread_1.is_alive() or thread_2.is_alive():
            continue
        else:
            break


if __name__ == '__main__':
    main()