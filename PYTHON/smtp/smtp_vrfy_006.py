#!/usr/bin/python3.6
import socket
from termcolor import colored

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
        _smtpcode = data[:3]
        if "252" in str(_smtpcode):
            print (colored('[+]' ,'green'), "[+] BINGO - O conta usuario -> " , _username , " enumerada.")

        if "550" in str(_smtpcode):
            print (colored('[-]' ,'yellow'), "[-] FAIL - O conta usuario -> " , _username , " nao existe.")

        if "503" in str(_smtpcode):
            print (colored('[!]' ,'red'), "[!] ERRO - Esse servidor requer autenticacao no SMTP!!! ") 

        if "500" in str(_smtpcode):
            print (colored('[!]' ,'red'), "[!] FALHOU - O comando VRFY nao eh suportado nesse servidor!!! ") 
            break

s.close()
#print("\n Conta verificada!")
