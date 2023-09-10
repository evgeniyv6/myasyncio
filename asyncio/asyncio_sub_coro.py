#!/usr/bin/env python

import asyncio
import asyncio.subprocess

async def run_df():
    print('in run_df')
    buffer=bytearray()

    create=asyncio.create_subprocess_exec('df','-hl', stdout=asyncio.subprocess.PIPE,)

    print('launching process')
    proc = await create
    print(f'proc started {proc.pid}')

    while 1:
        line = await proc.stdout.readline()
        print(f'read {line}')
        if not line:
            print('no output')
            break
        buffer.extend(line)
    print('wait proc complete')
    await proc.wait()

    def parse_res(output):
        if not output: return []
        lines=output.splitlines()
        headers=lines[0].split()
        devices=lines[1:]
        res=[dict(zip(headers, l.split())) for l in devices]
        return res

    rc = proc.returncode
    print(f'rc - {rc}')
    if not rc:
        cmd_output = bytes(buffer).decode()
        res=parse_res(cmd_output)
    else:
        res=[]
    return (rc,res)

event_loop = asyncio.get_event_loop()
try:
    rc, res = event_loop.run_until_complete(run_df())
finally:
    event_loop.close()
if rc:
    print(f'err exit {rc}')
else:
    print('\nFree space')
    for r in res: print('{Mounted:25}: {Avail}'.format(**r))