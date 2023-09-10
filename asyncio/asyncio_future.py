#!/usr/bin/env python

import asyncio
from concurrent.futures import FIRST_COMPLETED

# 1st
async def wrapped():
    print('wrapped')
    return 'res'

async def inner(task):
    print('inner: start')
    print(f'inner: wait for {task}')
    res = await task
    print(f'inner: task ret {res}')

async def starter():
    print('starter: create task')
    task = asyncio.ensure_future(wrapped())
    print('starter: wait for inner')
    await inner(task)
    print('starter: inner ret')
# event_loop = asyncio.get_event_loop()
# try:
#     print('enter event loop')
#     res = event_loop.run_until_complete(starter())
# finally:
#     event_loop.close()

# 2nd

async def phase(i):
    try:
        print(f'in phase {i}')
        await asyncio.sleep(i)
        print(f'done phase {i}')
    except asyncio.CancelledError:
        print('task canceled')
    return f'phase res - {i}'

async def main(num):
    print('starting main')
    phases = [phase(i) for i in range(num)]
    print('wait phase complete')
    completed, pending = await asyncio.wait(phases, return_when=FIRST_COMPLETED)
    for fut in pending: fut.cancel()
    res = [t.result() for t in completed]
    print(f'res: {res}')

event_loop = asyncio.get_event_loop()
try:
    print('enter event loop')
    res = event_loop.run_until_complete(main(5))
finally:
    event_loop.close()