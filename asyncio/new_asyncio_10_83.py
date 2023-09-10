#!/usr/bin/env python

import asyncio

def mark_done(fut, res):
    print('in future')
    fut.set_result(res)

async def main_done(loop):
    myfut = asyncio.Future()
    loop.call_soon(mark_done, myfut, 'from main done to the mark done')
    res = await myfut
    print(res)

event_loop = asyncio.get_event_loop()

try:
    event_loop.run_until_complete(main_done(event_loop))
finally:
    event_loop.close()