#!/usr/bin/python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import sys
import socket
import subprocess


#Espera de un segon, per defecte per a tot.
Tsleep = 1
#Temps de duració de café
Tcafe = 80

#Comprovar si tenim taça
# def checkTasa():
#   if(flag==1)
#     return true;
#   else
#     return false;

#Apretar i soltar el boto.
def botoCafe():
  GPIO.output(boto, GPIO.HIGH)
  print "[*]\tBoton PRESSED"
  time.sleep(Tsleep);
  GPIO.output(boto, GPIO.LOW)
  print "[*]\tBoton RELEASED"
  return;


#Obrir la tapa
def obriTapa():
  time.sleep(Tsleep)
  print "[/]\tTapa OBERTA"
  GPIO.output(tapa, GPIO.LOW)
  return;

#Tancar la tapa
def tancaTapa():
  GPIO.output(tapa, GPIO.HIGH)
  print "[\]\tTAPA Tancada"
  time.sleep(Tsleep);
  return;

#Tira Cafe
def tirar():
  print "[!]\tTirant Cafuá"
  for i in range(Tcafe*4):
    warning = GPIO.input(23)
    if warning == False:
       time.sleep(2)
       if warning == False:
         print ('[WARN]Parando Cafetera (implementar parar)')
         obriTapa()
         break
    time.sleep(0.25)
  print "[!]\tCafe FET!"
  return;

#Executar tot.
def faena():
  obriTapa()
  tancaTapa()
  botoCafe()
  tirar()
  obriTapa()
  return;


#Mode utilitzant Pins n GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#----Pins a utilitzar----
#17 es Control automàtic de tapadora tassimo
#18 es Control automàtic del boto de acció

pinsEixida = [17,18]
tapa = 17
boto = 18

#Config de pinsEixida, com a Eixida.
for i in pinsEixida:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.LOW)




if len(sys.argv) != 2:
  print "Arguments incorrectes!! \n Usage : ./tassimo.py PORT"
  sys.exit
else:
  port = int(sys.argv[1])
  s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

  interf="eth0"
  #Obtindre IP actual de la wlan0
  cmd = "/sbin/ifconfig "+str(interf)+" | grep 'inet addr:' | cut -d: -f2 | awk '{ print $1}'"
  r2 = subprocess.check_output(cmd, shell=True,stdin=None, stderr=None)
  gb = r2.replace('\n', u'')

  s.bind( (gb, port ))
  s.listen( 5 )
  print "------------VLC_Logic // ALC_Logic ORIGINAL-----------"
  print "Aceptant conexions en -> " +str(gb)+":"+str(port)+" en "+str(interf)
  print "------------------------------------------------------"

  while 1:
    c, (remhost, remport) = s.accept()
    resp = c.recv(100)

    if resp == 'cafe':
      print "------------VLC_Logic // ALC_Logic ORIGINAL-----------"
      print "[:D]\tFaena de Cafetera"
      print "[i]\tTemps de Cafe : "+str(Tcafe)
      print "--------------------------------------------------"
      faena()
      print "[:D]\tFinished!"
    else:
      print "[:?]\tS'ha rebut :"+str(resp)
    c.close()
