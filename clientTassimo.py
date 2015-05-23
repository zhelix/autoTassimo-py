#!/usr/bin/python -tt
#Sockets i tal.
import socket
import sys

#Numero incorrecte de parametros
if len(sys.argv) != 4:
  print "Arguments incorrectes!! \n Usage : ./clientTassimo.py ADDR PORT ORDRE         pe: cafe"
  sys.exit
else:  
  #Creem el socket VLC_Logic
  addr   = str(sys.argv[1])
  port   = int(sys.argv[2])
  msg    = str(sys.argv[3])
  s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
  s.connect( ( addr , port) )
  s.send(msg)
