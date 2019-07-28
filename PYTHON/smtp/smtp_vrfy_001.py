#!/usr/bin/python3.6

import socket

remoteip = "10.171.1.129"
port=int("25") 
user='msfadmin' 
command='VRFY' 
msg='helo server' 

print("\nTeste de Conexao com o servidor SMTP... " + remoteip )

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((remoteip,port))

greeting=encode('helo mailserver'}
s.send(greeting)
data = s.recv(1024)
print(data)

msg=(command + ' ' + user + ' ' + '\r\n' )

sendmsg=msg.encode()

print(sendmsg)

s.send(sendmsg)
data = s.recv(1024)
print(data)

'''
s.send(command + " " + user + '\r\n')
data = s.recv(1024)
print(data)

s.close()
print("\n Conta verificada!")
'''
