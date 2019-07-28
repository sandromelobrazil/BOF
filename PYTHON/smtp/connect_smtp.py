#!/usr/bin/python

import socket

remoteip = "10.171.1.129"
port=int("25") 
user="msfadmin" 
command="VRFY" 

print("\nTeste de Conexao com o servidor SMTP... " + remoteip )

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((remoteip,port))
data = s.recv(1024)
print(data)

