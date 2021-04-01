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
    msj_cifrado = conn.recv(BUFFER_SIZE)
    conn.send(b"Enterado. Bye!")
    break
conn.close()

#Generar el objeto para cifrar
file = open('clave.key','rb')
clave = file.read()
file.close()
cipher_suite = Fernet(clave)

mensajeBytes = cipher_suite.decrypt(msj_cifrado, None)
mensaje = mensajeBytes.decode()
print("Mensaje recibido:\n". mensaje)

