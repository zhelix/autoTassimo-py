#!/usr/bin/python -tt
#Sockets i tal.
import socket
import sys
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Numero incorrecte de parametros
if len(sys.argv) != 4:
    print "Arguments incorrectes!! \n Usage : ./clientBoto.py ADDR PORT ORDRE         pe: cafe"
    sys.exit
else:
    pausas=320
    while True:
        input_state = GPIO.input(23)
        if input_state == False:
            time.sleep(2)
            if input_state == False:
                print ('Sirviendo CAFE. . .')    
                #Creem el socket VLC_Logic
                addr   = str(sys.argv[1])
                port   = int(sys.argv[2])
                msg    = str(sys.argv[3])
                s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
                s.connect( ( addr , port) )
                s.send(msg)

