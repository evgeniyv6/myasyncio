#!/usr/bin/env python

import asyncio
import functools

async def coroutine():
    print('in coroutine.start sleep 10')
    await asyncio.sleep(10)
    return 'coro result'

async def coroutine2():
    print('on coroutine 2. sleep 5')
    await asyncio.sleep(5)
    return 'coro2 res'

def callback(arr, * , kw = 'default'):
    print('callback with {} and {}'.format(arr, kw))

async def outer():
    print('in outer')
    print('wait res1')
    await coroutine()
    print('wait res2')
    await coroutine2()
    return 'outer res'


async def maincallback(loop):
    loop.call_soon(callback, '1arg')
    xx = functools.partial(callback, kw='not default')
    loop.call_soon(xx, '2arg')
    await asyncio.sleep(.1)

event_loop = asyncio.get_event_loop()

try:
    print('start coro')
    print('enter event loop')
    event_loop.run_until_complete(maincallback(event_loop))
finally:
    print('close event loop')
    event_loop.close()