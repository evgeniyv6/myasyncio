#!/usr/bin/env python

import asyncio
import sys
import logging

SRV_ADDR = ('localhost', 10000)

logging.basicConfig(level=logging.DEBUG,format='%(name)s: %(message)s', stream=sys.stderr)

log = logging.getLogger('main')

event_loop = asyncio.get_event_loop()

async def echo(reader, writer):
    address = writer.get_extra_info('peername')
    log = logging.getLogger('echo_{}_{}'.format(*address))
    log.debug('connection accepted')
    while True:
        data = await reader.read(128)
        if data:
            log.debug(f'received {data}')
            writer.write(data)
            await writer.drain()
            log.debug(f'sent {data}')
        else:
            log.debug('closing')
            writer.close()
            return

factory = asyncio.start_server(echo, *SRV_ADDR)
srv = event_loop.run_until_complete(factory)
log.debug('starting {} on port {}'.format(*SRV_ADDR))

try:
    event_loop.run_forever()
except KeyboardInterrupt: pass
finally:
    log.debug('closing srv')
    srv.close()
    event_loop.run_until_complete(srv.wait_closed())
    log.debug('closing event loop')
    event_loop.close()