#!/usr/bin/env python

import argparse
import socket
from cryptography.fernet import Fernet

#Preparamos los datos de la conexion
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 2048

#Establecemos la conexion
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

(conn, addr) = s.accept()
print('Direccion de conexion: ', addr)
while True:
    mss_cifrado = conn.recv(BUFFER_SIZE)
    conn.send(b"Enterado. Bye!")
    break
conn.close()