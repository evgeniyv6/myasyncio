#!/usr/bin/env python

import asyncio
import asyncio.subprocess

async def to_upper(inp):
    print('in to_upper')
    create = asyncio.create_subprocess_exec('tr','[:lower:]','[:upper:]',stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    print('launch proc')
    proc = await create
    print(f'pid {proc.pid}')
    print('communic with proc')
    stdout, stderr = await proc.communicate(inp.encode())
    print('wait proc to complete')
    await proc.wait()

    # rc = proc.returncode
    # print(f'rc - {rc}')
    # if not rc: res = bytes(stdout).decode()
    # else: res=''

    return (rc, res)

MSG="""
This is message
next
"""

event_loop = asyncio.get_event_loop()
try:
    rc, res = event_loop.run_until_complete(to_upper(MSG))
finally:
    event_loop.close()
# if rc: print(f'err {rc}')
# else:
#     print(f'origin {MSG}')
#     print(f'new {res}')
