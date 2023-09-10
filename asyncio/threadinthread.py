#!/usr/bin/env python

import threading
import multiprocessing
#
# def adder(x, res, i):
#     res[i] += x*i
#
# def creator(a, threads, results):
#     for i in range(a):
#         results.append(0)
#         t = threading.Thread(target=adder, args=(a, results, i))
#         threads.append(t)
#         t.start()
#     for t in threads:
#         t.join()
#
# threads = []
# results = []
#
# mainThread = threading.Thread(target=creator, args=(5, threads, results))
# mainThread.start()
# mainThread.join()
# for i in range(len(results)):
#     print results[i]
#     print threads[i]
import time
def uptime_bot(url):
    try:
        time.sleep(1)
    except Exception:
        pass
    else:
        # Website is up
        print('OP is up')

print(uptime_bot('dd'))