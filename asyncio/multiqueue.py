#!/usr/bin/env python

import multiprocessing
import time
import logging

class Consumer(multiprocessing.Process):
    def __init__(self, task_q, res_q):
        multiprocessing.Process.__init__(self)
        self.task_q = task_q
        self.res_q = res_q

    def run(self):
        pn = self.name
        while True:
            next_task = self.task_q.get()
            if next_task is None:
                print('{} Exiting'.format(pn))
                self.task_q.task_done()
                break
            print('{}:{}'.format(pn, next_task))
            answer = next_task()
            self.task_q.task_done()
            self.res_q.put(answer)

class Task:
    def __init__(self, a, b):
        self.a=a
        self.b=b
    def __call__(self):
        time.sleep(.1)
        return '{self.a} * {self.b} = {product}'.format(self=self, product=self.a*self.b)
    def __repr__(self):
        return '{self.a} * {self.b}'.format(self=self)

if __name__=='__main__':
    # multiprocessing.log_to_stderr(logging.DEBUG)
    tasks=multiprocessing.JoinableQueue()
    res=multiprocessing.Queue()
    num_consumers=multiprocessing.cpu_count()*2
    print('Create {} consumers'.format(num_consumers))
    consumers = [Consumer(tasks, res) for i in range(num_consumers)]
    for w in consumers: w.start()

    num_jobs = 10
    for i in range(num_jobs): tasks.put(Task(i,i+1))
    for i in range(num_consumers): tasks.put(None)

    tasks.join()

    while num_jobs:
        myres=res.get()
        print('Res: ', myres)
        num_jobs -= 1