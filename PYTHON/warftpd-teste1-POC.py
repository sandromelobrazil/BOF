#!/usr/bin/python

import socket, time


remoteip="172.16.162.136"

print "POC de Conexao - Buffer Overflow no USER do FTP"
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
        s.connect((remoteip, 21))
except:
        print ("[-] Connection error!")
        sys.exit(1)

print s.recv(1024)
print "Sending username..."
s.send('USER anonymous\r\n')
print s.recv(1024)
print "Sending pass..."
s.send('PASS eder@eder.com\r\n')
print s.recv(1024)
s.close()
