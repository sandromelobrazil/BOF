#!/usr/bin/python3.6

import socket

remoteip = "10.171.1.129"
port=int("25") 
user='msfadmin' 
command='VRFY' 

print("\nTeste de Conexao com o servidor SMTP... " + remoteip )

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((remoteip,port))
data = s.recv(1024)
print(data)

s.send('VRFY'+'\r\n')
data = s.recv(1024)
print(data)

'''
s.send(command + " " + user + '\r\n')
data = s.recv(1024)
print(data)

s.close()
print("\n Conta verificada!")
'''
