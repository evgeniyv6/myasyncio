#!/usr/bin/env python

import asyncio
import functools

async def run_df(loop):
    print('in run_df')
    cmd_done = asyncio.Future(loop=loop)
    factory = functools.partial(DFProtocol, cmd_done)
    proc = loop.subprocess_exec(factory, 'df', '-hl', stdin=None, stderr=None)
    try:
        print('launch proc')
        transport, protocol = await proc
        print('wait for proc to complete')
        await cmd_done
    finally:
        transport.close()
    return cmd_done.result()

class DFProtocol(asyncio.SubprocessProtocol):
    FD_NAMES = ['stdin', 'stdout', 'stderr']
    def __init__(self, done_fut):
        self.done = done_fut
        self.buffer = bytearray()
        super().__init__()

    def connection_made(self, transport):
        print(f'proc started {transport.get_pid()}')
        self.transport = transport

    def pipe_data_received(self, fd, data):
        print('read {} bytes from {}'.format(len(data), self.FD_NAMES[fd]))
        if fd==1: self.buffer.extend(data)

    def process_exited(self):
        print('process exited')
        rc = self.transport.get_returncode()
        print(f'return code: {rc}')
        if not rc:
            cmd_output = bytes(self.buffer).decode()
            res = self._parse_res(cmd_output)
        else:
            res=[]
        self.done.set_result((rc,res))

    def _parse_res(self, output):
        if not output: return []
        lines=output.splitlines()
        headers=lines[0].split()
        devices=lines[1:]
        res=[dict(zip(headers, l.split())) for l in devices]
        return res
event_loop = asyncio.get_event_loop()
try:
    rc, res = event_loop.run_until_complete(run_df(event_loop))
finally:
    event_loop.close()

if rc: print(f'err exit {rc}')
else:
    print('\nFree space')
    for r in res: print('{Mounted:25}: {Avail}'.format(**r))