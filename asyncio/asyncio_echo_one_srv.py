#!/usr/bin/env python

import asyncio
import logging
import sys

SRV_ADDR = ('localhost', 10000)

logging.basicConfig(level=logging.DEBUG,format='%(name)s: %(message)s', stream=sys.stderr)

log = logging.getLogger('main')

event_loop = asyncio.get_event_loop()

class EchoServer(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport
        self.address = transport.get_extra_info('peername')
        self.log = logging.getLogger('EchoServer_{}_{}'.format(*self.address))
        self.log.debug('connection accepted')

    def data_received(self, data):
        self.log.debug(f'received {data}')
        self.transport.write(data)
        self.log.debug(f'sent {data}')

    def eof_received(self):
        self.log.debug('received EOF')
        if self.transport.can_write_eof():
            self.transport.write_eof()

    def connection_lost(self, exc):
        if exc:
            self.log.debug(f'connection lost, error: {exc}')
        else:
            self.log.debug('connection close')
        super().connection_lost(exc)

factory = event_loop.create_server(EchoServer, *SRV_ADDR)
srv = event_loop.run_until_complete(factory)
log.debug('starting {} on port {}'.format(*SRV_ADDR))

try:
    event_loop.run_forever()
finally:
    log.debug('closing srv')
    srv.close()
    event_loop.run_until_complete(srv.wait_closed())
    log.debug('closing event loop')
    event_loop.close()
