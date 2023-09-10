#!/usr/bin/env python

import asyncio
import logging
import socket
import sys

async def main(loop, target):
    for t in target:
        info = await loop.getaddrinfo(*t, proto = socket.IPPROTO_TCP)
        for host in info: print(f'{t[0]}: {host[4][0]}')

event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop,[('vk.ru','https')]))
finally:
    event_loop.close()