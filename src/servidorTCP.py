#!/usr/bin/env python

import argparse
import socket
from cryptography.fernet import Fernet

#Paso de argumentos
description = """ Modo de uso:
    cliente.py -msj "Mensaje a enviar"""

parser = argparse.ArgumentParser(description='Port scanning', epilog=description, formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-msj", metavar='MSJ', dest="msj", help="mensaje a enviar", required=True)
params = parser.parse_args()

#Generar el objeto para cifrar
clave = Fernet.generate_key()
cipher_suite = Fernet(clave)

#Almacenamos la clave
file - open('clave.key', 'wb') #Se guarda en bytes wb
file.write(clave)
file.close()

#Tomar el argumento, convertirlo a bytes
mensaje = params.msj
mensajeBytes = mensaje.encode()


