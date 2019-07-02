#!/usr/bin/python

import struct
import socket

remoteip = "172.16.162.136"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	print "\nTeste de Conexao..."
	s.connect((remoteip,110))
	data = s.recv(1024)
	print data
	
	s.send('USER eder' +'\r\n')
	data = s.recv(1024)
	print data
	
	s.send('PASS entrar\r\n')
	data = s.recv(1024)
	print data
	
	s.close()
	print "\nTeste Realizado!"

except:
	print "Nao consegui conectar no POP3!"
