#Socket client
 
import socket 
import sys 
import pygame
import os
import time

from pygame.locals import *

pygame.init()

remote_ip = '10.42.42.15' #IP DU SERVEUR

port = 8883 #PORT (comme son nom l'indique)

message = ''



### CREATION DU SOCKET

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #CONFIG DU SOCKET : AF_NET = IPV4, SOCK_STREAM = TCP

except socket.error:
        sys.exit(); 

print 'Socket crée'



### CONNEXION AU SERVEUR

s.connect((remote_ip , port))
 
print 'Socket connecté sur ' + remote_ip



### ENVOI DE DONNEES
 
try :

        while 1:
        
            myjoystick = pygame.joystick.Joystick(0)

            myjoystick.init()

            pygame.event.pump()
	
            valeur_x = myjoystick.get_axis(0)
            valeur_y = myjoystick.get_axis(1)

            message_x = ''
            message_y = ''

            if -0.01 < valeur_x < 0.01 :
                    valeur_x = 0

            if 0.99 < valeur_x :
                    valeur_x = 1

            if valeur_x < -0.99 :
                    valeur_x = -1

            if -0.01 < valeur_y < 0.01 :
                    valeur_y = 0

            if 0.99 < valeur_y :
                    valeur_y = 1

            if valeur_y < -0.99 :
                    valeur_y = -1

            vitesse_x = int(100 + 100 * valeur_x)
            vitesse_y = int(100 - 100 * valeur_y)


            if vitesse_x < 10:
                    message_x = '00' + str(vitesse_x)

            elif 10 <= vitesse_x < 100:
                    message_x = '0' + str(vitesse_x)

            else:
                    message_x = str(vitesse_x)


            if vitesse_y < 10:
                    message_y = '00' + str(vitesse_y)

            elif 10 <= vitesse_y < 100:
                    message_y = '0' + str(vitesse_y)

            else:
                    message_y = str(vitesse_y)

            message = 'X' + message_x + 'Y' + message_y + '$'

            print(message)

            s.sendall(message)
            
            time.sleep(0.01)
            
except socket.error:
    #Erreur
    print 'Erreur'
    sys.exit()
 
print 'Message envoyé'











