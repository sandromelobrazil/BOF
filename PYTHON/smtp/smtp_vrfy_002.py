#!/usr/bin/python3.6

import socket

remoteip = "10.171.1.129"
port=int("25") 
command='VRFY' 
msg='helo server' 

user1='msfadmin' 
user2='naruto' 
user3='jiraiya' 

#print("Teste de Conexao com o servidor SMTP... " + remoteip )
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((remoteip,port))
data = s.recv(1024)
print(data)


### running commad
smtpcmd=(command + ' ' + user1 + ' ' + ' \r\n')
sendsmtpcmd=smtpcmd.encode()
s.send(sendsmtpcmd)
data = s.recv(1024)
print(data)

smtpcmd=(command + ' ' + user2 + ' ' + ' \r\n')
sendsmtpcmd=smtpcmd.encode()
s.send(sendsmtpcmd)
data = s.recv(1024)
print(data)

smtpcmd=(command + ' ' + user3 + ' ' + ' \r\n')
sendsmtpcmd=smtpcmd.encode()
s.send(sendsmtpcmd)
data = s.recv(1024)
print(data)


s.close()
#print("\n Conta verificada!")
