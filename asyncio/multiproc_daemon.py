#!/usr/bin/env python

import sys
import multiprocessing
import time
import logging

def my_daemon():
    d = multiprocessing.current_process()
    print('daemon start', d.name, d.pid)
    sys.stdout.flush()
    time.sleep(2)
    print('Exit ', d.name, d.pid)
    sys.stdout.flush()

def my_non_daemon():
    nd = multiprocessing.current_process()
    print('daemon start', nd.name, nd.pid)
    sys.stdout.flush()
    print('Exit ', nd.name, nd.pid)
    sys.stdout.flush()

if __name__=='__main__':
    multiprocessing.log_to_stderr()
    logger = multiprocessing.get_logger()
    logger.setLevel(logging.DEBUG)
    pd = multiprocessing.Process(
        name='daemon',
        target=my_daemon,
    )

    pd.daemon=True
    nd = multiprocessing.Process(
        name='non daemon',
        target=my_non_daemon,
    )
    nd.daemon=False

    pd.start()
    time.sleep(1)
    nd.start()

    pd.join()
    # nd.join()