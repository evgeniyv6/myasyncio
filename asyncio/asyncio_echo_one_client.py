#!/usr/bin/env python

import asyncio
import logging
import sys
import functools

MSG = [b'This is the msg. ', b'It will be sent ', b'in parts. ',]

SRV_ADDR = ('localhost', 10000)

logging.basicConfig(level=logging.DEBUG,format='%(name)s: %(message)s', stream=sys.stderr)

log = logging.getLogger('main')

event_loop = asyncio.get_event_loop()

class EchoClient(asyncio.Protocol):
    def __init__(self, msg, future):
        super().__init__()
        self.msg = msg
        self.log = logging.getLogger('EchoClient')
        self.fut = future

    def connection_made(self, transport):
        self.transport = transport
        self.address = transport.get_extra_info('peername')
        self.log.debug('connecting to {} port {}'.format(*self.address))
        for m in self.msg:
            transport.write(m)
            self.log.debug(f'sending {m}')
        if transport.can_write_eof(): transport.write_eof()

    def data_received(self, data):
        self.log.debug(f'received {data}')

    def eof_received(self):
        self.log.debug('received EOF')
        self.transport.close()
        if not self.fut.done():
            self.fut.set_result(True)

    def connection_lost(self, exc):
        self.log.debug('server closed conn')
        self.transport.close()
        if not self.fut.done():
            self.fut.set_result(True)
        super().connection_lost(exc)

client_completed = asyncio.Future()

client_factory = functools.partial(EchoClient, msg=MSG,future=client_completed)

factory_coroutine = event_loop.create_connection(client_factory, *SRV_ADDR)

log.debug('wait client complete')
try:
    event_loop.run_until_complete(factory_coroutine)
    event_loop.run_until_complete(client_completed)
finally:
    log.debug('closing event loop')
    event_loop.close()


