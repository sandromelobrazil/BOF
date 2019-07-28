#!/usr/bin/python3.6
import socket

remoteip = "10.171.1.129"
port=int("25") 
command='VRFY' 

#print("Teste de Conexao com o servidor SMTP... " + remoteip )
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((remoteip,port))
data = s.recv(1024)
print(data)


### running commad
with open('userlist.txt') as _dictionary:
    for _username in _dictionary:
        smtpcmd=(command + ' ' + _username + ' ' + ' \n')
        sendsmtpcmd=smtpcmd.encode()
        s.send(sendsmtpcmd)
        data = s.recv(1024)
        print(data)

s.close()
#print("\n Conta verificada!")
