import socket
import sys
import serial
import io

HOST = ''   
PORT = 8883 
 
socket_7Robot = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
 
try:
    socket_7Robot.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'

socket_7Robot.listen(10)
print 'Socket now listening'
 

conn, addr = socket_7Robot.accept()
print 'Connected with ' + addr[0] + ':' + str(addr[1])

ser=serial.Serial(
port='/dev/ttyUSB0',
baudrate=57600,
)

while 1:

	data = conn.recv(1024)

	ser.write(data)

	print(data)

conn.close()
socket_7Robot.close()
