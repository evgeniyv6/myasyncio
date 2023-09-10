#!/usr/bin/env python

import asyncio
import logging
import sys

MSG = [b'This is the msg. ', b'It will be sent ', b'in parts. ',]

SRV_ADDR = ('localhost', 10000)

logging.basicConfig(level=logging.DEBUG,format='%(name)s: %(message)s', stream=sys.stderr)

log = logging.getLogger('main')

event_loop = asyncio.get_event_loop()

async def echo_client(address, msg):
    log = logging.getLogger('echo_client')
    log.debug('connection to {} on port {}'.format(*address))
    reader, writer = await asyncio.open_connection(*address)

    for m in msg:
        writer.write(m)
        log.debug(f'sending {m}')
    if writer.can_write_eof(): writer.write_eof()
    await writer.drain()
    log.debug('wait resp')
    while True:
        data = await reader.read(128)
        if data:
            log.debug(f'received {data}')
        else:
            log.debug('closing')
            writer.close()
            return
try:
    event_loop.run_until_complete(echo_client(SRV_ADDR, MSG))
finally:
    log.debug('closing event loop')
    event_loop.close()