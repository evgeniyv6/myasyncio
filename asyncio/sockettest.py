#!/usr/bin/env python


import socket

from urllib.parse import urlparse

URLS=('http://python.org', 'smtp://mail.example.com')

for url in URLS:
    pu=urlparse(url)
    port=socket.getservbyname(pu.scheme)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

srv_addr = ('', 10002)
print('start on {} port {}'.format(*srv_addr))
sock.bind(srv_addr)

sock.listen(1)

while 1:
    print('wait for a connect')
    conn, client_addr = sock.accept()
    try:
        print('conn from ', client_addr)
        while 1:
            data = conn.recv(16)
            print(f'received {data}')
            if data:
                print('send back')
                conn.sendall(data)
            else:
                print('no data from addr', client_addr)
                break
    finally:
        conn.close()