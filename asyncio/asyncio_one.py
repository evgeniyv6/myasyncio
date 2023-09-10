#!/usr/bin/env python

import asyncio


# 1st example
async def mycoro(name=None):
    print(f'inside coro {name}')
    return 'res from inside coro'

# evet_loop = asyncio.get_event_loop()
# try:
#     print('starting coro')
#     coro = mycoro('Sanka')
#     print('entering event loop')
#     ares = evet_loop.run_until_complete(coro)
#     print(f'returned val is: {ares}')
# finally:
#     print('closing event loop')
#     evet_loop.close()

print('='*25)
# second example
async def outer():
    print('in oter')
    print('wait for res1')
    res1 = await phase1()
    print('wait for res2')
    res2 = await phase2(res1)
    return (res1, res2)

async def phase1():
    print('in ph1')
    return 'res1'

async def phase2(arr):
    print('in ph2')
    return f'res2 derived from res1: {arr}'

# new_event_loop = asyncio.get_event_loop()
# try:
#     ret = new_event_loop.run_until_complete(outer())
#     print(f'ret val is: {ret}')
# finally:
#     new_event_loop.close()

print("-"*25)
# third example
import functools
def callback(arg, *args, kwarg='default'):
    print(f'callback with {arg}, {args} and {kwarg}')

async def main(loop):
    loop.call_soon(callback, 1,2,3)
    wrapped = functools.partial(callback, kwarg='not default')
    loop.call_soon(wrapped,4,5,6)
    await asyncio.sleep(3)

# newnew_event_loop = asyncio.get_event_loop()
# try:
#     print('entering event loop')
#     newnew_event_loop.run_until_complete(main(newnew_event_loop))
# finally: newnew_event_loop.close()

print('*'*25)

# 5th example
def mark_done(future, res):
    print('set future res to {!r}'.format(res))
    future.set_result(res)

async def main(loop):
    all_done = asyncio.Future()
    loop.call_soon(mark_done, all_done, 'the res')

    res = await all_done

    print(f'ret res: {res}')

# newnewnew_event_loop = asyncio.get_event_loop()
# newnewnew_event_loop.run_until_complete(main(newnewnew_event_loop))
# newnewnew_event_loop.close()

print('*'*10+'-'*15)
# 6th example
def cb(future, n):
    print(f'{n}: future done: {future.result()}')

async def reg_cb(all_done):
    print('reg cb on future')
    all_done.add_done_callback(functools.partial(cb,n=1))
    all_done.add_done_callback(functools.partial(cb, n=2))

async def main(all_done):
    await reg_cb(all_done)
    print('set res to future')
    all_done.set_result('the res')

# newnewnew_event_loop = asyncio.get_event_loop()
# all_done = asyncio.Future()
# newnewnew_event_loop.run_until_complete(main(all_done))
# newnewnew_event_loop.close()

print('i-'*25)
# 7th Task example

async def task_func():
    print('in task func')
    return 'the res'
async def main(loop):
    print('creating task')
    task = loop.create_task(task_func())
    print(f'wait for task {task}')
    ret_val = await task
    print(f'task completed: {task}')
    print(f'ret val - {ret_val}')
# newnewnew_event_loop = asyncio.get_event_loop()
# newnewnew_event_loop.run_until_complete(main(newnewnew_event_loop))
# newnewnew_event_loop.close()

# 8th Cancel task example
async def task_f():
    print('in task func, slepping...')
    try:
        await asyncio.sleep(1)
    except asyncio.CancelledError:
        print('task was calcelled')
        raise
    return 'the res'

def task_canceller(t):
    print('in task canceller')
    t.cancel()
    print('task cancel')

async def main(loop):
    print('create task')
    task = loop.create_task(task_f())
    loop.call_soon(task_canceller, task)
    try:
        await task
    except asyncio.CancelledError:
        print('main also sees task as canceled')

event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()


