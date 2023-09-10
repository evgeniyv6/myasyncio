#!/usr/bin/env python

import asyncio
import sys, itertools

async def spin(msg):
    write, flush = sys.stdout.write, sys.stdout.flush
    for ch in itertools.cycle('|/-\\'):
        status = ch + ' ' + msg
        write(status)
        # print('\r'*len(status))
        flush()
        write('\x08'*len(status))
        try:
            await asyncio.sleep(.06)
        except asyncio.CancelledError:
            break
    write(' '*len(status) + '\x08'*len(status))

async def slow_func():
    await asyncio.sleep(5)
    return 42

async def supervisor(loop):
    spinner = loop.create_task(spin('thinking'))
    print('spinner obj: ', spinner)
    res = await slow_func()
    spinner.cancel()
    return res

def main():
    loop = asyncio.get_event_loop()
    res = loop.run_until_complete(supervisor(loop))
    loop.close()
    print(res)

if __name__=='__main__':
    main()