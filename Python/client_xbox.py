#!/usr/bin/env python2

import socket
import sys
import pygame
import os
import time

from pygame.locals import *

pygame.init()

remote_ip = '10.42.42.21' #IP DU SERVEUR

port = 8883 #PORT (comme son nom l'indique)

message = ''



### CREATION DU SOCKET

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #CONFIG DU SOCKET : AF_NET = IPV4, SOCK_STREAM = TCP

except socket.error:
        sys.exit();

print('Socket cree')



### CONNEXION AU SERVEUR

s.connect((remote_ip , port))

print('Socket connecte sur ' + remote_ip)



### ENVOI DE DONNEES

try :

   pad = pygame.joystick.Joystick(0)

   pad.init()

   while 1:

        mess = ''

        pygame.event.pump()

        valeur_x_g = int(100 + 100*pad.get_axis(0))

        if valeur_x_g < 10 :
            m_valeur_x_g = '00' + str(valeur_x_g)
        elif 10 <= valeur_x_g < 100 :
            m_valeur_x_g = '0' + str(valeur_x_g)
        else :
            m_valeur_x_g = str(valeur_x_g)


        valeur_y_g = int(100 - 100*pad.get_axis(1))

        if valeur_y_g < 10 :
            m_valeur_y_g = '00' + str(valeur_y_g)
        elif 10 <= valeur_y_g < 100 :
            m_valeur_y_g = '0' + str(valeur_y_g)
        else :
            m_valeur_y_g = str(valeur_y_g)


        valeur_x_d = int(512 + 512*pad.get_axis(4))

        if valeur_x_d < 10 :
            m_valeur_x_d = '000' + str(valeur_x_d)
        elif 10 <= valeur_x_d < 100 :
            m_valeur_x_d = '00' + str(valeur_x_d)
        elif 100 <= valeur_x_d < 1000 :
            m_valeur_x_d = '0' + str(valeur_x_d)
        else :
            m_valeur_x_d = str(valeur_x_d)


        valeur_y_d = int(512 - 512*pad.get_axis(3))

        if valeur_y_d < 10 :
            m_valeur_y_d = '000' + str(valeur_y_d)
        elif 10 <= valeur_y_d < 100 :
            m_valeur_y_d = '00' + str(valeur_y_d)
        elif 100 <= valeur_y_d < 1000 :
            m_valeur_y_d = '0' + str(valeur_y_d)
        else :
            m_valeur_y_d = str(valeur_y_d)


        valeur_trig = int(512 - 512*pad.get_axis(2))

        if valeur_trig < 10 :
            m_valeur_trig = '000' + str(valeur_trig)
        elif 10 <= valeur_trig < 100 :
            m_valeur_trig = '00' + str(valeur_trig)
        elif 100 <= valeur_trig < 1000 :
            m_valeur_trig = '0' + str(valeur_trig)
        else :
            m_valeur_trig = str(valeur_trig)


        b0 = str(pad.get_button(0))
        b1 = str(pad.get_button(1))
        b2 = str(pad.get_button(2))
        b3 = str(pad.get_button(3))
        b4 = str(pad.get_button(4))
        b5 = str(pad.get_button(5))
        b6 = str(pad.get_button(6))
        b7 = str(pad.get_button(7))
        b8 = str(pad.get_button(8))
        b9 = str(pad.get_button(9))

        cstick = pad.get_hat(0)

        cstick_g = str(cstick[0] + 1)
        cstick_d = str(cstick[1] + 1)

        #print("Valeur de l'axe x, joystick gauche : %d", valeur_x_g)
        #print("Valeur de l'axe y, joystick gauche : %d", valeur_y_g)
        #print("Valeur de l'axe x, joystick droit : %d", valeur_x_d)
        #print("Valeur de l'axe y, joystick droit : %d", valeur_y_d)
        #print("Valeur du trigger gauche : %d", valeur_trig_g)
        #print("Valeur du trigger droit : %d", valeur_trig_d)

        #print("Bouton A : ", b0)
        #print("Bouton B : ", b1)
        #print("Bouton X : ", b2)
        #print("Bouton Y : ", b3)
        #print("Bouton LB : ", b4)
        #print("Bouton RB : ", b5)
        #print("Bouton BACK : ", b6)
        #print("Bouton START : ", b7)
        #print("Bouton XBOX : ", b8)
        #print("Bouton LS : ", b9)
        #print("Bouton RS : ", b10)

        #print("C-STICK : ", cstick)

        message = [m_valeur_x_g, m_valeur_y_g, m_valeur_x_d, m_valeur_y_d, m_valeur_trig, b0, b1, b2, b3, b4, b5, b6, b7, b8, b9, cstick_g, cstick_d]

        for i in range (0, len(message)) :
            mess = mess + message[i]

        print(mess)

        s.sendall(mess)

        time.sleep(0.01)

except socket.error:
    #Erreur
    print ('Erreur')
    sys.exit()
