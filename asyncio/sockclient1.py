#!/usr/bin/env python

import socket, sys


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


srv_addr = ('localhost', 10002)

print('conn on {} to port'.format(* srv_addr))

sock.connect(srv_addr)

try:
    msg=b'this msg will be repeat'
    print(f'sending {msg}')
    sock.sendall(msg)

    amount_receive=0
    amount_expected=len(msg)

    while amount_receive<amount_expected:
        data=sock.recv(16)
        amount_receive +=len(data)
        print(f'receive {data}')
finally: sock.close()