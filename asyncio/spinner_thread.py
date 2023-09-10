#!/usr/bin/env python

import threading
import itertools
import sys
import time

class Signal:
    go = True

def spin(msg, signal):
    write, flush = sys.stdout.write, sys.stdout.flush
    for ch in itertools.cycle('|/-\\'):
        status = ch+' '+msg
        print(status,end='\r')
        print(end='\r', flush=True)
        time.sleep(.1)
        if not signal.go:
            break
    print(' '*len(status) + '\x08'*len(status), flush=True)

def slow_f():
    time.sleep(3)
    return 42

def supervisor():
    sig = Signal()
    spinner = threading.Thread(target=spin, args=('thinking!', sig))
    print('spinner obj: ', spinner)
    spinner.start()
    res = slow_f()
    sig.go=False
    spinner.join()
    return res

def main():
    res = supervisor()
    print(f'answer {res}')

if __name__=='__main__':
    main()