#!/usr/bin/env python

import asyncio
import logging
import sys
import itertools
import warnings
import time

SLEEP_TIMEOUT = .1

logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)7s: %(message)s',
    stream=sys.stderr
)
LOG = logging.getLogger('')

async def coro_one():
    await asyncio.sleep(15)
    # LOG.info('hi from coro')
    return 'result'
async def coro_iter(i):
    await asyncio.sleep(.5 - (.1 * i))
    # LOG.info('hi from coro')
    return f'result {i}'


async def spinner():
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        write(char)
        flush()
        write('\x08'*len(char))
        time.sleep(.1)
        try:
            await asyncio.sleep(SLEEP_TIMEOUT)
        except asyncio.CancelledError:
            write(' ' * len(char) + '\x08' * len(char))
            flush()
            break

async def main():
    LOG.info('start main')
    task1 = asyncio.ensure_future(coro_one())
    task2 = asyncio.ensure_future(spinner())
    completed, pending = await asyncio.wait([task1, task2], return_when=asyncio.FIRST_COMPLETED)
    if pending:
        # LOG.info('cancel pending coro')
        for p in pending:
            p.cancel()
    # LOG.info('exit main')

async def main2(num=3):
    res = []
    phases = [coro_iter(i) for i in range(num)]
    for next_to_complete in asyncio.as_completed(phases):
        answ = await next_to_complete
        res.append(answ)
    print(res)
    return res

# el = asyncio.get_event_loop()
# el.set_debug(True)
# try:
    # LOG.info('start coro')
    # coro = coro_one()
    # LOG.info('enter event loop')
    # res = el.run_until_complete(coro)
    # LOG.info(f'res is {res}')
# except:
#     el.close()

if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    event_loop.set_debug(True)
    event_loop.slow_callback_duration = 0.00001
    warnings.simplefilter('always', ResourceWarning)
    try:
        res = asyncio.run(main())
        LOG.info(res)
    finally:
        event_loop.close()
