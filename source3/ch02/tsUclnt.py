#!/usr/bin/env python

from socket import *

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udp_client = socket(AF_INET,SOCK_DGRAM)
udp_client.connect(ADDR)

while True:
    data = input('> ')
    if not data:
        break
    udp_client.sendto(data.encode(),ADDR) #以bytes方式发送
    data ,addr= udp_client.recvfrom(BUFSIZ)
    data=data.decode() #转换为str
    if not data:
        break
    print(data)

udp_client.close()

