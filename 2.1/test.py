from socket import *
import sys

connection_socket = socket(AF_INET, SOCK_STREAM)
connection_socket.connect((sys.argv[1], int(sys.argv[2])))
connection_socket.send(f"GET /{sys.argv[3]} HTTP/1.1".encode())

while True:
    try:
        message = connection_socket.recv(999)
        print(message)
    except error:
        break

